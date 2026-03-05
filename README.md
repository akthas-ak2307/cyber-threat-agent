# 🛡️ Cyber Threat Monitoring & Alert Agent

**An AI-powered web agent that automatically monitors cybersecurity threats and sends instant alerts.**

---

## 🎯 What Does This Do?

Instead of manually checking multiple cybersecurity news sites, this agent:
- ✅ **Automatically fetches** latest cyber threats from RSS feeds
- ✅ **Analyzes** content using NLP keyword detection
- ✅ **Filters** only critical/important threats
- ✅ **Alerts** you immediately via console/email/Telegram

Think of it as: **A 24/7 watchman for cybersecurity news**

---

## 🧩 Architecture (5 Components)

```
Internet → Collector → Analyzer → Filter → Alerter
              ↑                              ↓
              └──────── Scheduler ───────────┘
```

### 1️⃣ **Data Collector** (`agent/collector.py`)
- Fetches RSS feeds from NVD, CERT-In, BleepingComputer, etc.
- Extracts: title, summary, link, source

### 2️⃣ **Text Analyzer** (`agent/analyzer.py`)
- Detects threat keywords: CVE, zero-day, ransomware, exploit
- Determines severity: CRITICAL, HIGH, MEDIUM, LOW
- Extracts CVE IDs using regex

### 3️⃣ **Threat Filter** (`agent/filter.py`)
- Decision rules:
  - CRITICAL severity → Always alert
  - HIGH + CVE → Alert
  - Exploit + CVE → Alert
  - Multiple CVEs → Alert

### 4️⃣ **Alert Engine** (`agent/alerter.py`)
- Sends alerts via:
  - 🖥️ Console (always enabled)
  - 📧 Email (optional)
  - 📲 Telegram (optional)
- Prevents duplicate alerts using cache

### 5️⃣ **Scheduler** (`agent/scheduler.py`)
- Runs agent every 10 minutes (configurable)
- Autonomous operation, no manual intervention

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure (Optional)
Edit `config/settings.py` or create `.env`:
```env
ALERT_EMAIL=your@email.com
EMAIL_PASSWORD=your_app_password
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### 3. Run
```bash
python main.py
```

---

## 📊 Example Output

```
[COLLECTOR] Fetched 50 articles
[FILTER] 3/50 articles are real threats

🚨 CYBER THREAT ALERT 🚨
============================================================
Time     : 2024-03-07 14:32:10
Title    : Critical Zero-Day in Apache Struts (CVE-2024-1234)
Severity : CRITICAL
Reason   : Critical severity threat detected
Keywords : CVE, zero-day, exploit, RCE
CVEs     : CVE-2024-1234
Source   : The Hacker News
Link     : https://...
============================================================
```

---

## 🔧 Configuration

### RSS Feeds (`config/settings.py`)
```python
RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/",
    "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
    "https://www.cert.gov.in/rss-feed.php",
]
```

### Check Interval
```python
CHECK_INTERVAL_MINUTES = 10  # Run every 10 minutes
```

---

## 🤖 Why This is "AI"?

- **NLP-based keyword detection** (not just string matching)
- **Rule-based decision making** (intelligent filtering)
- **Autonomous behavior** (runs without human input)
- **Context understanding** (severity + CVE + exploit combinations)

This is a **lightweight intelligent agent** — perfect for hackathons!

---

## 🎤 One-Line Pitch

> "An AI-powered web agent that continuously monitors cybersecurity sources, detects critical threats, and instantly alerts users, reducing response time and manual monitoring."

---

## 📁 Project Structure

```
cyber-threat-agent/
├── agent/
│   ├── collector.py   # Fetch RSS feeds
│   ├── analyzer.py    # NLP analysis
│   ├── filter.py      # Decision logic
│   ├── alerter.py     # Send notifications
│   └── scheduler.py   # Automation
├── config/
│   └── settings.py    # Configuration
├── main.py            # Entry point
└── requirements.txt   # Dependencies
```

---

## ✅ Why This Project Wins Hackathons

✔ **Real-world problem** (cybersecurity is critical)  
✔ **Automation** (runs 24/7 without human input)  
✔ **AI/NLP** (intelligent threat detection)  
✔ **No paid APIs** (100% free to run)  
✔ **Easy demo** (visible console alerts)  
✔ **Scalable** (can add more sources/alerts)

---

## 🛠️ Future Enhancements

- [ ] Web dashboard for threat history
- [ ] Machine learning for better severity prediction
- [ ] Integration with Slack/Discord
- [ ] Twitter/X monitoring for #CyberSecurity
- [ ] Database storage (SQLite/PostgreSQL)

---

## 📜 License

MIT License - Free to use and modify

---

**Built for hackathons. Designed for impact. 🚀**
