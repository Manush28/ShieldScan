import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def analyze_content(url):
    score = 0
    reasons = []

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        has_password = bool(soup.find("input", {"type": "password"}))
        has_form = bool(soup.find("form"))

        if has_password:
            score += 0.1
            reasons.append("Password field detected")

        if has_form:
            score += 0.1
            reasons.append("Form detected")

        if has_password and has_form:
            score += 0.3
            reasons.append("Login form structure detected")

        return min(score, 1), reasons

    except Exception:
        return 0.1, ["Could not fetch page"]
