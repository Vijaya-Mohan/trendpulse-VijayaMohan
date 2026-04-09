import os
import json
import time
from datetime import datetime
import requests

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"],
}

try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    response.raise_for_status()
    story_ids = response.json()[:500]
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []

collected = {category: [] for category in categories}

for story_id in story_ids:
    # get_story(story_id) (inlined)
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        story = response.json()
    except Exception as e:
        print(f"Error fetching story {story_id}:", e)
        story = None

    if not story or "title" not in story:
        continue
    title = story.get("title")
    if not title:
        continue
    title_lower = title.lower()
    category = None
    for cat, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                category = cat
                break
        if category:
            break

    if not category:
        continue

    # Limit to 25 per category
    if len(collected[category]) >= 25:
        continue

    processed_story = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by"),
        "collected_at": datetime.now().isoformat(),
    }

    collected[category].append(processed_story)
    if all(len(collected[c]) >= 25 for c in categories):
        break
for _ in categories:
    time.sleep(2)

filename = f"C:\\Users\\vijay\\OneDrive\\Documents\\Masai_git\\Mini_project\\data\\trends_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
all_stories = []
for stories in collected.values():
    all_stories.extend(stories)

with open(filename, "w", encoding="utf-8") as f:
    json.dump(all_stories, f, indent=2, ensure_ascii=False)

print(f"Saved {len(all_stories)} stories to {filename}")