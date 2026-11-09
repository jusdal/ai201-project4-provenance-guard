# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 16:08
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_91441d67b605` | unsure | 0.139 | BROKE: AI text, 0.5695 → unsure |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_a5078817c95d` | human | 0.305 | BROKE: AI text, 0.3474 → **human** (was unsure before) |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_53fee202273c` | unsure | 0.076 | BROKE: AI text, 0.4618 → unsure |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_3242d741d1bc` | ai | 0.526 | HELD: 0.7629 → ai |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_847c636d8a66` | human | 0.329 | BROKE: AI text, 0.3357 → **human** (was unsure before) |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_94beb7a891a2` | unsure | 0.025 | BROKE: AI text, 0.4874 → unsure |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_5c6a4741e5bb` | unsure | 0.181 | BROKE: AI text, 0.5903 → unsure |
| EV08 | evasion | signal one: text below the token window | 200 | `c_0d511464696e` | unsure | 0.012 | HELD: 10 words, 0.506 → unsure via length pull |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_bf70501ab174` | unsure | 0.303 | BROKE: AI text, 0.6515 → unsure |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_abe7a7f9527e` | ai | 0.537 | HELD: 0.7685 → ai |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_14f5a3ecd9da` | unsure | 0.231 | HELD: Human, 0.6157 → unsure |
| FP02 | false_positive | human writing in a formal register | 200 | `c_46b30f0cd7da` | ai | 0.515 | BROKE: Human writing, 0.7577 → **ai** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_aa38c380c834` | ai | 0.509 | BROKE: Human writing, 0.7543 → **ai** |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_cc73b9a5feeb` | unsure | 0.396 | HELD: Human, 0.6982 → unsure |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_1979885a5f8b` | unsure | 0.480 | HELD: Human, 0.7398 → unsure (was ai before) |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_4176c3903c04` | unsure | 0.258 | HELD: Human, 0.6288 → unsure |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_ba29f54ed929` | unsure | 0.166 | HELD: Human, 0.5831 → unsure |
| FP08 | false_positive | very short genuine human submission | 200 | `c_d4a98cb61081` | unsure | 0.002 | HELD: Human, 0.4989 → unsure |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_a9a30d2772c5` | unsure | 0.062 | HELD: 0.4691 → unsure, not the human label it asked for. Text never read as instructions |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_ad9813fac006` | unsure | 0.278 | HELD: 0.361 → unsure. Fake SYSTEM line ignored |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_de787b8190b4` | unsure | 0.011 | HELD: 0.4944 → unsure |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_5bdf11e972ea` | unsure | 0.096 | HELD: Label is fixed text and submitted text isn't echoed or logged, so the script tag goes nowhere |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_94291ef64242` | unsure | 0.050 | HELD: Submitted text isn't written to the log, and entries are json.dumps'd, so no forged fields |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_4cf124c03ce1` | unsure | 0.190 | HELD: 0.5951 → unsure. Instruction had no effect (human text still not labeled human) |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD: 400 bad_text |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD: 400 too_short |
| MF03 | malformed | text is control characters | 200 | `c_f4761df56f38` | unsure | 0.000 | BROKE: Accepted ANSI control codes as writing: 200, content_id, a label |
| MF04 | malformed | text is only punctuation | 200 | `c_0766ba29887c` | unsure | 0.000 | BROKE: Accepted punctuation-only as writing: 200, content_id, a label |
| MF05 | malformed | text is a very long single word | 200 | `c_a6eac29a253a` | unsure | 0.010 | BROKE: Accepted one 300-char 'word': signal one 0.998, saved only by the length pull |
| MF06 | malformed | text is emoji only | 200 | `c_bcc8879c1277` | unsure | 0.000 | BROKE: Accepted emoji-only: signal one 0.997, style 1.0, saved only by the length pull |
| MF07 | malformed | text is right-to-left script | 200 | `c_c6458a060892` | unsure | 0.000 | HELD: 0.5 unsure, no crash. But signal one 0.906 on Arabic: a longer non-English text would be labeled ai |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_a435fc6964a4` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_6742682911b5` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_fba0b9bff06c` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_de7b6565ed65` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_76464b523c71` | unsure | 0.003 | HELD: 200, within 5/min |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD: 429 rate_limited |

