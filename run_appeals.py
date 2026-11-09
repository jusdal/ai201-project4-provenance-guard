#!/usr/bin/env python3
"""
Run criterion 3 — the appeal path — three times.  <- UNIT 8, MILESTONE 3

    python app.py                                 # in one terminal
    python run_appeals.py --label before          # in another

`run_eval.py` only ever calls /submit, and an appeal needs a content_id that a
submission handed back first. So this does both, per trial:

  1. Submit 10 pieces of my own writing, each from its own creator_id.
  2. Appeal all 10: 5 with written reasoning, 3 with reasoning "", 2 with the
     field left out entirely.
  3. Read GET /log and check each appeal is there with the exact reasoning
     sent, and the original decision entry is still there, unchanged.
  4. Appeal a content_id that was never issued and expect a 404.

Unlike run_eval.py this one does decide pass/fail, because criterion 3's
checks are all exact: a status code, a field value, an entry that is or isn't
in the log.
"""

import argparse
import datetime as dt
import json
import sys

import config
import scenarios

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

# Reasoning sent with each of the 10 appeals. None means "leave the field out".
# What the log should hold for each is the same string, or "" for the last five.
REASONING = [
    "I wrote this myself for a graduate seminar. I can share my drafts.",
    "This is my own coursework. Formal academic writing is just how I write.",
    "I wrote every word of this. Please have a person look at it.",
    "My own essay from my master's program, written before AI tools existed.",
    "I'm the author. I have the original file with its edit history.",
    "",
    "",
    "",
    None,
    None,
]


def appeal_body(content_id, reasoning):
    body = {"content_id": content_id}
    if reasoning is not None:
        body["reasoning"] = reasoning
    return body


def run_trial(requests, url, trial, stamp, timeout):
    """One trial. Returns (checks, evidence): a list of per-appeal results and
    the raw JSON for the report."""
    texts = scenarios.MY_WRITING[: len(REASONING)]

    submitted = []
    for i, text in enumerate(texts, 1):
        creator_id = f"eval_appeal_{stamp}_t{trial}_{i}"
        response = requests.post(f"{url}/submit", timeout=timeout,
                                 json={"text": text, "creator_id": creator_id})
        payload = response.json()
        if response.status_code != 200:
            sys.exit(f"trial {trial}: submission {i} got {response.status_code} "
                     f"{payload} — criterion 3 can't be tested without a content_id")
        submitted.append(payload)

    # The decision entries as they stood before any appeal, to compare against.
    log_before = requests.get(f"{url}/log", timeout=timeout).json()["entries"]
    decisions_before = {
        e["content_id"]: e for e in log_before
        if e.get("status") == "decided" and e.get("content_id")
    }

    appeals = []
    for submission, reasoning in zip(submitted, REASONING):
        response = requests.post(f"{url}/appeal", timeout=timeout,
                                 json=appeal_body(submission["content_id"], reasoning))
        appeals.append((response.status_code, response.json()))

    log_after = requests.get(f"{url}/log", timeout=timeout).json()["entries"]

    checks = []
    for submission, reasoning, (status, payload) in zip(submitted, REASONING, appeals):
        content_id = submission["content_id"]
        entries = [e for e in log_after if e.get("content_id") == content_id]
        appeal_entries = [e for e in entries if e.get("event") == "appeal"]
        decision_entries = [e for e in entries if e.get("status") == "decided"]
        expected = reasoning if reasoning is not None else ""
        checks.append({
            "content_id": content_id,
            "reasoning_sent": "(field left out)" if reasoning is None else reasoning,
            "response_200": status == 200,
            "status_under_review": payload.get("status") == "under_review",
            "same_content_id": payload.get("content_id") == content_id,
            "appeal_logged_with_exact_reasoning": (
                len(appeal_entries) == 1 and appeal_entries[0].get("reasoning") == expected
            ),
            "decision_unchanged": (
                len(decision_entries) == 1
                and decision_entries[0] == decisions_before.get(content_id)
            ),
        })

    bogus_id = f"c_never_issued_{stamp}_{trial}"
    response = requests.post(f"{url}/appeal", timeout=timeout,
                             json={"content_id": bogus_id, "reasoning": "test"})
    not_found = {
        "status": response.status_code,
        "body": response.json(),
        "pass": response.status_code == 404
        and response.json().get("error") == "not_found",
    }

    first, empty = 0, len(REASONING) - 1  # one written, one left-out, for the report
    evidence = {
        "submit_response": submitted[first],
        "appeal_response_with_reasoning": appeals[first][1],
        "appeal_response_reasoning_left_out": appeals[empty][1],
        "log_entries_for_one_content_id": [
            e for e in log_after if e.get("content_id") == submitted[first]["content_id"]
        ],
        "log_entries_for_left_out_reasoning": [
            e for e in log_after if e.get("content_id") == submitted[empty]["content_id"]
        ],
        "never_issued_appeal": not_found,
    }
    return checks, not_found, evidence


def passed(check):
    return all(v for k, v in check.items() if k not in ("content_id", "reasoning_sent"))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    import requests

    problems = scenarios.validate()
    if problems:
        sys.exit("scenarios.py has problems — run_eval.py will list them.")
    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        sys.exit(f"Nothing answering at {args.url}. Start it:  python app.py")

    # Fresh creator_ids every run, so a second run the same day doesn't trip
    # the per-creator daily limit.
    stamp = dt.datetime.now().strftime("%H%M%S")
    trials = []
    for trial in range(1, args.trials + 1):
        checks, not_found, evidence = run_trial(requests, args.url, trial, stamp,
                                                args.timeout)
        n = sum(passed(c) for c in checks)
        print(f"  trial {trial}: {n}/{len(checks)} appeals pass · "
              f"never-issued id → {not_found['status']}")
        trials.append({"checks": checks, "not_found": not_found, "evidence": evidence})

    write_report(trials, args)


def write_report(trials, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"

    lines = [
        f"# Appeal run — criterion 3{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_appeals.py::main`",
        "- Service: `app.py::appeal` · log: `audit.py::log_appeal`, `GET /log`",
        f"- {len(trials)} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| Trial | Appeals passing all checks | Never-issued id → 404 |",
        "|---|---|---|",
    ]
    for i, t in enumerate(trials, 1):
        n = sum(passed(c) for c in t["checks"])
        lines.append(f"| {i} | {n}/{len(t['checks'])} | "
                     f"{'yes' if t['not_found']['pass'] else 'no'} "
                     f"({t['not_found']['status']}) |")

    for i, t in enumerate(trials, 1):
        lines += ["", f"## Trial {i}", "", "### Per-appeal checks", "", "```json",
                  json.dumps(t["checks"], indent=2), "```", "",
                  "### What actually came back", "", "```json",
                  json.dumps(t["evidence"], indent=2), "```"]

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
