# 🛡 ShieldScan — Real-Time Phishing Detection System

ShieldScan is a multi-layer phishing URL detection system built for cybersecurity and hackathon demonstrations.

It combines:
- URL heuristic analysis
- Typo-domain detection
- Content analysis
- Domain intelligence
- Real-time browser extension scanning

---

# 🚀 Features

✅ Real-time phishing detection  
✅ Chrome extension (Manifest V3)  
✅ SAFE / SUSPICIOUS / MALICIOUS classification  
✅ Threat scoring system (0–100%)  
✅ Explainable AI-style reasoning  
✅ Automatic malicious website blocking  
✅ Typo attack detection (g00gle, paypa1, etc.)  
✅ Content-based login form analysis  

---

# 🧠 Detection Layers

1. URL Heuristics  
2. Domain Intelligence  
3. Content Analysis  
4. Typo / Brand Mimic Detection  

---

# 🛠 Tech Stack

- Python
- FastAPI
- JavaScript
- HTML/CSS
- Chrome Extension API
- tldextract
- BeautifulSoup

---

# 🚀 Setup

## Backend

```bash
cd backend
python -m venv venv
venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
---

# 📸 Screenshots

## ✅ SAFE Detection

![SAFE Detection](screenshots/safe_detection.png)

---

## 🚨 Malicious Detection

![Malicious Detection](screenshots/malicious_detection.png)

---

## 🛡 Block Page

![Block Page](screenshots/block_page.png)
