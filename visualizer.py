import matplotlib.pyplot as plt
from analyzer import get_day_averages, get_keyword_frequency, get_mood_trend


def show_mood_by_day(entries):
    averages = get_day_averages(entries)

    if not averages:
        print("not enough data to show day patterns yet.")
        return

    days = list(averages.keys())
    scores = list(averages.values())

    # color bars based on positive or negative mood
    colors = ["green" if s >= 0 else "red" for s in scores]

    plt.figure(figsize=(10, 5))
    plt.bar(days, scores, color=colors)
    plt.title("average mood by day of week")
    plt.xlabel("day")
    plt.ylabel("mood score (-1 to 1)")
    plt.axhline(y=0, color="black", linestyle="--", linewidth=0.8)
    plt.tight_layout()
    plt.show()


def show_mood_trend(entries):
    trend = get_mood_trend(entries)

    if len(trend) < 2:
        print("need at least 2 entries to show a trend.")
        return

    dates = [t[0] for t in trend]
    scores = [t[1] for t in trend]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, scores, marker="o", color="blue", linewidth=2)
    plt.title("mood trend over time")
    plt.xlabel("date")
    plt.ylabel("mood score (-1 to 1)")
    plt.axhline(y=0, color="black", linestyle="--", linewidth=0.8)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def show_keyword_frequency(entries):
    freq = get_keyword_frequency(entries)

    if not freq:
        print("no keywords found yet.")
        return

    # take top 10 keywords only
    top_keywords = dict(list(freq.items())[:10])

    words = list(top_keywords.keys())
    counts = list(top_keywords.values())

    plt.figure(figsize=(10, 5))
    plt.barh(words, counts, color="steelblue")
    plt.title("most common topics in your journal")
    plt.xlabel("times mentioned")
    plt.ylabel("keyword")
    plt.tight_layout()
    plt.show()


def show_mood_distribution(entries):
    labels = ["very positive", "positive", "neutral", "negative", "very negative"]
    counts = {label: 0 for label in labels}

    for entry in entries:
        label = entry["mood_label"]
        if label in counts:
            counts[label] += 1

    plt.figure(figsize=(7, 7))
    plt.pie(
        counts.values(),
        labels=counts.keys(),
        autopct="%1.1f%%",
        colors=["darkgreen", "lightgreen", "gold", "salmon", "red"]
    )
    plt.title("overall mood distribution")
    plt.tight_layout()
    plt.show()