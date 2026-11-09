# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **A writer sends their text.** It goes to `POST /submit` as JSON:
   `{"text": "...", "creator_id": "..."}`.
2. **The route checks it.** `app.py::submit` turns away missing or empty
   `text` or `creator_id`, text over 5,000 characters and text too short to
   score, each with a 400 and an error code, and logs the rejection. Accepted
   text gets a `content_id`.
3. **Signal one reads it.** `detector.py::model_signal` runs a small language
   model (gpt2) locally to measure how predictable the text is. That becomes
   `model_score` (0 = human-like, 1 = AI-like).
4. **Signal two measures its shape.** `stylometry.py::style_signal` scores
   sentence-length variation and punctuation, giving `style_score` (0–1).
5. **The scores are combined.** `scoring.py::combine_signals` averages them
   50/50 and pulls short texts (under 100 words) toward 0.5, giving
   `combined_score`.
6. **The score becomes words.** `scoring.py::score_to_label` maps it to a guess
   (`human` below 0.35, `ai` at 0.75 and up, `unsure` between) and a
   plain-English sentence.
7. **It's logged and returned.** `audit.log_decision` writes all three scores,
   the guess and the label to `logs/audit.jsonl` with status `decided`. The
   writer gets the label, the scores and the `content_id`, which they need to
   appeal: `POST /appeal` logs their reasoning beside the decision and moves
   it to `under_review`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** how predictable the text is to a small language model
(gpt2, run locally), as perplexity, squashed onto 0–1 by
`detector.py::model_signal`. Higher = more AI-like.

**Why that might differ between human and AI writing:** AI writes by picking
likely next words, so its output is easy for a model to predict. People make
odder, more specific choices.

**What it can't see:** predictability isn't authorship. Plain, simple human
writing (second-language writers, younger writers, anyone writing simply on
purpose) looks just as predictable. The plain paragraph from Milestone 1 scored
**0.91**, higher than the clearly-AI sample (0.75). Fancy writing full of rare
words reads as human even when an AI wrote it.

### Signal two — the style signal

**What it measures:** the shape of the text without reading it
(`stylometry.py::style_signal`). Two measures go into the score:

- **Sentence-length spread:** standard deviation of words per sentence divided
  by the mean. 0.20 or less maps to 1.0 (AI); 0.90 or more maps to 0.0 (human).
- **Punctuation density:** dashes, semicolons, colons, brackets, quotes, `!` and
  `?` per 100 words, not counting full stops and commas, which everyone uses.
  0 maps to 1.0 (AI); 4 or more maps to 0.0 (human).

`style_score = 0.6 × spread + 0.4 × punctuation`. Higher = more AI-like.

A third measure, **type-token ratio** (moving average over 50-word windows), is
computed but **left out of the score**. On the calibration inputs it ran
backwards: the AI texts had the *most* varied vocabulary (0.92 and 0.94),
because formal AI prose cycles through synonyms. I didn't flip it to fit five
samples.

**Why that might differ between human and AI writing:** AI tends toward even,
mid-length sentences and plain punctuation. Human writing is lumpier: a
three-word sentence next to a thirty-word one, a dash, a question.

**What it can't see:** it can't read. Anything that changes the shape but not
the substance fools it: chopped-up sentences, an added dash or quotation. It
also calls **even, plainly punctuated human writing** AI-like, so formal human
prose (0.86) and the plain Milestone 1 paragraph (0.86) both score as AI. That
is the same blind spot as signal one, which means that when the two agree on a
plain writer it isn't two independent pieces of evidence.

### The combining rule

**The rule:**

1. Take the weighted average of the two signals.
2. If the text is short, pull that average toward 0.5 ("unsure") in proportion
   to how short it is. From 100 words up there's no pull; at 50 words the
   distance from 0.5 is halved.

When the signals disagree, the average lands in the middle and the label is
"unsure": two methods disagreeing *is* uncertainty.

