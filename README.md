# 🛡 ShieldScan — Real-Time Phishing Detection System

ShieldScan is a multi-layer phishing URL detection system built for cybersecurity learning, hackathons, and real-time browser protection demonstrations.

It combines:
- URL heuristic analysis
- Typo-domain detection
- Content analysis
- Domain intelligence
- Real-time Chrome extension scanning

---

# 🚀 Features

✅ Real-time phishing detection  
✅ Chrome Extension (Manifest V3)  
✅ SAFE / SUSPICIOUS / MALICIOUS classification  
✅ Automatic URL scanning  
✅ Threat scoring system (0–100%)  
✅ Explainable AI-style reasoning  
✅ Automatic malicious website blocking  
✅ Typo attack detection (g00gle, paypa1, etc.)  
✅ Content-based login form analysis  
✅ Risk meter and cybersecurity dashboard UI  

---

# 🧠 Multi-Layer Detection Engine

## Layer 1 — URL Heuristics
Analyzes:
- URL length
- Special characters
- Entropy
- Hyphens
- IP usage
- Suspicious keywords

---

## Layer 2 — Domain Intelligence
Checks:
- WHOIS information
- Trusted domains
- Suspicious TLDs
- Domain trust indicators

---

## Layer 3 — Content Analysis
Analyzes webpage content:
- Login forms
- Password fields
- Suspicious text
- Hidden phishing behavior

---

## Layer 4 — Typo / Brand Mimic Detection
Detects fake domains like:
- g00gle
- paypa1
- micros0ft
- amaz0n

using typo analysis and similarity checking.

---

# 🛠 Tech Stack

## Backend
- Python
- FastAPI
- Requests
- BeautifulSoup
- tldextract

## Frontend
- Chrome Extension
- JavaScript
- HTML/CSS
- Manifest V3

---

# 🚀 Project Structure

```bash
ShieldScan_Project/
│
├── backend/
│   ├── main.py
│   ├── heuristics.py
│   ├── typo_detector.py
│   ├── content_analyzer.py
│   ├── domain_analyzer.py
│   ├── feature_extractor.py
│   └── requirements.txt
│
├── extension/
│   ├── manifest.json
│   ├── background.js
│   ├── popup.html
│   ├── popup.js
│   ├── styles.css
│   └── block.html
│
└── screenshots/
