import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Threat keywords to detect
THREAT_KEYWORDS = [
    "CVE", "zero-day", "zero day", "exploit", "ransomware",
    "vulnerability", "breach", "critical patch", "RCE",
    "remote code execution", "privilege escalation", "malware",
    "backdoor", "trojan", "phishing"
]

# Severity words
SEVERITY_CRITICAL = ["critical", "severe", "emergency", "actively exploited"]
SEVERITY_HIGH     = ["high", "important", "dangerous"]
SEVERITY_MEDIUM   = ["medium", "moderate"]

# RSS Feed Sources (free, no API key needed)
RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/",
    "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
    "https://www.cert.gov.in/rss-feed.php",
    "https://us-cert.cisa.gov/ncas/all.xml",
]

# Alert settings (from environment variables)
ALERT_EMAIL      = os.getenv("ALERT_EMAIL", "")
EMAIL_PASSWORD   = os.getenv("EMAIL_PASSWORD", "")
SMTP_SERVER      = "smtp.gmail.com"
SMTP_PORT        = 587
TELEGRAM_TOKEN   = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# Scheduler interval (in minutes)
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", "10"))

# Cache directory
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cache")
os.makedirs(CACHE_DIR, exist_ok=True)