Why step 2: the plain human paragraph scored more AI-like than real AI text on
**both** signals (model 0.91 vs 0.75, style 0.86 vs 0.82), so no choice of
weights could separate them. Length was the only difference, and short text
is thin evidence that shouldn't get a confident label either way.

**The numbers** (`config.py`):

| Setting | Value |
|---|---|
| `WEIGHT_MODEL_SIGNAL` / `WEIGHT_STYLE_SIGNAL` | 0.5 / 0.5 |
| `FULL_CONFIDENCE_WORDS` | 100 |
| `HUMAN_THRESHOLD` | 0.35 |
| `AI_THRESHOLD` | 0.75 (Milestone 1 said 0.80; at 0.80 the clearly-AI sample could never be labelled AI) |

```
average  = 0.5 × model_score + 0.5 × style_score
strength = min(1, words / 100)
combined = 0.5 + (average − 0.5) × strength
confidence = |combined − 0.5| × 2
```

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**Calibration run** (`samples/calibration.json`, through `POST /submit`):

| Input | Words | model | style | combined |
|---|---|---|---|---|
| clearly AI | 92 | 0.754 | 0.817 | **0.763** |
| clearly human | 94 | 0.445 | 0.000 | **0.239** |
| formal human (Federalist No. 10) | 128 | 0.429 | 0.859 | **0.644** |
| lightly-edited AI | 87 | 0.586 | 0.633 | **0.596** |
| plain human (Milestone 1) | 53 | 0.910 | 0.859 | **0.704** |

**A case where my two signals split, and what my rule does with it:** formal
human writing (Federalist No. 10). Signal one says human (0.43): old, formal
vocabulary is hard for gpt2 to predict. Signal two says AI (0.86): the
sentences are long and even, with almost no dashes or questions. The average
is 0.644, inside the unsure band, so the writer is told the system can't tell
rather than being accused.

**What this rule doesn't fix:** the protection for plain writers comes only from
length. A plain writer who submits 150 words gets no pull toward unsure and
would score about 0.88, which is "AI". The clearly-AI sample also clears the AI
threshold by only 0.013.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
| --- | --- | --- |
| high-confidence human | 0.00 – under 0.35 | This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools. |
| unsure | 0.35 – under 0.75 | We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review. |
| high-confidence AI | 0.75 – 1.00 | This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do. |

The text lives in `scoring.py` (`LABEL_HUMAN`, `LABEL_UNSURE`, `LABEL_AI`);
`scoring.py::score_to_label` picks one. Every score from 0 to 1 maps to exactly
one label. Each was reached through `POST /submit`: clearly human (0.239 →
human), formal human (0.644 → unsure), clearly AI (0.763 → AI).

**Why I worded the "unsure" one this way:**

It says what the system can't do ("we can't tell") instead of what the writer
might have done. It talks about "the work", never "you", because the person
reading it may well have written every word. "Lots of people's own writing
lands here" is true on my calibration set (formal human writing and the plain
second-language paragraph both landed here), and it tells the writer they're
not being singled out. The review is offered, not demanded: unsure is not an
accusation, so it shouldn't read like one.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission** (the clearly-AI sample, labelled AI)

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d @samples/clearly_ai.json
```

```json
{
  "combined_score": 0.763,
  "confidence": 0.526,
  "content_id": "c_09e022f93384",
  "guess": "ai",
  "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
  "model_score": 0.7544,
  "style_score": 0.8173
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_09e022f93384", "reasoning": "I wrote this for a work newsletter. I write formally because that is what my manager asks for."}'
```

```json
{
  "content_id": "c_09e022f93384",
  "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
  "status": "under_review"
}
```

**What the log shows afterwards**

The original decision is still there, unchanged, and the appeal sits right
after it with status `under_review`. Its `creator_id` comes from the original
decision, not from the appeal request.

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.763,
      "content_id": "c_09e022f93384",
      "creator_id": "demo_instructor",
      "guess": "ai",
      "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
      "model_score": 0.7544,
      "status": "decided",
      "style_score": 0.8173,
      "timestamp": "2026-11-02T15:17:20+00:00"
    },
    {
      "content_id": "c_09e022f93384",
      "creator_id": "demo_instructor",
      "event": "appeal",
      "reasoning": "I wrote this for a work newsletter. I write formally because that is what my manager asks for.",
      "status": "under_review",
      "timestamp": "2026-11-02T15:17:20+00:00"
    }
  ]
}
```

**A rejected submission** (text over 5,000 characters)

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "aaaa…5,001 characters…", "creator_id": "u1"}'
```

```json
{
  "error": "text_too_long",
  "message": "Text is over 5,000 characters."
}
```

**An appeal for a content_id that doesn't exist**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_doesnotexist"}'
```

