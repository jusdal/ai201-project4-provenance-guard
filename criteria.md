# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Real writers are rarely labelled AI

Out of 20 human-written pieces (prose and poetry) in
`samples/clearly_human.json` — including the second-language paragraph traced
in `notes/milestone1.md` — **at most 1** comes back from `POST /submit` with
`guess: "ai"` (the high-confidence AI label). This must hold **in each of 3
trials**; a single trial with 2 is a miss.

**Why this target:** Telling a real writer their work looks AI-generated costs
them far more than missing some AI text costs the site, so "AI" should only be
said when the text is overwhelmingly synthetic and everything ambiguous should
fall into "unsure". The plain-writer paragraph is in the set on purpose: it's
the input both of my signals are weakest on, so a criterion without it would be
too easy.

> **Revised in unit 8 (2026-11-09, Milestone 3):** The 20 pieces are the
> second-language paragraph plus 19 pieces I wrote myself, one per file in
> `samples/my_writing/` (loaded by `scenarios.py::MY_WRITING`). The target is unchanged: at most 1 `guess: "ai"` in each of 3
> trials. Criterion 2's 15 human pieces are the first 15 of that list.
>
> **Why revised:** `samples/clearly_human.json` holds one piece, the
> instructor's demo text, not 20. So the original line pointed at a test set
> that didn't exist and couldn't be measured. Someone else's prose also can't
> show whether *my* writing gets wrongly flagged.

### Verdict (unit 8, Milestone 4): **MET**

**How I decided:** 0 of 20 came back `guess: "ai"` in trial 1, trial 2 and
trial 3 (`results/run_2026-11-09_1539_before.md`). The target was at most 1 in
every trial, so it holds.

**Honest reading:** it's met, but narrowly. All 20 landed in "unsure", none in
"human". The highest was `19.txt` at 0.7351, 0.015 under the 0.75 AI line, and 5
of 20 scored 0.69 or more. It passed because the unsure band is wide, not because
the signals read my writing as human. The attack set's false-positive family
shows how thin that margin is: 3 of its 8 human texts *were* labelled AI
(FP02, FP03, FP05). Those are short and use no punctuation beyond full stops and
commas. My writing has citations, quotations and dashes, which signal two reads
as human. This is the criterion I'd tighten: the same 20 pieces with none
scoring above 0.70, or with the false-positive attack texts added to the set.

---

## 2. Scores spread apart, and all three labels are reachable

Test suite: 15 clearly human pieces (`samples/clearly_human.json`), 15 clearly
AI pieces (`samples/clearly_ai.json`) and 6 borderline pieces
(`samples/borderline.json`), 36 in total. Using `combined_score` from each
response, in **each of 3 trials**:

- **Separation:** the mean `combined_score` of the 15 AI pieces is at least
  **0.40** higher than the mean of the 15 human pieces.
- **Coverage:** each of the three guesses (`"human"`, `"unsure"`, `"ai"`)
  appears **at least 4 times** across the 36 responses.

Both parts must pass for the criterion to pass.

**Why this target:** If scores bunch up around 0.5, the label is a coin flip
dressed up as a judgment. A 0.40 gap is the width of my unsure band
(0.35–0.80), so clear cases should land on opposite sides of it. Requiring 4 of
each label proves "unsure" is a working buffer, not dead code — and the
borderline set is what's meant to land there, so "unsure" isn't only reached
through misclassified clear cases.

> **Revised in unit 7 (2026-11-02, Milestone 4):** The unsure band is
> 0.35–0.75, not 0.35–0.80. The targets are unchanged: a mean gap of at least
> 0.40, and at least 4 of each label.
>
> **Why revised:** `AI_THRESHOLD` moved from 0.80 to 0.75 in Milestone 4. At
> 0.80 the clearly-AI calibration sample (combined 0.763) could never be
> labelled AI, so the "why" above described a band the code no longer uses.

> **Revised in unit 8 (2026-11-09, Milestone 3):** The 36 inputs are defined
> in `scenarios.py`. The 15 human pieces are the first 15 of
> `MY_WRITING` (my own writing, `samples/my_writing/`, see criterion 1).
> The 15 clearly-AI pieces are `CLEARLY_AI`, and the 6 borderline pieces are
> `BORDERLINE`. The targets are unchanged: a mean gap of at least 0.40, and at
> least 4 of each label, in each of 3 trials. Criterion 5 uses the same 36.
>
> **Why revised:** `samples/clearly_human.json`, `samples/clearly_ai.json` and
> `samples/borderline.json` each hold one piece, not 15, 15 and 6. They're
> single request bodies for the README's `curl` examples, so the original line
> pointed at test sets that didn't exist and couldn't be measured.

### Verdict (unit 8, Milestone 4): **MISSED**, both parts, in all 3 trials

