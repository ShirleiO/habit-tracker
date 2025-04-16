import csv
import os

# Define the CSV file name
CSV_FILE = "habits.csv"
HABITS_FILE = "habits_list.txt"  # File to store custom habits

# Predefined list of habits (editable in the future)
def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    return ["Exercise", "Meditation", "Painting", "Reading", "Baking"]

HABIT_OPTIONS = load_habits()
STATUS_OPTIONS = ["15%", "50%", "100%"] # Status now represented as percentages

# Function to initialize the CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Habit Name", "Date (DD-MM)", "Status"])  # Column headers
        print("CSV file created successfully!")
    
# Function to add a new habit entry
def add_habit():
    print("\nChoose a habit:")
    for i, habit in enumerate(HABIT_OPTIONS, start=1):
        print(f"{i}. {habit}")
    choice = input("Enter the number of the habit: ")
    
    try:
        habit_name = HABIT_OPTIONS[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please select a number from the list.")
        return
    
    day = input("Enter the day (DD): ")
    month = input("Enter the month (MM): ")
    
    try:
        date = f"{int(day):02d}-{int(month):02d}"
    except ValueError:
        print("Invalid date format.")
        return
    
    print("\nChoose a status:")
    for i, status in enumerate(STATUS_OPTIONS, start=1):
        print(f"{i}. {status}")
    status_choice = input("Enter the number of the status: ")
    
    try:
        status = STATUS_OPTIONS[int(status_choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please select a number from the list.")
        return
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([habit_name, date, status])
    print(f"Habit '{habit_name}' recorded for {date} with status '{status}'.")

# Function to view all habit entries
def view_habits():
    if not os.path.exists(CSV_FILE):
        print("No habits recorded yet.")
        return
    
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        habits = list(reader)
        
        if len(habits) <= 1:
            print("No habits recorded yet.")
            return
        
        print("\nLogged Habits:")
        for row in habits[1:]:  # Skip header row
            print(f"Habit: {row[0]}, Date: {row[1]}, Status: {row[2]}")

# Function to update a habit entry
def update_habit():
    if not os.path.exists(CSV_FILE):
        print("No habits recorded yet.")
        return
    
    habit_name = input("Enter the habit name to update: ")
    day = input("Enter the day (DD): ")
    month = input("Enter the month (MM): ")
    
    try:
        date = f"{int(day):02d}-{int(month):02d}"
    except ValueError:
        print("Invalid date format.")
        return
    
    print("\nChoose a new status:")
    for i, status in enumerate(STATUS_OPTIONS, start=1):
        print(f"{i}. {status}")
    status_choice = input("Enter the number of the status: ")
    
    try:
        new_status = STATUS_OPTIONS[int(status_choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please select a number from the list.")
        return
    
    updated = False
    habits = []
    
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        habits = list(reader)
    
    for row in habits:
        if row[0] == habit_name and row[1] == date:
            row[2] = new_status
            updated = True
    
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(habits)
    
    if updated:
        print(f"Habit '{habit_name}' on {date} updated to '{new_status}'.")
    else:
        print("Habit entry not found.")

# Function to create a new habit
def create_new_habit():
    new_habit = input("Enter the name of the new habit: ").strip()
    if not new_habit:
        print("Habit name cannot be empty.")
        return
    
    if new_habit in HABIT_OPTIONS:
        print("This habit already exists.")
        return
    
    with open(HABITS_FILE, "a") as file:
        file.write(new_habit + "\n")
    
    HABIT_OPTIONS.append(new_habit)
    print(f"New habit '{new_habit}' added successfully!")

# Main menu loop
def main():
    initialize_csv()
    while True:
        print("\nHabit Tracker")
        print("1. Add a new habit entry")
        print("2. View all habits")
        print("3. Update a habit")
        print("4. Create a new habit")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_habit()
        elif choice == "2":
            view_habits()
        elif choice == "3":
            update_habit()
        elif choice == "4":
            create_new_habit()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
