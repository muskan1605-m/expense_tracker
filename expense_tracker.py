import csv
from datetime import datetime

def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not date:
            print("❌ Date cannot be empty.")
            return
        
        if not validate_date(date):
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            return

        category = input("Enter category (e.g., Food, Transport, etc.): ").strip()
        if not category:
            print("❌ Category cannot be empty.")
            return

        description = input("Enter description: ").strip()
        if not description:
            print("❌ Description cannot be empty.")
            return

        amount_str = input("Enter amount: ").strip()
        if not amount_str:
            print("❌ Amount cannot be empty.")
            return
        
        if not validate_amount(amount_str):
            print("❌ Invalid amount. Please enter a valid number.")
            return
        
        amount = float(amount_str)

        with open("expenses.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("✅ Expense added successfully.")

    except Exception as e:
        print(f"❌ Error adding expense: {e}")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            if len(rows) <= 1:  # Only header or empty file
                print("\n📝 No expenses recorded yet.")
                return
            
            print("\n--- All Expenses ---")
            print(f"{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<10}")
            print("-" * 65)
            
            for row in rows[1:]:  # Skip header row
                if len(row) >= 4:
                    print(f"{row[0]:<12} {row[1]:<15} {row[2]:<25} ${row[3]:<10}")

    except FileNotFoundError:
        print("❌ Expenses file not found.")
    except Exception as e:
        print(f"❌ Error reading expenses: {e}")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ").strip()

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("👋 Exiting the tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")




    