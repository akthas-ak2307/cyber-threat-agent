import re
from config.settings import THREAT_KEYWORDS, SEVERITY_CRITICAL, SEVERITY_HIGH, SEVERITY_MEDIUM

def clean_text(text):
    """Remove HTML tags and extra whitespace"""
    text = re.sub(r'<[^>]+>', '', text)
    return text.lower().strip()

def detect_keywords(text):
    """Find which threat keywords are present"""
    found = []
    text_lower = text.lower()
    for kw in THREAT_KEYWORDS:
        if kw.lower() in text_lower:
            found.append(kw)
    return found

def detect_severity(text):
    """Determine threat severity level"""
    text_lower = text.lower()
    
    for word in SEVERITY_CRITICAL:
        if word in text_lower:
            return "CRITICAL"
    
    for word in SEVERITY_HIGH:
        if word in text_lower:
            return "HIGH"
    
    for word in SEVERITY_MEDIUM:
        if word in text_lower:
            return "MEDIUM"
    
    return "LOW"

def extract_cve(text):
    """Extract CVE IDs like CVE-2024-1234"""
    return re.findall(r'CVE-\d{4}-\d{4,7}', text, re.IGNORECASE)

def analyze_article(article):
    """Full analysis of one article"""
    full_text = article["title"] + " " + article["summary"]
    cleaned   = clean_text(full_text)
    
    keywords = detect_keywords(full_text)
    severity = detect_severity(full_text)
    cves     = extract_cve(full_text)
    
    return {
        **article,
        "keywords": keywords,
        "severity": severity,
        "cves": cves,
        "is_threat": len(keywords) > 0  # True if any keyword found
    }