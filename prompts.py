"""Prompt builder for LLM-generated career report."""

import json


def build_career_report_prompt(score_summary):
    """
    Build a structured prompt that asks the LLM for a markdown report.

    Args:
        score_summary (dict): Deterministic output from calculate_scores().

    Returns:
        str: Prompt text to send to the LLM.
    """
    summary_json = json.dumps(score_summary, indent=2)

    return f"""
You are an expert Gen-AI career counsellor.

I will provide a deterministic career preference score summary in JSON.
Use it to produce a personalized beginner-friendly report.
Be specific and practical.

Deterministic score summary:
```json
{summary_json}
```

Return your answer in clear markdown with these exact sections:

## Career Fit Summary
- A concise interpretation of the user's fit based on the scores.

## Top Gen-AI Areas
- Mention the strongest categories from the score summary.

## Suggested Career Paths (3-5)
For each path:
- **Path Name**
- **Why this fits**
- **Two practical starting steps**

## Portfolio Project Idea
- One concrete beginner-friendly project idea aligned to the top categories.
- Include what to build, key features, and what to show on GitHub.

## 14-Day Beginner Roadmap
- Day-by-day or phase-based plan for 14 days.
- Keep tasks realistic for a beginner.

## Recommended GitHub Showcase Improvements
- 5-7 actionable improvements for presenting this project professionally.

Important constraints:
- Keep the advice aligned with the provided deterministic results.
- Avoid generic motivational filler.
- Make it directly useful for someone building a GitHub portfolio.
""".strip()