**How I decided:** in each trial, the AI pieces averaged 0.885 and my 15 human
pieces averaged 0.574, a gap of **0.311** against a target of 0.40. The labels
were human **0** / unsure 21 / ai 15. "Unsure" and "ai" clear 4, but "human"
never appears. `combined_score` isn't recorded by `run_eval.py`, so I recomputed
it with `scoring.py::combine_signals`. Every value matched the recorded
`confidence` and `guess`.

**Diagnosis:** the shortfall is entirely on the human side. The AI pieces did
their job, and my writing scores too high to ever reach "human". Two stages
cause it, and the label threshold makes it arithmetic.

- **Signal one:** gpt2 finds my academic prose predictable. Across the 15
  pieces `model_score` runs 0.47–0.91 (mean 0.63), and none is under 0.47.
  Formal expository writing uses common words in conventional orders, which is
  what low perplexity measures. It's the same thing that put the Federalist
  paragraph and the second-language paragraph high.
- **Signal two, the sentence-length spread scale:** spread maps to 0.0 (human)
  only at 0.90. I set that from one calibration paragraph of choppy fiction. My
  expository writing spreads 0.34–0.62, so that measure scores it 0.40–0.80
  "AI". At 60% of the style score, it puts a floor of about 0.24 under
  `style_score` even when punctuation reads fully human. The lowest style score
  I got was 0.239.
- **Label mapping:** at 100+ words `combined_score` is the plain average, so
  "human" (< 0.35) needs `model + style < 0.70`. My best piece was 0.481 + 0.324
  = 0.805 → 0.402. With signal one never under 0.47 and signal two floored near
  0.24, no piece of mine can get there.

**Stage and mechanism:** signal two's spread scale is calibrated to fiction, so
it reads all expository prose as AI-leaning. Signal one reads formal prose as
predictable. Together they put the "human" label out of reach for an academic
writer.

---

## 3. Every appeal changes status and is recorded

10 appeals against 10 different `content_id`s returned by `/submit` — 5 with
written `reasoning` and 5 with `reasoning` empty or left out. For **10 of 10**:

- the response is HTTP 200 with `status: "under_review"` and the same
  `content_id`;
- `GET /log` shows an appeal entry for that `content_id` with the exact
  reasoning sent, and the original decision entry is still there, unchanged.

Also, an appeal for a `content_id` that was never issued returns **404** with
`{"error": "not_found", ...}`, in 3 of 3 attempts.

**Why this target:** The appeal is the only thing a wrongly flagged writer can
do, so it can't fail even once. Empty reasoning is tested on purpose: I made it
optional so a writer who can't argue in polished English can still appeal, and
that promise needs checking too.

### Verdict (unit 8, Milestone 4): **MET**

**How I decided:** `run_appeals.py::main` checked each appeal against all five
conditions with no judgment calls: HTTP 200, `status: "under_review"`, the same
`content_id`, an appeal entry in `GET /log` with the exact reasoning sent, and
the original decision entry unchanged. The result was 10 of 10 in all 3 trials
(5 written reasoning, 3 `""`, 2 field left out, logged as `""`). The
never-issued `content_id` returned 404 `not_found` in 3 of 3
(`results/appeals_2026-11-09_1549_before.md`).

**Honest reading:** this one is exact, so there's no generous reading to take.
What it doesn't test: appealing the same `content_id` twice, or an appeal
reasoning over the 2,000-character limit.

---

## 4. Bad input gets a clean 400, never a crash

Each of these 9 requests to `POST /submit` is sent 3 times (27 requests):

1. `text` missing
2. `creator_id` missing
3. `text` is `""`
4. `text` is whitespace only
5. `creator_id` is `""`
6. `text` is not a string (e.g. `123`)
7. body is not JSON
8. `text` too short to score (e.g. `"Hi."`)
9. `text` is 5,001 characters

**27 of 27** return HTTP 400 with a JSON body containing both `error` and
`message` (the shape in `notes/milestone1.md`). Zero responses are 500. After
the run, `POST /ping` still answers. A `text` of exactly 5,000 characters
returns 200 in 3 of 3 attempts.

**Why this target:** Bad input should fail cleanly and tell the caller what was
wrong, not crash the service or waste model time on megabytes of text. The
5,000-character check makes sure the limit sits exactly where the contract says
and doesn't reject a legitimate long piece.

### Verdict (unit 8, Milestone 4): **MISSED**, 26 of 27

