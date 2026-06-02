"""LLM client for OpenAI-compatible chat completion APIs."""

import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import build_career_report_prompt


def generate_career_report(score_summary):
    """
    Generate an LLM-based career report from deterministic summary data.

    Returns:
        str: Markdown report from LLM or fallback message on failure.
    """
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        return (
            "### LLM Service Unavailable\n"
            "Could not find `OPENAI_API_KEY` in your environment.\n\n"
            "Add your key to `.env`, then try again."
        )

    try:
        client = OpenAI(api_key=api_key)
        prompt = build_career_report_prompt(score_summary)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You provide practical Gen-AI career guidance grounded in user data."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )

        content = response.choices[0].message.content
        if not content:
            return (
                "### LLM Service Returned Empty Output\n"
                "The model did not return report text. Please try again."
            )

        return content

    except Exception as exc:  # broad catch to keep app beginner-friendly
        return (
            "### LLM Request Failed\n"
            "The deterministic score is still available, but the AI report could not be generated.\n\n"
            f"Technical detail: `{exc}`"
        )
