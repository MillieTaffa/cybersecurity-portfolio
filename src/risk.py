SEVERITY_ORDER = {"informational": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}
CONFIDENCE_ORDER = {"low": 0, "medium": 1, "high": 2}


def classify_severity(score):
    if score >= 4:
        return "critical"
    if score >= 3:
        return "high"
    if score >= 2:
        return "medium"
    if score >= 1:
        return "low"
    return "informational"


def classify_confidence(score):
    if score >= 2:
        return "high"
    if score >= 1:
        return "medium"
    return "low"


def score_severity(indicators):
    return sum(indicators)


def score_confidence(indicators):
    return sum(indicators)
