import time
from agent.scheduler import ThreatScheduler
from agent.collector import fetch_rss_feeds
from agent.analyzer  import analyze_article
from agent.filter    import filter_threats
from agent.alerter   import send_alerts
from config.settings import CHECK_INTERVAL_MINUTES

def run_agent():
    """Main agent execution logic"""
    print(f"\n[AGENT] Running at {__import__('datetime').datetime.now().strftime('%H:%M:%S')}")
    
    try:
        # Step 1: Collect
        articles = fetch_rss_feeds()
        
        if not articles:
            print("[AGENT] No articles fetched, skipping this cycle")
            return
        
        # Step 2: Analyze
        analyzed = [analyze_article(a) for a in articles]
        
        # Step 3: Filter
        threats = filter_threats(analyzed)
        
        # Step 4: Alert
        send_alerts(threats)
        
        print(f"[AGENT] Cycle completed successfully")
    except Exception as e:
        print(f"[AGENT] Error during execution: {e}")

if __name__ == "__main__":
    print("🛡️  Cyber Threat Monitoring Agent Starting...")
    print(f"Check interval: {CHECK_INTERVAL_MINUTES} minutes\n")
    
    scheduler = ThreatScheduler(interval_minutes=CHECK_INTERVAL_MINUTES)
    scheduler.start(run_agent, run_immediately=True)

    # Keep main thread alive
    try:
        while True:
            time.sleep(60)
            scheduler.status()   # Print status every 60s
    except KeyboardInterrupt:
        scheduler.stop()
        print("\n👋 Agent shut down cleanly.")