**How I decided:** trials 1 and 2 were 9 of 9 → 400, but trial 3 was 8 of 9.
Case 5 (`creator_id: ""`) got **429**, not 400. Eight cases were sent by
`run_eval.py`. Case 7 (body not JSON) was sent by hand with `curl`, 3 of 3 →
400 (`results/not_json_2026-11-09.txt`). Every 400 had both `error` and
`message` (`results/bad_input_bodies_2026-11-09.txt`). There were zero 500s, the
5,000-character text got 200 in 3 of 3, and `POST /ping` answered 200 after the
run. Everything except the one 429 passed, but the target was 27 of 27, so it's
a miss.

**Diagnosis:**

- **Stage:** the route, or more exactly the rate limiter that sits in front of it.
- **Mechanism:** the `@limiter.limit(...)` decorator on `/submit` runs *before*
  `app.py::submit` validates anything. `rate_limit_key` counts a request against
  its `creator_id`, or against the caller's IP when there isn't one. Cases 2 and
  5 have no usable `creator_id`, so they share one IP bucket of 5 per minute. By
  trial 3 that bucket was full, and the malformed request was rejected for
  *rate* before the route could reject it for *content*.

This is the same mechanism as RQ10 and RQ11 in the attack run. Both were 429'd
before the route saw them, so how the route handles form-encoded and
`text/plain` bodies is still untested. The criterion predates the rate limiter
(added in unit 8, Milestone 1), but it's still measurable, so it stays a miss
rather than a revision.

---

## 5. Signal two actually changes outcomes

Across the 36 inputs from criterion 2, in **each of 3 trials**:

- **at least 5** inputs get a different `guess` than `model_score` alone would
  get under the same thresholds (below 0.35 → human, 0.80 or above → AI,
  otherwise unsure); and
- the mean of `|combined_score − model_score|` is **at least 0.10**.

Both are computed from the `model_score` and `combined_score` fields in each
response.

**Why this target:** The point of two signals is that the second one catches
what the first misses. If signal two never changes a label, the service is a
single-model detector with that model's blind spots — like calling plain human
writing AI. 0.10 is the smallest shift that can move a score across a threshold
often enough to matter.

> **Revised in unit 7 (2026-11-02, Milestone 4):** "The same thresholds" means
> below 0.35 → human, **0.75** or above → AI, otherwise unsure. Still at least
> 5 changed labels and a mean shift of at least 0.10.
>
> **Why revised:** `AI_THRESHOLD` moved from 0.80 to 0.75 in Milestone 4.
> Checked against 0.80, signal one alone would be judged on a cut-off the
> service never applies, so the count of changed labels wouldn't measure what
> signal two actually does.

### Verdict (unit 8, Milestone 4): **MISSED**, both parts, in all 3 trials

**How I decided:** in each trial **4** of 36 labels differed from what
`model_score` alone would give (target ≥ 5), and the mean
`|combined − model|` was **0.060** (target ≥ 0.10). Both numbers were identical
across all three trials.

**Diagnosis:**

- **Stage:** signal two, through the combining rule.
- **Mechanism:** at 100+ words `combined = (model + style) / 2`, so
  `|combined − model|` is exactly half of `|style − model|`. A mean shift of
  0.06 means the two signals were only 0.12 apart on average. They agree
  because they measure overlapping things. Across the 36 inputs, `model_score`
  and `style_score` correlate at **r = 0.75**.
- **On the AI pieces:** all 15 use no punctuation beyond full stops and commas,
  which pins the punctuation half of signal two at 1.0. Their sentences are
  even, so the spread half is high too. Signal two just repeats signal one,
  with a mean shift of 0.033.
- **On my writing:** both signals land mid-to-high together, for the reasons
  in criterion 2.

**The count overstates signal two.** Of the 4 changed labels, 3 are my own
pieces that signal one alone would have called "ai" (0.91, 0.81, 0.75). That's
the job signal two is there for. But the 0.91 one is the 53-word
second-language paragraph, and signal two *agreed* with signal one there
(0.86). Their average is 0.885, which is still "ai". What moved it to unsure
was the combining rule's short-text pull, not signal two. So signal two on its
own changed 3 labels. The criterion measures `combined − model`, which counts
the length pull as if it were signal two.

---

## Pattern across the misses

The three misses come down to two problems, not three:

1. **Both signals reward the same thing: even sentences and plain punctuation.**
   That makes them correlated (r = 0.75), so averaging them adds little.
   Criterion 5 misses because signal two rarely disagrees with signal one.
   Criterion 2 misses because when they agree on my academic writing, they
   agree on "fairly AI". The attack run's three false accusations (FP02, FP03,
   FP05) are the same problem with less punctuation to protect them: both
   signals score 0.74–0.97. Signal two's spread scale is the part most worth
   recalibrating, because its human end (0.90) sits where real expository
   prose almost never goes.
2. **The rate limiter runs before validation.** That's criterion 4's one 429,
   and it's why RQ10 and RQ11 never reached the route.

No criterion is broken in the "can't be measured" sense. All three misses
stay misses.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
