"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(
    model_score: float, style_score: float, word_count: int | None = None
) -> float:
    """
    Combine two 0–1 signals into one 0–1 score. Higher means more likely AI.

    The rule, in words:

      1. Average the two signals, weighted by config (0.5 / 0.5).
      2. If the text is short, pull that average toward 0.5 — "unsure" — in
         proportion to how short it is. At FULL_CONFIDENCE_WORDS (100) words or
         more there is no pull; at 50 words the distance from 0.5 is halved.

    Why step 2: on the calibration inputs, a plain human paragraph (53 words)
    scored MORE AI-like than real AI text on both signals, so no weighting
    could separate them. Length was the only thing that did. Short text is
    thin evidence, so it shouldn't get a confident label either way.

    When the signals disagree, the average lands near the middle and the label
    is "unsure" — two methods disagreeing is uncertainty.

    `word_count` of None means "long enough": no pull.
    """
    average = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    if word_count is None:
        strength = 1.0
    else:
        strength = min(1.0, word_count / config.FULL_CONFIDENCE_WORDS)
    score = 0.5 + (average - 0.5) * strength
    return round(min(max(score, 0.0), 1.0), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.
    ← TODO (Milestone 5)

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.

    ⚠️ Write the label text for someone who has never heard the word
    "threshold".

        ✗ "human, 0.81 confidence"
        ✓ "We think this was probably written by a person."

    All three labels have to be **reachable**. If no score can produce one of
    them, your ranges have a gap — and Milestone 5 asks you to submit text that
    produces each one, which is how you'd find out.

    The hardest one to write is "unsure". It has to admit uncertainty without
    sounding like an accusation, because the person reading it may well have
    written every word themselves. Your breakout asks your group what they'd
    think if they got it on their own work. That question is the whole
    milestone.
    """
    # TODO: replace this — thresholds are in config.py
    if score >= config.AI_THRESHOLD:
        return "ai", "PLACEHOLDER — write the high-confidence AI label."
    if score <= config.HUMAN_THRESHOLD:
        return "human", "PLACEHOLDER — write the high-confidence human label."
    return "unsure", "PLACEHOLDER — write the unsure label."


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
