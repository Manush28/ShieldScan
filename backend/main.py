from fastapi import FastAPI
from pydantic import BaseModel

from feature_extractor import extract_features, get_main_domain
from heuristics import analyze_url
from content_analyzer import analyze_content
from domain_analyzer import get_domain_age
from typo_detector import detect_typo
from scorer import classify
from config import TRUSTED_DOMAINS, BANNED_DOMAINS

app = FastAPI()


class URLRequest(BaseModel):
    url: str


@app.get("/health")
def health():
    return {"status": "running"}


@app.post("/detect")
def detect(req: URLRequest):
    url = req.url.lower()
    domain = get_main_domain(url)

    if domain in TRUSTED_DOMAINS:
        return {
            "url": url,
            "label": "SAFE",
            "score": 0.0,
            "confidence": "100%",
            "reasons": ["Trusted domain"]
        }

    for banned in BANNED_DOMAINS:
        if banned in url:
            return {
                "url": url,
                "label": "MALICIOUS",
                "score": 1.0,
                "confidence": "100%",
                "reasons": ["Domain is in banned list"]
            }

    features = extract_features(url)
    layer1_score, reasons = analyze_url(features)

    try:
        layer3_score, content_reasons = analyze_content(url)
    except Exception:
        layer3_score = 0.1
        content_reasons = ["Content analysis failed"]

    reasons.extend(content_reasons)

    try:
        domain_score, domain_reasons = get_domain_age(url)
    except Exception:
        domain_score = 0.1
        domain_reasons = ["WHOIS lookup failed"]

    reasons.extend(domain_reasons)

    typo_score, typo_reasons = detect_typo(features.get("domain", ""))
    reasons.extend(typo_reasons)

    final_score = (
        0.4 * layer1_score +
        0.3 * layer3_score +
        0.2 * domain_score +
        0.35 * typo_score
    )

    if layer3_score > 0.3 and typo_score > 0.3:
        final_score += 0.3
        reasons.append("Phishing pattern: login + fake domain")

    final_score = min(max(final_score, 0), 1)

    label = classify(final_score)

    confidence = round(final_score * 100, 2)

    explanation = (
        "This website is flagged because: " + ", ".join(reasons)
    )

    return {
        "url": url,
        "label": label,
        "score": final_score,
        "confidence": f"{confidence}%",
        "reasons": reasons,
        "explanation": explanation,
        "features": features
    }
