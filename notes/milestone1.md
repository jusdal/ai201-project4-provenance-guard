# Milestone 1 notes — the false positive and the endpoint contract

Each decision has a one-line reason. Thresholds are provisional until
Milestone 4, when the style signal exists and can be measured.

---

## 3. Trace the false positive

### Who

A real writer, writing in their second language. Short sentences, words they're
sure of, nothing fancy. Every word is theirs.

> I moved here two years ago. At first it was hard. I did not know many people
> and my English was not good. Now I have a job and some friends. I like the
> city. The winter is cold but the summer is nice. I want to stay here for a
> long time.

### What happens to them, step by step (with the starter defaults)

| Step | What the service does | What they get |
|---|---|---|
| Route | Text is non-empty and long enough → accepted, `content_id` assigned | — |
| Signal one | gpt2 finds plain, common words easy to predict | perplexity **10.6** → `model_score` **0.91** (measured, `python detector.py`) |
| Signal two | Sentences are all short and similar; words repeat ("I", "the", "is") | probably **high** too (stylometry isn't built yet — check in Milestone 4) |
| Combine | Default rule is 50/50 average | roughly **0.8+** |
| Label | Default thresholds: ≥ 0.65 is AI | **"high-confidence AI"** |
| Log | `status: decided` with both scores | — |

**The key point:** both signals share the same blind spot here. Plain writing
looks predictable to signal one *and* even/uniform to signal two. So when they
agree on this writer, it's not two independent pieces of evidence. It's the
same mistake counted twice.

### What the label says to them

With the defaults, they'd be told their own work was probably written by AI.
Whatever the final wording (Milestone 5), every label must:

- describe the **text**, never the **person** ("this text has patterns…", not
  "you used AI");
- tell them they can appeal, and how.

### What they can do about it

- `POST /appeal` with their `content_id` and (optionally) their reasoning.
- That moves the item to `under_review` and logs the appeal next to the
  original decision (nothing is overwritten).
- Nothing gets re-checked automatically. A person has to look at it.

### Decisions this forces

- **AI threshold: 0.80** (was 0.65). The default is clearable on signal one
  alone by a plain human writer. Accusing a real person costs far more than
  missing some AI text, so "AI" needs a high score.
- **Human threshold: 0.35** (unchanged). Being wrongly told "human" costs little.
- **So "unsure" covers 0.35–0.80.** Wide on purpose: borderline writers land
  here instead of in "AI".
- **Provisional.** In Milestone 4, run this exact paragraph through `/submit`.
  If it still lands in "AI", raise the threshold or change the combining rule
  so one signal alone can't push a text into "AI".
- **Test case to keep:** this paragraph goes into my calibration inputs and
  `criteria.md` as the plain-human example.

---

## 4. The endpoint shapes

All error responses share one shape:
`{"error": "<code>", "message": "<sentence a person can read>"}`.
All input problems are `400`; the `error` code says which problem.
*Why:* one status for "your input is wrong" keeps clients simple; the code is
what they branch on.

### `POST /submit`

**Request (JSON object)**

| Field | Type | Required | Rules |
|---|---|---|---|
| `text` | string | yes | Non-empty after trimming. Long enough for the model to score (a few sentences). **Max 5,000 characters.** |
| `creator_id` | string | **yes** | Non-empty after trimming. |

*Why 5,000:* the model only reads the first 400 tokens (~1,600 characters), so
longer text isn't judged on its whole length anyway. 5,000 fits a long essay
excerpt and stops someone sending megabytes.

*Why `creator_id` is required:* unit 8's rate limit counts per `creator_id`, and
an appeal needs to know whose work it was. Lumping everyone under `"unknown"`
breaks both. (All the unit 8 scripts already send one.)

**Success: `200`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | e.g. `"c_66f299df9c6d"`. Needed to appeal |
| `guess` | string | `"human"`, `"unsure"` or `"ai"` |
| `confidence` | float 0–1 | How far the combined score is from a coin flip: `abs(combined_score - 0.5) * 2`. 0 = no idea, 1 = as sure as the system gets |
| `label` | string | The plain-English sentence the writer reads |
| `model_score` | float 0–1 | Signal one. Higher = more AI-like |
| `style_score` | float 0–1 | Signal two. Higher = more AI-like |
| `combined_score` | float 0–1 | The number the label was picked from |

*Why that `confidence`:* it means the same thing for every guess. A raw score of
0.2 is a *confident* human guess; reporting 0.2 as "confidence" would read as
the opposite.

**Errors**

| Case | Status | `error` | Logged as rejection? |
|---|---|---|---|
| Body isn't a JSON object, or `text` missing / empty / not a string | 400 | `bad_request` | yes, `reason: "bad_text"` |
| `creator_id` missing / empty / not a string | 400 | `bad_request` | yes, `reason: "bad_creator_id"` |
| `text` too short to score | 400 | `text_too_short` | yes, `reason: "too_short"` |
| `text` over 5,000 characters | 400 | `text_too_long` | yes, `reason: "too_long"` |
| Model can't load | 503 | `detector_unavailable` | yes, `reason: "detector_unavailable"` |
| Too many requests (unit 8) | 429 | `rate_limited` | yes (already built) |

*Why log rejections:* unit 8 says it directly — an attack that only shows up
as an absence is one you'll never find. Log the length of the text, never the
text itself, for rejected inputs.

### `POST /appeal`

**Request (JSON object)**

| Field | Type | Required | Rules |
|---|---|---|---|
| `content_id` | string | yes | Must match a decision in the log (`audit.entries_for(id)`) |
| `reasoning` | string | **no** | Defaults to `""`. Max 2,000 characters |

*Why optional reasoning:* the person appealing may be the writer least able to
argue in polished English. The appeal is what matters; an empty one still gets
recorded and reviewed.

**Success: `200`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | Echoed back |
| `status` | string | `"under_review"` |
| `message` | string | "Thanks. A person will review this decision. Nothing about your submission changes until they do." |

**Appealing again:** also `200`, and the new appeal is logged too.
*Why:* never turn an appeal away; a second one may add information, and the
log is append-only so nothing is lost.

**Who appealed:** the log entry's `creator_id` comes from the **original
decision**, not the request. *Why:* the request can claim anything; the log
already knows whose submission it was.

**Errors**

| Case | Status | `error` |
|---|---|---|
| Body isn't a JSON object, or `content_id` missing / not a string | 400 | `bad_request` |
| `reasoning` not a string, or over 2,000 characters | 400 | `bad_request` |
| `content_id` not in the log | 404 | `not_found` |

### Read-back check

Could someone build against this without asking me a question? Every field has
a type and a rule, every bad input has a status and a code, and the one open
item (exact thresholds) is pinned to a test I'll run in Milestone 4.

### What changes in code because of this

- `app.py::submit`: require `creator_id`; add the 5,000-character limit; split
  out `text_too_short`; catch `DetectorUnavailable` → 503; log every rejection.
- `config.py`: `AI_THRESHOLD = 0.80` (Milestone 4, after measuring).
- `app.py::appeal`: build it to this contract (Milestone 5).
