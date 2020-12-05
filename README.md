# MoodJournal

A command line journal that tracks your mood over time using sentiment analysis.

I wanted to understand my own emotional patterns better so I built a tool that 
analyzes what I write and tells me how I am feeling without me having to label it myself.

## What it does

- Write journal entries in the terminal
- Automatically detects mood using sentiment analysis (TextBlob)
- Shows mood score on a scale of -1 (very negative) to 1 (very positive)
- Tracks keywords and topics you write about most
- Visualizes mood trends over time with charts
- Shows which days of the week you are happiest
- Stores all entries locally in a JSON file

## Requirements

- Python 3.x
- textblob
- matplotlib

## Setup
```bash
git clone https://github.com/yourusername/mood-journal
cd mood-journal
python3 -m venv venv
source venv/bin/activate
pip install textblob matplotlib
```

## Usage
```bash
python3 journal.py
```

## Menu options

- 1 - write a new entry (type END when finished)
- 2 - view mood trend over time
- 3 - view mood by day of week
- 4 - view most common topics
- 5 - view mood distribution
- 6 - view all entries
- q - quit

## What I learned

- How sentiment analysis works using polarity and subjectivity scores
- How to store and retrieve structured data using JSON
- How to build multi-file Python projects with separation of concerns
- Data visualization with matplotlib (bar charts, line charts, pie charts)
- Handling terminal input buffering issues on Mac