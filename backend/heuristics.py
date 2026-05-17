SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "banking",
    "signin"
]


def analyze_url(features):
    score = 0
    reasons = []

    if features["length"] > 75:
        score += 0.2
        reasons.append("Very long URL")

    if features["hyphens"] > 2:
        score += 0.2
        reasons.append("Too many hyphens")

    if features["entropy"] > 4:
        score += 0.2
        reasons.append("Random-looking URL")

    if features.get("num_letter_mix"):
        score += 0.5
        reasons.append("Suspicious letter-number mix")

    domain = features.get("domain", "")

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in domain:
            score += 0.3
            reasons.append(f"Suspicious keyword: {keyword}")

    return min(score, 1), reasons
