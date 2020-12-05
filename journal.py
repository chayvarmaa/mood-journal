import sys
import termios
import tty
from analyzer import analyze_mood
from storage import save_entry, get_all_entries, get_entry_count
from visualizer import show_mood_by_day, show_mood_trend, show_keyword_frequency, show_mood_distribution


def print_banner():
    print("=" * 50)
    print("  MoodJournal - daily mood tracker")
    print("=" * 50)


def print_menu():
    print("\nwhat do you want to do?")
    print("  1. write a new journal entry")
    print("  2. view mood trend over time")
    print("  3. view mood by day of week")
    print("  4. view most common topics")
    print("  5. view mood distribution")
    print("  6. view all entries")
    print("  'q' toquit")
    print("")


def flush_input():
    try:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except Exception:
        pass


def read_menu_choice():
    flush_input()
    print("enter choice (1-6 or 'q'): ", end="", flush=True)
    choice = sys.stdin.readline().strip()
    flush_input()
    return choice


def write_entry():
    flush_input()
    print("\nwrite about your day.")
    print("you can type a short line or paste a long paragraph.")
    print("when done, type END on a new line and press Enter.\n")

    lines = []
    while True:
        try:
            line = sys.stdin.readline()
            if line.strip().upper() == "END":
                break
            lines.append(line.rstrip())
        except KeyboardInterrupt:
            print("\ncancelled.")
            return

    text = " ".join(lines).strip()

    if len(text) < 10:
        print("entry too short, try writing a bit more.")
        return

    flush_input()

    result = analyze_mood(text)

    entry = save_entry(
        text=text,
        mood_score=result["score"],
        mood_label=result["label"],
        keywords=result["keywords"]
    )

    print("\n-- entry saved --")
    print("mood detected  : " + result["label"])
    print("mood score     : " + str(result["score"]) + " (scale: -1 to 1)")
    print("subjectivity   : " + str(result["subjectivity"]) + " (0 = factual, 1 = opinionated)")
    print("keywords found : " + ", ".join(result["keywords"]))


def view_all_entries():
    entries = get_all_entries()

    if not entries:
        print("no entries yet.")
        return

    print("\n-- all journal entries --\n")
    for i, entry in enumerate(entries, 1):
        print(str(i) + ". [" + entry["date"] + " " + entry["day"] + "] mood: " + entry["mood_label"] + " (" + str(entry["mood_score"]) + ")")
        print("   " + entry["text"][:100] + "...")
        print("")


def run():
    print_banner()

    while True:
        print_menu()
        choice = read_menu_choice()

        if choice == "1":
            write_entry()

        elif choice == "2":
            entries = get_all_entries()
            if len(entries) < 2:
                print("need at least 2 entries to show a trend.")
            else:
                show_mood_trend(entries)

        elif choice == "3":
            entries = get_all_entries()
            if not entries:
                print("no entries yet.")
            else:
                show_mood_by_day(entries)

        elif choice == "4":
            entries = get_all_entries()
            if not entries:
                print("no entries yet.")
            else:
                show_keyword_frequency(entries)

        elif choice == "5":
            entries = get_all_entries()
            if not entries:
                print("no entries yet.")
            else:
                show_mood_distribution(entries)

        elif choice == "6":
            view_all_entries()

        elif choice == "q":
            print("goodbye.")
            sys.exit(0)

        else:
            print("invalid choice, enter a number between 1 and 6 or 'q' to quit.")


if __name__ == "__main__":
    run()