```json
{
  "error": "not_found",
  "message": "No submission with content_id 'c_doesnotexist'."
}
```

---

## How I Used AI

**Moment 1: checking my acceptance criteria**

- _What I asked for:_ I pasted my five criteria into Claude and asked how they
  held up, then asked it to refine them.
- _What came back:_ It found that several contradicted my own Milestone 1
  contract. Criterion 2 used `confidence` where it meant `combined_score`,
  criterion 4 said 50,000 characters where my contract says 5,000, and
  criterion 5 ("modify Signal 2's features by ≥40%") couldn't be checked from
  outside the code. None of them said the target had to hold across all three
  trials.
- _What I changed:_ I kept my original targets (at most 1 of 20, a 0.40 gap,
  10 of 10 appeals, a 0.10 shift) and had the wording fixed to match the
  contract and say exactly what a checker sends and looks at. I asked whether
  to shrink the sample counts to fit the 2 samples the starter ships with, and
  decided to keep them, because 1 of 10 would quietly double my allowed
  false-positive rate.

**Moment 2: choosing the combining rule**

- _What I asked for:_ Help building signal two and a table of both signals
  over the calibration inputs, including the plain second-language paragraph
  from Milestone 1.
- _What came back:_ The plain human paragraph scored *more* AI-like than the
  real AI text on both signals (0.91 vs 0.75, and 0.86 vs 0.82), so no
  weighting could separate them. It also showed type-token ratio running
  backwards. It gave me three rules with their scores: a plain average with AI
  at 0.80 (the plain writer gets labelled AI), the average with AI only at 0.90
  (almost nothing gets labelled AI), or the average pulled toward unsure for
  short texts.
- _What I changed:_ I picked the short-text rule. That meant lowering the AI
  threshold from 0.80 to 0.75 so the clearly-AI sample could still be
  labelled AI. Because that broke the numbers in criteria 2 and 5, I added
  dated revision notes under them instead of editing the originals. I also
  wrote down what the rule doesn't fix: a plain writer who submits 150 words
  still gets no protection.

## Stretch Features

**Declared before building (2026-11-02): `GET /content/<id>`.**

What it will do: return one item's current status, so a writer who appealed
can check where it stands without reading the whole log.

The planned contract:

