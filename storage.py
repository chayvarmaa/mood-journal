import json
import os
from datetime import datetime

JOURNAL_FILE = "entries.json"


def load_entries():
    if not os.path.exists(JOURNAL_FILE):
        return []
    with open(JOURNAL_FILE, "r") as f:
        return json.load(f)


def save_entry(text, mood_score, mood_label, keywords):
    entries = load_entries()

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "day": datetime.now().strftime("%A"),
        "time": datetime.now().strftime("%H:%M"),
        "text": text,
        "mood_score": mood_score,
        "mood_label": mood_label,
        "keywords": keywords
    }

    entries.append(entry)

    with open(JOURNAL_FILE, "w") as f:
        json.dump(entries, f, indent=4)

    return entry


def get_all_entries():
    return load_entries()


def get_entry_count():
    return len(load_entries())