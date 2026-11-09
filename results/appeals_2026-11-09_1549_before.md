# Appeal run — criterion 3 — before

- Produced by: `run_appeals.py::main`
- Service: `app.py::appeal` · log: `audit.py::log_appeal`, `GET /log`
- 3 trials · 2026-11-09 15:49

| Trial | Appeals passing all checks | Never-issued id → 404 |
|---|---|---|
| 1 | 10/10 | yes (404) |
| 2 | 10/10 | yes (404) |
| 3 | 10/10 | yes (404) |

## Trial 1

### Per-appeal checks

```json
[
  {
    "content_id": "c_5a6be5d45337",
    "reasoning_sent": "I wrote this myself for a graduate seminar. I can share my drafts.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_6664ab351e6b",
    "reasoning_sent": "This is my own coursework. Formal academic writing is just how I write.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_92f56928f143",
    "reasoning_sent": "I wrote every word of this. Please have a person look at it.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_8287bd42b909",
    "reasoning_sent": "My own essay from my master's program, written before AI tools existed.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_f46464ca5941",
    "reasoning_sent": "I'm the author. I have the original file with its edit history.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_95ca59bfddcd",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_9f59bc1ff9a0",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_187aa0d71330",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_c8acdb812ec2",
    "reasoning_sent": "(field left out)",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_fb5fc637b908",
    "reasoning_sent": "(field left out)",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  }
]
```

### What actually came back

```json
{
  "submit_response": {
    "combined_score": 0.7038,
    "confidence": 0.4076,
    "content_id": "c_5a6be5d45337",
    "guess": "unsure",
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "model_score": 0.9101,
    "style_score": 0.8589
  },
  "appeal_response_with_reasoning": {
    "content_id": "c_5a6be5d45337",
    "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
    "status": "under_review"
  },
  "appeal_response_reasoning_left_out": {
    "content_id": "c_fb5fc637b908",
    "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
    "status": "under_review"
  },
  "log_entries_for_one_content_id": [
    {
      "combined_score": 0.7038,
      "content_id": "c_5a6be5d45337",
      "creator_id": "eval_appeal_154915_t1_1",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
      "model_score": 0.9101,
      "status": "decided",
      "style_score": 0.8589,
      "timestamp": "2026-11-09T08:49:15+00:00"
    },
    {
      "content_id": "c_5a6be5d45337",
      "creator_id": "eval_appeal_154915_t1_1",
      "event": "appeal",
      "reasoning": "I wrote this myself for a graduate seminar. I can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-09T08:49:16+00:00"
    }
  ],
  "log_entries_for_left_out_reasoning": [
    {
      "combined_score": 0.6547,
      "content_id": "c_fb5fc637b908",
      "creator_id": "eval_appeal_154915_t1_10",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
      "model_score": 0.623,
      "status": "decided",
      "style_score": 0.6865,
      "timestamp": "2026-11-09T08:49:16+00:00"
    },
    {
      "content_id": "c_fb5fc637b908",
      "creator_id": "eval_appeal_154915_t1_10",
      "event": "appeal",
      "reasoning": "",
      "status": "under_review",
      "timestamp": "2026-11-09T08:49:16+00:00"
    }
  ],
  "never_issued_appeal": {
    "status": 404,
    "body": {
      "error": "not_found",
      "message": "No submission with content_id 'c_never_issued_154915_1'."
    },
    "pass": true
  }
}
```

## Trial 2

### Per-appeal checks

```json
[
  {
    "content_id": "c_549c51c4026c",
    "reasoning_sent": "I wrote this myself for a graduate seminar. I can share my drafts.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_0b780f568108",
    "reasoning_sent": "This is my own coursework. Formal academic writing is just how I write.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_2cecefa50532",
    "reasoning_sent": "I wrote every word of this. Please have a person look at it.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_12e656fc1d25",
    "reasoning_sent": "My own essay from my master's program, written before AI tools existed.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_9e662cd92b5f",
    "reasoning_sent": "I'm the author. I have the original file with its edit history.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_96341cdb1ef8",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_6268742f283b",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_02287aff5c82",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_01fc0d49c348",
    "reasoning_sent": "(field left out)",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_82d234672f89",
    "reasoning_sent": "(field left out)",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  }
]
```

### What actually came back

