import feedparser
import requests
from config.settings import RSS_FEEDS
import time

def fetch_rss_feeds():
    articles = []
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            if feed.bozo:  # Check for parsing errors
                print(f"[COLLECTOR] Warning: Feed parsing issue for {url}")
            
            for entry in feed.entries[:10]:  # latest 10 per feed
                articles.append({
                    "title":   entry.get("title", ""),
                    "summary": entry.get("summary", ""),
                    "link":    entry.get("link", ""),
                    "source":  feed.feed.get("title", url),
                    "published": entry.get("published", "")
                })
        except requests.exceptions.RequestException as e:
            print(f"[COLLECTOR] Network error fetching {url}: {e}")
        except Exception as e:
            print(f"[COLLECTOR] Error fetching {url}: {e}")
    
    print(f"[COLLECTOR] Fetched {len(articles)} articles")
    return articles