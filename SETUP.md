# 🚀 Quick Setup Guide (5 Minutes)

## Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Run (No Configuration Needed!)
```bash
python main.py
```

That's it! The agent will:
- ✅ Fetch cyber threats from RSS feeds
- ✅ Analyze and filter critical ones
- ✅ Show alerts in console

---

## Optional: Enable Email/Telegram Alerts

### For Email Alerts:
1. Copy `.env.example` to `.env`
2. Add your Gmail credentials:
```env
ALERT_EMAIL=your@gmail.com
EMAIL_PASSWORD=your_app_password
```

**Note:** Use [App Password](https://support.google.com/accounts/answer/185833), not regular password!

### For Telegram Alerts:
1. Create a bot: Talk to [@BotFather](https://t.me/botfather)
2. Get your chat ID: Talk to [@userinfobot](https://t.me/userinfobot)
3. Add to `.env`:
```env
TELEGRAM_TOKEN=123456:ABC-DEF...
TELEGRAM_CHAT_ID=123456789
```

---

## Customization

### Change Check Interval
In `.env`:
```env
CHECK_INTERVAL_MINUTES=5  # Check every 5 minutes
```

### Add More RSS Feeds
Edit `config/settings.py`:
```python
RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://your-custom-feed.com/rss",
]
```

---

## Troubleshooting

**No articles fetched?**
- Check internet connection
- Some RSS feeds may be slow/down

**Email not working?**
- Use Gmail App Password, not regular password
- Enable "Less secure app access" (if needed)

**Want to test immediately?**
- Set `CHECK_INTERVAL_MINUTES=1` for faster testing

---

## Demo Tips for Judges

1. **Show it running live** - Let it fetch real threats
2. **Explain the 5 components** - Collector → Analyzer → Filter → Alerter → Scheduler
3. **Highlight the AI** - NLP keyword detection, severity analysis
4. **Show the alert** - Point out CVE extraction, severity levels
5. **Mention scalability** - Can add Twitter, Slack, database, ML

---

**Ready to impress! 🎯**