```json
{
  "submit_response": {
    "combined_score": 0.7038,
    "confidence": 0.4076,
    "content_id": "c_549c51c4026c",
    "guess": "unsure",
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "model_score": 0.9101,
    "style_score": 0.8589
  },
  "appeal_response_with_reasoning": {
    "content_id": "c_549c51c4026c",
    "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
    "status": "under_review"
  },
  "appeal_response_reasoning_left_out": {
    "content_id": "c_82d234672f89",
    "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
    "status": "under_review"
  },
  "log_entries_for_one_content_id": [
    {
      "combined_score": 0.7038,
      "content_id": "c_549c51c4026c",
      "creator_id": "eval_appeal_154915_t2_1",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
      "model_score": 0.9101,
      "status": "decided",
      "style_score": 0.8589,
      "timestamp": "2026-11-09T08:49:16+00:00"
    },
    {
      "content_id": "c_549c51c4026c",
      "creator_id": "eval_appeal_154915_t2_1",
      "event": "appeal",
      "reasoning": "I wrote this myself for a graduate seminar. I can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-09T08:49:17+00:00"
    }
  ],
  "log_entries_for_left_out_reasoning": [
    {
      "combined_score": 0.6547,
      "content_id": "c_82d234672f89",
      "creator_id": "eval_appeal_154915_t2_10",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
      "model_score": 0.623,
      "status": "decided",
      "style_score": 0.6865,
      "timestamp": "2026-11-09T08:49:17+00:00"
    },
    {
      "content_id": "c_82d234672f89",
      "creator_id": "eval_appeal_154915_t2_10",
      "event": "appeal",
      "reasoning": "",
      "status": "under_review",
      "timestamp": "2026-11-09T08:49:17+00:00"
    }
  ],
  "never_issued_appeal": {
    "status": 404,
    "body": {
      "error": "not_found",
      "message": "No submission with content_id 'c_never_issued_154915_2'."
    },
    "pass": true
  }
}
```

## Trial 3

### Per-appeal checks

```json
[
  {
    "content_id": "c_c7f5e6c22deb",
    "reasoning_sent": "I wrote this myself for a graduate seminar. I can share my drafts.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_c1b482776880",
    "reasoning_sent": "This is my own coursework. Formal academic writing is just how I write.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_8c38e1aeafbe",
    "reasoning_sent": "I wrote every word of this. Please have a person look at it.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_789170adde08",
    "reasoning_sent": "My own essay from my master's program, written before AI tools existed.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_b4aadcdde7b7",
    "reasoning_sent": "I'm the author. I have the original file with its edit history.",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_8c688ef6cc88",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_ab12c312af91",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_81a2bc866df9",
    "reasoning_sent": "",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_682fe7ba1f63",
    "reasoning_sent": "(field left out)",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  },
  {
    "content_id": "c_28da00cfe9ab",
    "reasoning_sent": "(field left out)",
    "response_200": true,
    "status_under_review": true,
    "same_content_id": true,
    "appeal_logged_with_exact_reasoning": true,
    "decision_unchanged": true
  }
]
```

### What actually came back

```json
{
  "submit_response": {
    "combined_score": 0.7038,
    "confidence": 0.4076,
    "content_id": "c_c7f5e6c22deb",
    "guess": "unsure",
    "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
    "model_score": 0.9101,
    "style_score": 0.8589
  },
  "appeal_response_with_reasoning": {
    "content_id": "c_c7f5e6c22deb",
    "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
    "status": "under_review"
  },
  "appeal_response_reasoning_left_out": {
    "content_id": "c_28da00cfe9ab",
    "message": "Thanks. A person will review this decision. Nothing about your submission changes until they do.",
    "status": "under_review"
  },
  "log_entries_for_one_content_id": [
    {
      "combined_score": 0.7038,
      "content_id": "c_c7f5e6c22deb",
      "creator_id": "eval_appeal_154915_t3_1",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
      "model_score": 0.9101,
      "status": "decided",
      "style_score": 0.8589,
      "timestamp": "2026-11-09T08:49:17+00:00"
    },
    {
      "content_id": "c_c7f5e6c22deb",
      "creator_id": "eval_appeal_154915_t3_1",
      "event": "appeal",
      "reasoning": "I wrote this myself for a graduate seminar. I can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-09T08:49:19+00:00"
    }
  ],
  "log_entries_for_left_out_reasoning": [
    {
      "combined_score": 0.6547,
      "content_id": "c_28da00cfe9ab",
      "creator_id": "eval_appeal_154915_t3_10",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with an AI tool. Lots of people's own writing lands here, so this isn't a finding against the work. If you wrote it and want a person to take a look, you can ask for a review.",
      "model_score": 0.623,
      "status": "decided",
      "style_score": 0.6865,
      "timestamp": "2026-11-09T08:49:18+00:00"
    },
    {
      "content_id": "c_28da00cfe9ab",
      "creator_id": "eval_appeal_154915_t3_10",
      "event": "appeal",
      "reasoning": "",
      "status": "under_review",
      "timestamp": "2026-11-09T08:49:19+00:00"
    }
  ],
  "never_issued_appeal": {
    "status": 404,
    "body": {
      "error": "not_found",
      "message": "No submission with content_id 'c_never_issued_154915_3'."
    },
    "pass": true
  }
}
```
