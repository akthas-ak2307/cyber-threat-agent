def should_alert(analyzed_article):
    """
    Decision rules:
    - CRITICAL severity → always alert
    - HIGH + CVE found → alert
    - Any CVE with exploit keyword → alert
    - Otherwise → ignore
    """
    a = analyzed_article
    severity = a.get("severity", "LOW")
    keywords = a.get("keywords", [])
    cves     = a.get("cves", [])
    
    if severity == "CRITICAL":
        return True, "Critical severity threat detected"
    
    if severity == "HIGH" and len(cves) > 0:
        return True, f"High severity + CVE ({', '.join(cves)})"
    
    # Case-insensitive exploit detection
    exploit_words = ["exploit", "rce", "remote code execution", "zero-day", "zero day"]
    keywords_lower = [kw.lower() for kw in keywords]
    if any(kw in keywords_lower for kw in exploit_words) and len(cves) > 0:
        return True, "Exploit + CVE combination detected"
    
    if len(cves) >= 2:
        return True, f"Multiple CVEs detected: {', '.join(cves)}"
    
    return False, "Not critical enough"

def filter_threats(analyzed_articles):
    """Return only articles that need alerts"""
    threats = []
    for article in analyzed_articles:
        alert, reason = should_alert(article)
        if alert:
            article["alert_reason"] = reason
            threats.append(article)
    
    print(f"[FILTER] {len(threats)}/{len(analyzed_articles)} articles are real threats")
    return threats