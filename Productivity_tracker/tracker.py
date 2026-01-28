from storage import load_data, save_data
from utils import get_valid_duration
from datetime import date, datetime, timedelta

def add_session():
    subject = input("Enter subject: ").strip()
    if not subject:
        print("Subject cannot be empty.")
        return

    duration = get_valid_duration()
    session_date = str(date.today())

    data = load_data()
    data.append({
        "subject": subject,
        "duration": duration,
        "date": session_date
    })

    save_data(data)
    print("Session added successfully.")

def show_summary():
    data = load_data()
    if not data:
        print("No study sessions found.")
        return

    total = 0
    subjects = {}

    for entry in data:
        total += entry["duration"]
        subjects[entry["subject"]] = subjects.get(entry["subject"], 0) + entry["duration"]

    print("\n--- Total Study Summary ---")
    print("Total time:", total, "minutes")
    for sub, time in subjects.items():
        print(f"{sub}: {time} minutes")

def show_by_date():
    data = load_data()
    date_input = input("Enter date (YYYY-MM-DD): ")

    print(f"\nSessions on {date_input}:")
    found = False

    for entry in data:
        if entry["date"] == date_input:
            print(f"{entry['subject']} - {entry['duration']} minutes")
            found = True

    if not found:
        print("No sessions found.")

def show_weekly_summary():
    data = load_data()
    today = datetime.today().date()
    week_ago = today - timedelta(days=7)

    total = 0
    subjects = {}

    for entry in data:
        entry_date = datetime.strptime(entry["date"], "%Y-%m-%d").date()
        if week_ago <= entry_date <= today:
            total += entry["duration"]
            subjects[entry["subject"]] = subjects.get(entry["subject"], 0) + entry["duration"]

    print("\n--- Weekly Summary (Last 7 Days) ---")
    print("Total time:", total, "minutes")

    if total == 0:
        print("No study activity this week.")
        return

    for sub, time in subjects.items():
        print(f"{sub}: {time} minutes")
