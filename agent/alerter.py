import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config.settings import CACHE_DIR, ALERT_EMAIL, EMAIL_PASSWORD

# Track already-alerted links (avoid duplicates)
ALERTED_CACHE = set()
CACHE_FILE = os.path.join(CACHE_DIR, "alerted_cache.json")

def load_cache():
    global ALERTED_CACHE
    try:
        with open(CACHE_FILE) as f:
            ALERTED_CACHE = set(json.load(f))
    except:
        ALERTED_CACHE = set()

def save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(list(ALERTED_CACHE), f)

def is_duplicate(article):
    return article["link"] in ALERTED_CACHE

def mark_alerted(article):
    ALERTED_CACHE.add(article["link"])
    save_cache()

# ── Console Alert (always works, good for demo) ──
def alert_console(threat):
    print("\n" + "="*60)
    print(f"🚨 CYBER THREAT ALERT 🚨")
    print(f"Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Title    : {threat['title']}")
    print(f"Severity : {threat['severity']}")
    print(f"Reason   : {threat['alert_reason']}")
    print(f"Keywords : {', '.join(threat['keywords'])}")
    print(f"CVEs     : {', '.join(threat['cves']) if threat['cves'] else 'None'}")
    print(f"Source   : {threat['source']}")
    print(f"Link     : {threat['link']}")
    print("="*60 + "\n")

# ── Email Alert ──
def alert_email(threat, to_email=None, from_email=None, password=None):
    # Use settings if not provided
    to_email = to_email or ALERT_EMAIL
    from_email = from_email or ALERT_EMAIL
    password = password or EMAIL_PASSWORD
    
    if not all([to_email, from_email, password]):
        print("[ALERT] Email credentials not configured, skipping email alert")
        return
    
    try:
        msg = MIMEMultipart()
        msg["Subject"] = f"🚨 [{threat['severity']}] Cyber Threat: {threat['title'][:60]}"
        msg["From"] = from_email
        msg["To"] = to_email
        
        body = f"""
CYBER THREAT ALERT
==================
Title    : {threat['title']}
Severity : {threat['severity']}
Reason   : {threat['alert_reason']}
Keywords : {', '.join(threat['keywords'])}
CVEs     : {', '.join(threat['cves']) if threat['cves'] else 'None'}
Source   : {threat['source']}
Link     : {threat['link']}
Time     : {datetime.now()}
"""
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(from_email, password)
            s.sendmail(from_email, to_email, msg.as_string())
        
        print(f"[ALERT] Email sent for: {threat['title'][:50]}")
    except Exception as e:
        print(f"[ALERT] Email failed: {e}")

# ── Telegram Alert ──
def alert_telegram(threat, token=None, chat_id=None):
    from config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
    
    token = token or TELEGRAM_TOKEN
    chat_id = chat_id or TELEGRAM_CHAT_ID
    
    if not token or not chat_id:
        print("[ALERT] Telegram credentials not configured, skipping Telegram alert")
        return
    
    try:
        import requests
        msg = (
            f"🚨 *CYBER THREAT ALERT*\n\n"
            f"*{threat['title']}*\n"
            f"🔴 Severity: `{threat['severity']}`\n"
            f"🔍 Reason: {threat['alert_reason']}\n"
            f"🏷 CVEs: {', '.join(threat['cves']) if threat['cves'] else 'None'}\n"
            f"🔗 [Read More]({threat['link']})"
        )
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, json={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"})
        print(f"[ALERT] Telegram sent for: {threat['title'][:50]}")
    except Exception as e:
        print(f"[ALERT] Telegram failed: {e}")

# ── Master Alert Function ──
def send_alerts(threats):
    load_cache()
    new_threats = [t for t in threats if not is_duplicate(t)]
    
    if not new_threats:
        print("[ALERT] No new threats to alert.")
        return
    
    for threat in new_threats:
        alert_console(threat)    # Always show in console
        alert_email(threat)      # Auto-uses settings if configured
        alert_telegram(threat)   # Auto-uses settings if configured
        mark_alerted(threat)
    
    print(f"[ALERT] Sent {len(new_threats)} new alerts.")