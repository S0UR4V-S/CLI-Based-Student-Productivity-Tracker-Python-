from tracker import (
    add_session,
    show_summary,
    show_by_date,
    show_weekly_summary
)

def menu():
    while True:
        print("\n--- Productivity Tracker ---")
        print("1. Add study session")
        print("2. View total summary")
        print("3. View sessions by date")
        print("4. View weekly summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_session()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_by_date()
        elif choice == "4":
            show_weekly_summary()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
