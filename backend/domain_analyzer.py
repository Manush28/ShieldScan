import whois
from datetime import datetime
from urllib.parse import urlparse


def get_domain_age(url):
    score = 0
    reasons = []

    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)

        creation_date = w.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        age_days = (datetime.now() - creation_date).days

        if age_days < 30:
            score += 0.5
            reasons.append("Very new domain")

        return min(score, 1), reasons

    except Exception:
        return 0.2, ["WHOIS lookup failed"]
