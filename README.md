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

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

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
