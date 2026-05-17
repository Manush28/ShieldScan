KNOWN_BRANDS = [
    "google", "amazon", "paypal", "facebook",
    "instagram", "netflix", "microsoft", "linkedin"
]


def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)

    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)

    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def normalize(text):
    replacements = {
        "0": "o",
        "1": "l",
        "3": "e",
        "5": "s",
        "rn": "m",
        "vv": "w"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


def clean_domain(domain):
    return domain.replace("-", "").replace("_", "")


def detect_typo(domain):
    if domain in KNOWN_BRANDS:
        return 0, []

    domain = clean_domain(domain)
    normalized = normalize(domain)

    for brand in KNOWN_BRANDS:

        if domain == brand:
            continue

        dist_original = levenshtein(domain, brand)
        dist_normalized = levenshtein(normalized, brand)

        if dist_original <= 2 or dist_normalized <= 2:
            return 0.9, [f"Domain mimics {brand} (typo attack detected)"]

        if brand in normalized:
            return 0.8, [f"Brand keyword detected: {brand}"]

    if any(char.isdigit() for char in domain):
        return 0.6, ["Numeric substitution detected"]

    return 0, []
