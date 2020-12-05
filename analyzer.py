from textblob import TextBlob
import re


def analyze_mood(text):
    blob = TextBlob(text)
    
    # polarity is a number between -1 and 1
    # -1 means very negative, 0 is neutral, 1 is very positive
    polarity = blob.sentiment.polarity
    
    # subjectivity is between 0 and 1
    # 0 means very factual, 1 means very opinion based
    subjectivity = blob.sentiment.subjectivity

    mood_label = get_mood_label(polarity)
    keywords = extract_keywords(text)

    return {
        "score": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "label": mood_label,
        "keywords": keywords
    }


def get_mood_label(polarity):
    if polarity >= 0.5:
        return "very positive"
    elif polarity >= 0.1:
        return "positive"
    elif polarity > -0.1:
        return "neutral"
    elif polarity > -0.5:
        return "negative"
    else:
        return "very negative"


def extract_keywords(text):
    # remove common words and extract meaningful ones
    stopwords = {
        "i", "me", "my", "the", "a", "an", "and", "or", "but",
        "in", "on", "at", "to", "for", "of", "with", "was", "is",
        "it", "this", "that", "had", "have", "been", "were", "are",
        "so", "just", "very", "really", "felt", "feel", "today", "day"
    }

    # clean and split the text
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    
    # filter out stopwords and return unique keywords
    keywords = list(set([w for w in words if w not in stopwords]))
    
    return keywords[:8]


def get_day_averages(entries):
    day_scores = {}

    for entry in entries:
        day = entry["day"]
        score = entry["mood_score"]

        if day not in day_scores:
            day_scores[day] = []
        day_scores[day].append(score)

    # calculate average score per day
    averages = {}
    for day, scores in day_scores.items():
        averages[day] = round(sum(scores) / len(scores), 3)

    return averages


def get_keyword_frequency(entries):
    freq = {}

    for entry in entries:
        for keyword in entry["keywords"]:
            if keyword not in freq:
                freq[keyword] = 0
            freq[keyword] += 1

    # sort by most frequent
    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return sorted_freq


def get_mood_trend(entries):
    # return last 10 entries scores to show trend over time
    recent = entries[-10:]
    return [(e["date"], e["mood_score"]) for e in recent]