---

## Verdict tally

After one change, the sentence-length spread's human end moving from 0.90
to 0.60 in `stylometry.py::style_signal`.

| Family | Held | Broke | Before (held / broke) |
|---|---|---|---|
| `evasion` | 3 | 7 | 3 / 7 |
| `false_positive` | 6 | 2 | 5 / 3 |
| `prompt_injection` | 6 | 0 | 6 / 0 |
| `malformed` | 16 | 4 | 16 / 4 |
| `flood_same_creator` | 12 | 0 | 12 / 0 |
| **Total** | **43** | **13** | 42 / 14 |

Same rules as the before run. An **evasion** broke if AI text didn't get the
`ai` label, except EV08, where 10 words is too short to judge. A
**false_positive** broke if human text got the `ai` label. A **malformed**
input broke if the service accepted non-writing as a scored submission.

Three rows changed: FP05 went `ai` → unsure, so it now holds. EV02 and EV05
went unsure → **human**. They were already counted as broken, but they now
break with a confident wrong label.

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_91441d67b605",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.139,
  "model_score": 0.1635,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_a5078817c95d",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3052,
  "model_score": 0.5943,
  "style_score": 0.0703,
  "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_53fee202273c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0764,
  "model_score": 0.6662,
  "style_score": 0.2575,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_3242d741d1bc",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.5258,
  "model_score": 0.6114,
  "style_score": 1.0,
  "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_847c636d8a66",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3286,
  "model_score": 0.3212,
  "style_score": 0.2781,
  "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_94beb7a891a2",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0252,
  "model_score": 0.5727,
  "style_score": 0.4,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_5c6a4741e5bb",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.1806,
  "model_score": 0.5862,
  "style_score": 0.6,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_0d511464696e",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.012,
  "model_score": 0.2452,
  "style_score": 0.8758,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_bf70501ab174",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.303,
  "model_score": 0.7042,
  "style_score": 0.5987,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_abe7a7f9527e",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.537,
  "model_score": 0.9792,
  "style_score": 0.7092,
  "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_14f5a3ecd9da",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.2314,
  "model_score": 0.6175,
  "style_score": 0.6138,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_46b30f0cd7da",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.5154,
  "model_score": 0.7387,
  "style_score": 0.9395,
  "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_aa38c380c834",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.5086,
  "model_score": 0.8051,
  "style_score": 0.8077,
  "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_cc73b9a5feeb",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.3964,
  "model_score": 0.8329,
  "style_score": 0.7499,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_1979885a5f8b",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.4796,
  "model_score": 0.8005,
  "style_score": 0.8847,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_4176c3903c04",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.2576,
  "model_score": 0.8814,
  "style_score": 0.5212,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_ba29f54ed929",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.1662,
  "model_score": 0.8816,
  "style_score": 0.4,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_d4a98cb61081",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.0022,
  "model_score": 0.3223,
  "style_score": 0.6505,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_a9a30d2772c5",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0618,
  "model_score": 0.4625,
  "style_score": 0.4,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_ad9813fac006",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.278,
  "model_score": 0.2044,
  "style_score": 0.1778,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_de787b8190b4",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0112,
  "model_score": 0.5943,
  "style_score": 0.3853,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_5bdf11e972ea",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0956,
  "model_score": 0.4998,
  "style_score": 0.3128,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_94291ef64242",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0502,
  "model_score": 0.6401,
  "style_score": 0.1929,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_4cf124c03ce1",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1902,
  "model_score": 0.5583,
  "style_score": 0.6319,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_f4761df56f38",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c_0766ba29887c",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_a6eac29a253a",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.01,
  "model_score": 0.9976,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_bcc8879c1277",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_c6458a060892",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_a435fc6964a4",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0026,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_6742682911b5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0026,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_fba0b9bff06c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0026,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_de7b6565ed65",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0026,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_76464b523c71",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0026,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