- `GET /content/<content_id>` → `200` with `content_id`, `status` (from the
  item's latest log entry: `decided` or `under_review`), the original
  `guess`, `label` and the three scores, `submitted_at`, and `appeals`
  (how many have been filed).
- Unknown `content_id` → `404` with `{"error": "not_found", "message": ...}`.
- Read-only: it never writes to the log.

**Built:** `app.py::content`. It reads `audit.entries_for(id)`, takes the
status from the latest entry and the scores and label from the original
decision. Nothing changes until someone asks: the log is still append-only,
and the endpoint only reads it.

**What it changed:** a writer can now see their item move from `decided` to
`under_review` after appealing, which before was only visible in the raw log.

**An item that was appealed** (the Sample Run submission; it shows 2 appeals
because I also tested an appeal with empty reasoning on it):

```bash
$ curl http://127.0.0.1:5000/content/c_09e022f93384
```

```json
{
  "appeals": 2,
  "combined_score": 0.763,
  "content_id": "c_09e022f93384",
  "guess": "ai",
  "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
  "model_score": 0.7544,
  "status": "under_review",
  "style_score": 0.8173,
  "submitted_at": "2026-11-02T15:17:20+00:00"
}
```

**An item nobody appealed:**

```bash
$ curl http://127.0.0.1:5000/content/c_7514b736f6f2
```

```json
{
  "appeals": 0,
  "combined_score": 0.2389,
  "content_id": "c_7514b736f6f2",
  "guess": "human",
  "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
  "model_score": 0.4445,
  "status": "decided",
  "style_score": 0.0,
  "submitted_at": "2026-11-02T15:17:11+00:00"
}
```

**An id that doesn't exist:**

```bash
$ curl http://127.0.0.1:5000/content/c_doesnotexist
```

```json
{
  "error": "not_found",
  "message": "No submission with content_id 'c_doesnotexist'."
}
```

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits their own work a few times an hour at most, so 5 a
minute and 50 a day is far more than a person needs, even someone re-checking
a draft after edits. A script trying to map my thresholds needs hundreds or
thousands of variations. At 5 a minute that takes hours, and the 50-a-day cap
means a thousand variations would take 20 days from one identity.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

Per `creator_id`, taken from the request body (`app.py::rate_limit_key`). If a
request has no usable `creator_id`, it falls back to the caller's IP address.
People sharing one network (a household, a school) don't use up each other's
limit. The weakness: `creator_id` is whatever the caller sends, so a script
that picks a new `creator_id` for every request never hits the limit at all.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

[ 1/15] 200
[ 2/15] 200
[ 3/15] 200
[ 4/15] 200
[ 5/15] 200
[ 6/15] 429
[ 7/15] 429
[ 8/15] 429
[ 9/15] 429
[10/15] 429
[11/15] 429
[12/15] 429
[13/15] 429
[14/15] 429
[15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================
```

---

## Attack Run — Before

`python run_attacks.py --set attack_set` against the service as of commit
`a3402b3`, 56 attacks on 2026-11-09. Full report:
[results/attack_run_2026-11-09_1503.md](results/attack_run_2026-11-09_1503.md).
The audit log for just this run is in
[results/audit_run_2026-11-09_1503.jsonl](results/audit_run_2026-11-09_1503.jsonl).

**42 held, 14 broke.** Nothing crashed and nothing returned a 5xx.

| Family | Held | Broke |
|---|---|---|
| `evasion` | 3 | 7 |
| `false_positive` | 5 | 3 |
| `prompt_injection` | 6 | 0 |
| `malformed` | 16 | 4 |
| `flood_same_creator` | 12 | 0 |

How I called it:
- **Evasion** broke if AI text didn't get the `ai` label. The unsure label
  tells the writer it "isn't a finding against the work", so AI text that lands
  there has got through. EV08 is the exception: at 10 words nobody can judge
  the text, and unsure is the right answer.
- **False positive** broke if human writing got the `ai` label.
- **Malformed** broke if the service accepted something that isn't writing
  and gave it a content_id and a label, instead of rejecting it.

The Score column is the `confidence` field (`|combined − 0.5| × 2`), not the
combined score. The verdict notes quote the combined score from the audit log,
because that's the number the thresholds (0.35 / 0.75) apply to.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_47530b6798f1` | unsure | 0.139 | BROKE: AI text, 0.570 → unsure. Typos dropped signal one to 0.16; signal two still said AI (1.0) |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_16cdb1ddf1ce` | unsure | 0.266 | BROKE: AI text, 0.367 → unsure, 0.017 from a human label. Signal two fell to 0.11 |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_564718936c3e` | unsure | 0.080 | BROKE: AI text, 0.540 → unsure |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_6c994776286d` | ai | 0.526 | HELD: 0.763 → ai. Rare words didn't move signal one enough |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_68884394d97a` | unsure | 0.171 | BROKE: AI text, 0.415 → unsure after a human edit pass |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_0ea037bca2a1` | unsure | 0.025 | BROKE: AI text, 0.487 → unsure |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_1c111758e216` | unsure | 0.181 | BROKE: AI text, 0.590 → unsure |
| EV08 | evasion | signal one: text below the token window | 200 | `c_293e6aa0573a` | unsure | 0.017 | HELD: 10 words: signal one fooled (0.25) but length pull held it at 0.509 unsure, not human |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_aa50d2005855` | unsure | 0.475 | BROKE: AI text, 0.7375 → unsure, 0.0125 under the AI line |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_4dcec9230ccd` | ai | 0.634 | HELD: 0.817 → ai |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_95aa5b90bf30` | unsure | 0.397 | HELD: Human, 0.698 → unsure (not accused, but nowhere near a human label) |
| FP02 | false_positive | human writing in a formal register | 200 | `c_7d3172539035` | ai | 0.535 | BROKE: Human writing, 0.768 → **ai** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_9766f30b52b7` | ai | 0.577 | BROKE: Human writing, 0.789 → **ai**. Worst outcome |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_09fa8188db4d` | unsure | 0.469 | HELD: Human, 0.735 → unsure, 0.015 under the AI line |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_b4aefc952f37` | ai | 0.514 | BROKE: Human writing, 0.757 → **ai** |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_0a14f355d5ea` | unsure | 0.389 | HELD: Human, 0.695 → unsure |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_3373be81f0a5` | unsure | 0.252 | HELD: Human, 0.626 → unsure |
| FP08 | false_positive | very short genuine human submission | 200 | `c_36dbc77f581e` | unsure | 0.010 | HELD: 8 words, 0.505 → unsure via length pull |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_f621695f40d7` | unsure | 0.030 | HELD: 0.515 → unsure, not the human label it asked for. Text never read as instructions |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_d470186b350a` | unsure | 0.182 | HELD: 0.409 → unsure. Fake SYSTEM line ignored |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_0bfa0822154a` | unsure | 0.039 | HELD: 0.520 → unsure |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_182b58defd31` | unsure | 0.031 | HELD: Label is fixed text and submitted text isn't echoed or logged, so the script tag goes nowhere |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_5fba0f9fc8fc` | unsure | 0.002 | HELD: Submitted text isn't written to the log, and entries are json.dumps'd, so no forged fields |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_1a071e232619` | unsure | 0.348 | HELD: 0.674 → unsure. Instruction had no effect (human text still not labeled human) |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD: 400 bad_text |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD: 400 too_short |
| MF03 | malformed | text is control characters | 200 | `c_1b17882c300d` | unsure | 0.000 | BROKE: Accepted ANSI control codes as writing: 200, content_id, a label |
| MF04 | malformed | text is only punctuation | 200 | `c_c3696b575b4c` | unsure | 0.000 | BROKE: Accepted punctuation-only as writing: 200, content_id, a label |
| MF05 | malformed | text is a very long single word | 200 | `c_0be906517fb6` | unsure | 0.010 | BROKE: Accepted one 300-char 'word': signal one 0.998, saved only by the length pull |
| MF06 | malformed | text is emoji only | 200 | `c_0a7fcab0b729` | unsure | 0.000 | BROKE: Accepted emoji-only: signal one 0.997, style 1.0, saved only by the length pull |
| MF07 | malformed | text is right-to-left script | 200 | `c_26971d2bc962` | unsure | 0.000 | HELD: 0.5 unsure, no crash. But signal one 0.906 on Arabic: a longer non-English text would be labeled ai |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD: 400 too_long |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD: 400 bad_creator_id |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD: 400 bad_creator_id |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD: 400 bad_text |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD: 429. No creator_id, so it shared the IP bucket with RQ02/06–09 and never reached the route |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD: 429. Same as RQ10: the route's handling of a text/plain body is untested |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD: 400 bad_text |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_7cde48fd4a57` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_9ff0370eac76` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_b8e5edb3366c` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_bc47ac4bdf20` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_4cc2fbf12aab` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |

**Audit log entries from the run** (12 of them: three false accusations, three
evasions, two junk inputs that signal one scored as near-certain AI, the log
injection attempt, and three rejections, two of them 429s)

```json
{"timestamp": "2026-11-09T08:03:13+00:00", "content_id": "c_9766f30b52b7", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.8901, "combined_score": 0.7885, "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:13+00:00", "content_id": "c_7d3172539035", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.9655, "combined_score": 0.7676, "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:13+00:00", "content_id": "c_b4aefc952f37", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.9341, "combined_score": 0.7571, "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:12+00:00", "content_id": "c_16cdb1ddf1ce", "creator_id": "attacker_EV02", "guess": "unsure", "model_score": 0.5943, "style_score": 0.1139, "combined_score": 0.3672, "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:13+00:00", "content_id": "c_aa50d2005855", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.7707, "combined_score": 0.7375, "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:12+00:00", "content_id": "c_47530b6798f1", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 1.0, "combined_score": 0.5695, "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:14+00:00", "content_id": "c_0a7fcab0b729", "creator_id": "attacker_MF06", "guess": "unsure", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.5, "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:14+00:00", "content_id": "c_26971d2bc962", "creator_id": "attacker_MF07", "guess": "unsure", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.5, "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:13+00:00", "content_id": "c_5fba0f9fc8fc", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.3674, "combined_score": 0.5011, "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-09T08:03:14+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "bad_creator_id", "text_length": 55}
{"timestamp": "2026-11-09T08:03:14+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-09T08:03:14+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

What these show:
- **FP03, FP02, FP05** are three human writers labeled `ai`. All three are
  plain, regular, careful writing, and both signals rate them as AI-like
  (model 0.74–0.81, style 0.89–0.97).
- **EV02** is AI text at 0.367, 0.017 from a human label. Signal two dropped to
  0.11 after the sentences were broken up with "Really."
- **EV09** is AI text at 0.7375, 0.0125 under the AI line.
- **EV01** targeted signal two with typos. Signal two didn't move (1.0); it was
  signal one that dropped (0.16). The attack worked, just not through the
  signal it was aimed at.
- **MF06 (emoji) and MF07 (Arabic)** got a signal one score of 0.997 and 0.906.
  Only the short-text pull toward 0.5 kept them at unsure. A longer Arabic
  text would be labeled AI.
- **PI05** tried to forge `"guess": "human"` into the log. It held because the
  submitted text is never written to the log.
- **The `unknown` 400 and 429** show that requests with no usable creator_id
  share one bucket per IP. RQ10 and RQ11 were 429'd before the route ever saw
  them, so how the route handles form-encoded and text/plain bodies is still
  untested.
- **The `attacker_flood` 429** is FL01_06, the 6th of 12 rapid submissions
  under one creator. 1–5 got 200, 6–12 got 429.

**The single worst outcome**, the one I'd least want to explain to a writer
whose work got caught by it:

**FP03, a non-native English speaker writing carefully, labeled AI at 0.7885.**
This is the highest score any human text got in the run:

> I want to describe my experience of the first month in this country. The
> weather was very different from my home. I did not expect the rain to
> continue for so many days. My colleagues were kind and they helped me to find
> an apartment. I am still learning the words that people use in the office.
> Sometimes I do not understand the jokes. But I am happy that I came here and I
> think it was a good decision for my family.

The service returned `guess: "ai"`, model 0.8051, style 0.8901, and the label
"This text has strong patterns we usually see in writing from AI tools." The
person most likely to get this label is someone writing in a second language
and choosing simple, safe sentences on purpose. That's exactly the writer least
able to argue with it.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
