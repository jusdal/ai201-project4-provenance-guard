# Run log — after_spaced

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-09 16:11

This is the after run for unit 8, Milestone 5. The one change: the
sentence-length spread's human end moved from 0.90 to 0.60 in
`stylometry.py::style_signal`.

I ran it at 16:11, a minute after the attack run finished. An earlier run at
16:08 (`run_2026-11-09_1608_after.md`) started within a minute of the attack
run's requests with no `creator_id`. Those had filled the per-address limit,
so that run's criterion 4 got extra 429s. Its scores are identical to this one.

Run 1–3 are the three trials. `combined_score` for criteria 2 and 5 was
recomputed with `scoring.py::combine_signals`, and every value matched the
recorded `confidence` and `guess`. Criterion 3 comes from
`results/appeals_2026-11-09_1608_after.md`. Criterion 4's not-JSON case was
sent by hand (`results/not_json_2026-11-09_after.txt`).

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing labelled high-confidence AI | ≤ 1 of 20 | 0/20 | 0/20 | 0/20 | MET |
| 2. Scores spread apart, all three labels reachable | gap ≥ 0.40, and each label ≥ 4 of 36 | gap 0.363 · human 4 / unsure 19 / ai 13 | gap 0.363 · 4 / 19 / 13 | gap 0.363 · 4 / 19 / 13 | MISSED (coverage now passes, gap doesn't) |
| 3. Every appeal changes status and is recorded | 10 of 10, never-issued id → 404 | 10/10 · 404 | 10/10 · 404 | 10/10 · 404 | MET |
| 4. Bad input gets a clean 400, never a crash | 9 of 9 → 400 each trial (27/27) | 9/9 | 9/9 | 8/9 (one 429) | MISSED |
| 5. Signal two actually changes outcomes | ≥ 5 labels changed, and mean \|combined − model\| ≥ 0.10 | 10 · 0.088 | 10 · 0.088 | 10 · 0.088 | MISSED (count now passes, shift doesn't) |

All three trials are identical on every score.

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3514,
    "model_score": 0.9101,
    "style_score": 0.7531,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "I moved here two years ago. At first it was hard. I did not know many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.187,
    "model_score": 0.6905,
    "style_score": 0.4964,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "As you can see from my CV, I have not taken a direct path to the field"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2208,
    "model_score": 0.6663,
    "style_score": 0.5546,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The program is a great fit for me not only because of my interdiscipli"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.4026,
    "model_score": 0.4807,
    "style_score": 0.1166,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "GLOBALIZATION\n\nHistorically, anthropologists have studied places bound"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.303,
    "model_score": 0.5773,
    "style_score": 0.1196,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "LOCALIZING ISLAM IN MAYOTTE\n\nIslamic Prayer Across the Indian Ocean: I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0382,
    "model_score": 0.4778,
    "style_score": 0.484,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs seen in the section on globalism, there was a longstand"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0188,
    "model_score": 0.7015,
    "style_score": 0.3173,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n \nThis paper will first lay out how the audience has been"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3992,
    "model_score": 0.6007,
    "style_score": 0.0,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "3.2: ACTIVE AUDIENCE\n\nIen Ang (1982) provides a textual analysis of le"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2154,
    "model_score": 0.8061,
    "style_score": 0.4092,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Self-Study: A Review of Lectures 1-7\n\nAs a social institution, marriag"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1952,
    "model_score": 0.623,
    "style_score": 0.5721,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "eJournal 5: What Should We Believe?\n\nWag the Dog, released in 1997, is"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.265,
    "model_score": 0.7542,
    "style_score": 0.5109,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Throughout the past century, media has become quite pervasive.  As mor"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3678,
    "model_score": 0.5244,
    "style_score": 0.1078,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "INTRODUCTION\n\nEven with a new transcultural, inter-disciplinary shift "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1502,
    "model_score": 0.6026,
    "style_score": 0.2473,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "DIFFERING PERSPECTIVES\n\nAs referenced above, Edgerton\u2019s findings must "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.136,
    "model_score": 0.4744,
    "style_score": 0.3897,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs evidenced by the review of these two perspectives, a co"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.069,
    "model_score": 0.5174,
    "style_score": 0.5517,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Guest Lecture\nMuslim Traders, Songhay Warriors, and the Arma: \nThe Soc"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.11,
    "model_score": 0.6227,
    "style_score": 0.4873,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Love Marriages in India \n\nMarriage in India has undergone many changes"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3118,
    "model_score": 0.7393,
    "style_score": 0.5725,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Methods of Data Gathering in Ethnographic Research\n\nGathering data is "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0494,
    "model_score": 0.7198,
    "style_score": 0.3295,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "A Summary of Pierre Bourdieu\u2019s \u201cThe Forms of Capital\u201d\n\nIn his 1989 ess"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3342,
    "model_score": 0.8062,
    "style_score": 0.5279,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n\nI have been thinking about which sociocultural phenomena"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.167,
    "model_score": 0.7016,
    "style_score": 0.1314,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "RESEARCH QUESTION\n\nAt the broadest level, I would like to know if inti"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3514,
    "model_score": 0.9101,
    "style_score": 0.7531,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "I moved here two years ago. At first it was hard. I did not know many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.187,
    "model_score": 0.6905,
    "style_score": 0.4964,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "As you can see from my CV, I have not taken a direct path to the field"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2208,
    "model_score": 0.6663,
    "style_score": 0.5546,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The program is a great fit for me not only because of my interdiscipli"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.4026,
    "model_score": 0.4807,
    "style_score": 0.1166,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "GLOBALIZATION\n\nHistorically, anthropologists have studied places bound"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.303,
    "model_score": 0.5773,
    "style_score": 0.1196,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "LOCALIZING ISLAM IN MAYOTTE\n\nIslamic Prayer Across the Indian Ocean: I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0382,
    "model_score": 0.4778,
    "style_score": 0.484,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs seen in the section on globalism, there was a longstand"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0188,
    "model_score": 0.7015,
    "style_score": 0.3173,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n \nThis paper will first lay out how the audience has been"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3992,
    "model_score": 0.6007,
    "style_score": 0.0,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "3.2: ACTIVE AUDIENCE\n\nIen Ang (1982) provides a textual analysis of le"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2154,
    "model_score": 0.8061,
    "style_score": 0.4092,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Self-Study: A Review of Lectures 1-7\n\nAs a social institution, marriag"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1952,
    "model_score": 0.623,
    "style_score": 0.5721,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "eJournal 5: What Should We Believe?\n\nWag the Dog, released in 1997, is"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.265,
    "model_score": 0.7542,
    "style_score": 0.5109,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Throughout the past century, media has become quite pervasive.  As mor"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3678,
    "model_score": 0.5244,
    "style_score": 0.1078,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "INTRODUCTION\n\nEven with a new transcultural, inter-disciplinary shift "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1502,
    "model_score": 0.6026,
    "style_score": 0.2473,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "DIFFERING PERSPECTIVES\n\nAs referenced above, Edgerton\u2019s findings must "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.136,
    "model_score": 0.4744,
    "style_score": 0.3897,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs evidenced by the review of these two perspectives, a co"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.069,
    "model_score": 0.5174,
    "style_score": 0.5517,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Guest Lecture\nMuslim Traders, Songhay Warriors, and the Arma: \nThe Soc"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.11,
    "model_score": 0.6227,
    "style_score": 0.4873,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Love Marriages in India \n\nMarriage in India has undergone many changes"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3118,
    "model_score": 0.7393,
    "style_score": 0.5725,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Methods of Data Gathering in Ethnographic Research\n\nGathering data is "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0494,
    "model_score": 0.7198,
    "style_score": 0.3295,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "A Summary of Pierre Bourdieu\u2019s \u201cThe Forms of Capital\u201d\n\nIn his 1989 ess"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3342,
    "model_score": 0.8062,
    "style_score": 0.5279,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n\nI have been thinking about which sociocultural phenomena"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.167,
    "model_score": 0.7016,
    "style_score": 0.1314,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "RESEARCH QUESTION\n\nAt the broadest level, I would like to know if inti"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3514,
    "model_score": 0.9101,
    "style_score": 0.7531,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "I moved here two years ago. At first it was hard. I did not know many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.187,
    "model_score": 0.6905,
    "style_score": 0.4964,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "As you can see from my CV, I have not taken a direct path to the field"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2208,
    "model_score": 0.6663,
    "style_score": 0.5546,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The program is a great fit for me not only because of my interdiscipli"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.4026,
    "model_score": 0.4807,
    "style_score": 0.1166,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "GLOBALIZATION\n\nHistorically, anthropologists have studied places bound"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.303,
    "model_score": 0.5773,
    "style_score": 0.1196,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "LOCALIZING ISLAM IN MAYOTTE\n\nIslamic Prayer Across the Indian Ocean: I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0382,
    "model_score": 0.4778,
    "style_score": 0.484,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs seen in the section on globalism, there was a longstand"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0188,
    "model_score": 0.7015,
    "style_score": 0.3173,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n \nThis paper will first lay out how the audience has been"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3992,
    "model_score": 0.6007,
    "style_score": 0.0,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "3.2: ACTIVE AUDIENCE\n\nIen Ang (1982) provides a textual analysis of le"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2154,
    "model_score": 0.8061,
    "style_score": 0.4092,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Self-Study: A Review of Lectures 1-7\n\nAs a social institution, marriag"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1952,
    "model_score": 0.623,
    "style_score": 0.5721,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "eJournal 5: What Should We Believe?\n\nWag the Dog, released in 1997, is"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.265,
    "model_score": 0.7542,
    "style_score": 0.5109,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Throughout the past century, media has become quite pervasive.  As mor"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3678,
    "model_score": 0.5244,
    "style_score": 0.1078,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "INTRODUCTION\n\nEven with a new transcultural, inter-disciplinary shift "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1502,
    "model_score": 0.6026,
    "style_score": 0.2473,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "DIFFERING PERSPECTIVES\n\nAs referenced above, Edgerton\u2019s findings must "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.136,
    "model_score": 0.4744,
    "style_score": 0.3897,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs evidenced by the review of these two perspectives, a co"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.069,
    "model_score": 0.5174,
    "style_score": 0.5517,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Guest Lecture\nMuslim Traders, Songhay Warriors, and the Arma: \nThe Soc"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.11,
    "model_score": 0.6227,
    "style_score": 0.4873,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Love Marriages in India \n\nMarriage in India has undergone many changes"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3118,
    "model_score": 0.7393,
    "style_score": 0.5725,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Methods of Data Gathering in Ethnographic Research\n\nGathering data is "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0494,
    "model_score": 0.7198,
    "style_score": 0.3295,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "A Summary of Pierre Bourdieu\u2019s \u201cThe Forms of Capital\u201d\n\nIn his 1989 ess"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3342,
    "model_score": 0.8062,
    "style_score": 0.5279,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n\nI have been thinking about which sociocultural phenomena"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.167,
    "model_score": 0.7016,
    "style_score": 0.1314,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "RESEARCH QUESTION\n\nAt the broadest level, I would like to know if inti"
  }
]
```

### coverage: human

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3514,
    "model_score": 0.9101,
    "style_score": 0.7531,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "I moved here two years ago. At first it was hard. I did not know many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.187,
    "model_score": 0.6905,
    "style_score": 0.4964,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "As you can see from my CV, I have not taken a direct path to the field"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2208,
    "model_score": 0.6663,
    "style_score": 0.5546,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The program is a great fit for me not only because of my interdiscipli"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.4026,
    "model_score": 0.4807,
    "style_score": 0.1166,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "GLOBALIZATION\n\nHistorically, anthropologists have studied places bound"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.303,
    "model_score": 0.5773,
    "style_score": 0.1196,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "LOCALIZING ISLAM IN MAYOTTE\n\nIslamic Prayer Across the Indian Ocean: I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0382,
    "model_score": 0.4778,
    "style_score": 0.484,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs seen in the section on globalism, there was a longstand"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0188,
    "model_score": 0.7015,
    "style_score": 0.3173,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n \nThis paper will first lay out how the audience has been"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3992,
    "model_score": 0.6007,
    "style_score": 0.0,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "3.2: ACTIVE AUDIENCE\n\nIen Ang (1982) provides a textual analysis of le"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2154,
    "model_score": 0.8061,
    "style_score": 0.4092,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Self-Study: A Review of Lectures 1-7\n\nAs a social institution, marriag"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1952,
    "model_score": 0.623,
    "style_score": 0.5721,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "eJournal 5: What Should We Believe?\n\nWag the Dog, released in 1997, is"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.265,
    "model_score": 0.7542,
    "style_score": 0.5109,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Throughout the past century, media has become quite pervasive.  As mor"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3678,
    "model_score": 0.5244,
    "style_score": 0.1078,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "INTRODUCTION\n\nEven with a new transcultural, inter-disciplinary shift "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1502,
    "model_score": 0.6026,
    "style_score": 0.2473,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "DIFFERING PERSPECTIVES\n\nAs referenced above, Edgerton\u2019s findings must "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.136,
    "model_score": 0.4744,
    "style_score": 0.3897,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs evidenced by the review of these two perspectives, a co"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.069,
    "model_score": 0.5174,
    "style_score": 0.5517,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Guest Lecture\nMuslim Traders, Songhay Warriors, and the Arma: \nThe Soc"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3514,
    "model_score": 0.9101,
    "style_score": 0.7531,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "I moved here two years ago. At first it was hard. I did not know many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.187,
    "model_score": 0.6905,
    "style_score": 0.4964,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "As you can see from my CV, I have not taken a direct path to the field"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2208,
    "model_score": 0.6663,
    "style_score": 0.5546,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The program is a great fit for me not only because of my interdiscipli"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.4026,
    "model_score": 0.4807,
    "style_score": 0.1166,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "GLOBALIZATION\n\nHistorically, anthropologists have studied places bound"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.303,
    "model_score": 0.5773,
    "style_score": 0.1196,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "LOCALIZING ISLAM IN MAYOTTE\n\nIslamic Prayer Across the Indian Ocean: I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0382,
    "model_score": 0.4778,
    "style_score": 0.484,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs seen in the section on globalism, there was a longstand"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0188,
    "model_score": 0.7015,
    "style_score": 0.3173,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n \nThis paper will first lay out how the audience has been"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3992,
    "model_score": 0.6007,
    "style_score": 0.0,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "3.2: ACTIVE AUDIENCE\n\nIen Ang (1982) provides a textual analysis of le"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2154,
    "model_score": 0.8061,
    "style_score": 0.4092,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Self-Study: A Review of Lectures 1-7\n\nAs a social institution, marriag"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1952,
    "model_score": 0.623,
    "style_score": 0.5721,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "eJournal 5: What Should We Believe?\n\nWag the Dog, released in 1997, is"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.265,
    "model_score": 0.7542,
    "style_score": 0.5109,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Throughout the past century, media has become quite pervasive.  As mor"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3678,
    "model_score": 0.5244,
    "style_score": 0.1078,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "INTRODUCTION\n\nEven with a new transcultural, inter-disciplinary shift "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1502,
    "model_score": 0.6026,
    "style_score": 0.2473,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "DIFFERING PERSPECTIVES\n\nAs referenced above, Edgerton\u2019s findings must "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.136,
    "model_score": 0.4744,
    "style_score": 0.3897,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs evidenced by the review of these two perspectives, a co"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.069,
    "model_score": 0.5174,
    "style_score": 0.5517,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Guest Lecture\nMuslim Traders, Songhay Warriors, and the Arma: \nThe Soc"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3514,
    "model_score": 0.9101,
    "style_score": 0.7531,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "I moved here two years ago. At first it was hard. I did not know many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.187,
    "model_score": 0.6905,
    "style_score": 0.4964,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "As you can see from my CV, I have not taken a direct path to the field"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2208,
    "model_score": 0.6663,
    "style_score": 0.5546,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The program is a great fit for me not only because of my interdiscipli"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.4026,
    "model_score": 0.4807,
    "style_score": 0.1166,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "GLOBALIZATION\n\nHistorically, anthropologists have studied places bound"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.303,
    "model_score": 0.5773,
    "style_score": 0.1196,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "LOCALIZING ISLAM IN MAYOTTE\n\nIslamic Prayer Across the Indian Ocean: I"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0382,
    "model_score": 0.4778,
    "style_score": 0.484,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs seen in the section on globalism, there was a longstand"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0188,
    "model_score": 0.7015,
    "style_score": 0.3173,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "INTRODUCTION\n \nThis paper will first lay out how the audience has been"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3992,
    "model_score": 0.6007,
    "style_score": 0.0,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "3.2: ACTIVE AUDIENCE\n\nIen Ang (1982) provides a textual analysis of le"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2154,
    "model_score": 0.8061,
    "style_score": 0.4092,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Self-Study: A Review of Lectures 1-7\n\nAs a social institution, marriag"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1952,
    "model_score": 0.623,
    "style_score": 0.5721,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "eJournal 5: What Should We Believe?\n\nWag the Dog, released in 1997, is"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.265,
    "model_score": 0.7542,
    "style_score": 0.5109,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Throughout the past century, media has become quite pervasive.  As mor"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3678,
    "model_score": 0.5244,
    "style_score": 0.1078,
    "label": "This reads like writing by a person. We didn't find the patterns we usually see in text from AI tools.",
    "sent": "INTRODUCTION\n\nEven with a new transcultural, inter-disciplinary shift "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.1502,
    "model_score": 0.6026,
    "style_score": 0.2473,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "DIFFERING PERSPECTIVES\n\nAs referenced above, Edgerton\u2019s findings must "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.136,
    "model_score": 0.4744,
    "style_score": 0.3897,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "CONCLUSION\n\nAs evidenced by the review of these two perspectives, a co"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.069,
    "model_score": 0.5174,
    "style_score": 0.5517,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Guest Lecture\nMuslim Traders, Songhay Warriors, and the Arma: \nThe Soc"
  }
]
```

