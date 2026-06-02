"""Deterministic scoring logic (no LLM calls in this file)."""

from career_data import CAREER_STATEMENTS


ALLOWED_RATINGS = {-1, 0, 1}


def calculate_scores(responses):
    """
    Calculate deterministic category scores from user responses.

    Args:
        responses (dict): Mapping like {"q1": 1, "q2": 0, ...}

    Returns:
        dict: {
            "category_scores": {...},
            "top_categories": [...],
            "total_score": int
        }
    """
    category_scores = {}
    total_score = 0

    for statement in CAREER_STATEMENTS:
        statement_id = statement["id"]
        category = statement["category"]
        rating = responses.get(statement_id)

        if rating not in ALLOWED_RATINGS:
            raise ValueError(f"Invalid rating for {statement_id}. Use only -1, 0, or 1.")

        category_scores[category] = category_scores.get(category, 0) + rating
        total_score += rating

    max_score = max(category_scores.values()) if category_scores else 0
    top_categories = [
        category
        for category, score in category_scores.items()
        if score == max_score
    ]

    return {
        "category_scores": category_scores,
        "top_categories": top_categories,
        "total_score": total_score,
    }