### coverage: AI

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.7544,
    "style_score": 0.6804,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The importance of effective time management cannot be overstated in to"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.908,
    "model_score": 0.9079,
    "style_score": 1.0,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Regular physical activity offers a wide range of benefits for both phy"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9034,
    "model_score": 0.9442,
    "style_score": 0.9592,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Climate change is one of the most pressing challenges facing the world"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.749,
    "model_score": 0.8337,
    "style_score": 0.9154,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Effective communication is a critical skill in both personal and profe"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7532,
    "model_score": 0.8477,
    "style_score": 0.9056,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Artificial intelligence is transforming industries across the globe. F"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3212,
    "model_score": 0.8039,
    "style_score": 0.5174,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Reading regularly provides numerous cognitive and emotional benefits. "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.728,
    "model_score": 0.8538,
    "style_score": 0.8743,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Remote work has become increasingly common in recent years, offering b"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6818,
    "model_score": 0.8984,
    "style_score": 0.7835,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Sleep plays a vital role in overall health and well-being. During slee"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8146,
    "model_score": 0.8738,
    "style_score": 0.9409,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Financial literacy is an essential life skill that empowers individual"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7698,
    "model_score": 0.833,
    "style_score": 0.9369,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Volunteering is a meaningful way to give back to the community while a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7614,
    "model_score": 0.8824,
    "style_score": 0.879,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Healthy eating is a cornerstone of a balanced lifestyle. A nutritious "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.5896,
    "model_score": 0.8448,
    "style_score": 0.7447,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Social media has fundamentally changed the way people communicate and "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7832,
    "model_score": 0.8438,
    "style_score": 0.9394,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Learning a second language offers a wide range of personal and profess"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.618,
    "model_score": 0.8459,
    "style_score": 0.772,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Public libraries play an important role in supporting communities. The"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8262,
    "model_score": 0.9186,
    "style_score": 0.9076,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Mindfulness is the practice of paying attention to the present moment "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.7544,
    "style_score": 0.6804,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The importance of effective time management cannot be overstated in to"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.908,
    "model_score": 0.9079,
    "style_score": 1.0,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Regular physical activity offers a wide range of benefits for both phy"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9034,
    "model_score": 0.9442,
    "style_score": 0.9592,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Climate change is one of the most pressing challenges facing the world"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.749,
    "model_score": 0.8337,
    "style_score": 0.9154,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Effective communication is a critical skill in both personal and profe"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7532,
    "model_score": 0.8477,
    "style_score": 0.9056,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Artificial intelligence is transforming industries across the globe. F"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3212,
    "model_score": 0.8039,
    "style_score": 0.5174,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Reading regularly provides numerous cognitive and emotional benefits. "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.728,
    "model_score": 0.8538,
    "style_score": 0.8743,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Remote work has become increasingly common in recent years, offering b"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6818,
    "model_score": 0.8984,
    "style_score": 0.7835,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Sleep plays a vital role in overall health and well-being. During slee"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8146,
    "model_score": 0.8738,
    "style_score": 0.9409,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Financial literacy is an essential life skill that empowers individual"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7698,
    "model_score": 0.833,
    "style_score": 0.9369,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Volunteering is a meaningful way to give back to the community while a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7614,
    "model_score": 0.8824,
    "style_score": 0.879,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Healthy eating is a cornerstone of a balanced lifestyle. A nutritious "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.5896,
    "model_score": 0.8448,
    "style_score": 0.7447,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Social media has fundamentally changed the way people communicate and "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7832,
    "model_score": 0.8438,
    "style_score": 0.9394,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Learning a second language offers a wide range of personal and profess"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.618,
    "model_score": 0.8459,
    "style_score": 0.772,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Public libraries play an important role in supporting communities. The"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8262,
    "model_score": 0.9186,
    "style_score": 0.9076,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Mindfulness is the practice of paying attention to the present moment "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4,
    "model_score": 0.7544,
    "style_score": 0.6804,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "The importance of effective time management cannot be overstated in to"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.908,
    "model_score": 0.9079,
    "style_score": 1.0,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Regular physical activity offers a wide range of benefits for both phy"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9034,
    "model_score": 0.9442,
    "style_score": 0.9592,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Climate change is one of the most pressing challenges facing the world"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.749,
    "model_score": 0.8337,
    "style_score": 0.9154,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Effective communication is a critical skill in both personal and profe"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7532,
    "model_score": 0.8477,
    "style_score": 0.9056,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Artificial intelligence is transforming industries across the globe. F"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3212,
    "model_score": 0.8039,
    "style_score": 0.5174,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Reading regularly provides numerous cognitive and emotional benefits. "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.728,
    "model_score": 0.8538,
    "style_score": 0.8743,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Remote work has become increasingly common in recent years, offering b"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6818,
    "model_score": 0.8984,
    "style_score": 0.7835,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Sleep plays a vital role in overall health and well-being. During slee"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8146,
    "model_score": 0.8738,
    "style_score": 0.9409,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Financial literacy is an essential life skill that empowers individual"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7698,
    "model_score": 0.833,
    "style_score": 0.9369,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Volunteering is a meaningful way to give back to the community while a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7614,
    "model_score": 0.8824,
    "style_score": 0.879,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Healthy eating is a cornerstone of a balanced lifestyle. A nutritious "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.5896,
    "model_score": 0.8448,
    "style_score": 0.7447,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Social media has fundamentally changed the way people communicate and "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7832,
    "model_score": 0.8438,
    "style_score": 0.9394,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Learning a second language offers a wide range of personal and profess"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.618,
    "model_score": 0.8459,
    "style_score": 0.772,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Public libraries play an important role in supporting communities. The"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8262,
    "model_score": 0.9186,
    "style_score": 0.9076,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "Mindfulness is the practice of paying attention to the present moment "
  }
]
```

### coverage: borderline

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.027,
    "model_score": 0.5862,
    "style_score": 0.4448,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Effective time management matters more than people think in today's fa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2408,
    "model_score": 0.4293,
    "style_score": 0.8115,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Among the numerous advantages promised by a well constructed Union, no"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2326,
    "model_score": 0.3489,
    "style_score": 0.304,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Time management matters more than people admit, especially now that wo"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0732,
    "model_score": 0.526,
    "style_score": 0.4008,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Exercise is good for you, obviously, but the reasons are more interest"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2358,
    "model_score": 0.4614,
    "style_score": 0.3029,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Remote work has real upsides. No commute, more flexibility, and for a "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0616,
    "model_score": 0.5548,
    "style_score": 0.5087,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Reading every day helps more than I expected. Your vocabulary grows wi"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.027,
    "model_score": 0.5862,
    "style_score": 0.4448,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Effective time management matters more than people think in today's fa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2408,
    "model_score": 0.4293,
    "style_score": 0.8115,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Among the numerous advantages promised by a well constructed Union, no"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2326,
    "model_score": 0.3489,
    "style_score": 0.304,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Time management matters more than people admit, especially now that wo"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0732,
    "model_score": 0.526,
    "style_score": 0.4008,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Exercise is good for you, obviously, but the reasons are more interest"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2358,
    "model_score": 0.4614,
    "style_score": 0.3029,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Remote work has real upsides. No commute, more flexibility, and for a "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0616,
    "model_score": 0.5548,
    "style_score": 0.5087,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Reading every day helps more than I expected. Your vocabulary grows wi"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.027,
    "model_score": 0.5862,
    "style_score": 0.4448,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Effective time management matters more than people think in today's fa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2408,
    "model_score": 0.4293,
    "style_score": 0.8115,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Among the numerous advantages promised by a well constructed Union, no"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2326,
    "model_score": 0.3489,
    "style_score": 0.304,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Time management matters more than people admit, especially now that wo"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0732,
    "model_score": 0.526,
    "style_score": 0.4008,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Exercise is good for you, obviously, but the reasons are more interest"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2358,
    "model_score": 0.4614,
    "style_score": 0.3029,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Remote work has real upsides. No commute, more flexibility, and for a "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0616,
    "model_score": 0.5548,
    "style_score": 0.5087,
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "sent": "Reading every day helps more than I expected. Your vocabulary grows wi"
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"I didn't sleep. Not properly, anyway \\u2014 I lay there listening to the boiler tick and thinking about the th"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "I didn't sleep. Not properly, anyway \u2014 I lay there listening to the bo"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_not_string\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "Hi."
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9976,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"I didn't sleep. Not properly, anyway \\u2014 I lay there listening to the boiler tick and thinking about the th"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "I didn't sleep. Not properly, anyway \u2014 I lay there listening to the bo"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_not_string\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "Hi."
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9976,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"I didn't sleep. Not properly, anyway \\u2014 I lay there listening to the boiler tick and thinking about the th"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t  "
  },
  {
    "status": 429,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "I didn't sleep. Not properly, anyway \u2014 I lay there listening to the bo"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_not_string\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "Hi."
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9976,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "This text has strong patterns we usually see in writing from AI tools. Our check can be wrong, especially on plain or simple writing. If you wrote this yourself, ask for a review and a person will look at it. Nothing changes until they do.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```
