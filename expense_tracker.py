import csv
from datetime import datetime

def show_menu(): # This function shows the menu of the expense tracker
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")

def validate_date(date_str): # This function validates the date
    try:
        datetime.strptime(date_str, "%Y-%m-%d") # specifies the date format
        return True
    except ValueError:
        return False

def validate_amount(amount_str): # This function validates the amount
    try:
        float(amount_str) # converts the amount to a float
        return True
    except ValueError: 
        return False

def add_expense(): # This function adds a new expense
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip() 
        if not date:
            print("❌ Date cannot be empty.")
            return 
        
        if not validate_date(date): #checks if the date is in valid format
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            return

        category = input("Enter category (e.g., Food, Transport, etc.): ").strip() # asks for the category
        if not category:
            print("❌ Category cannot be empty.")
            return

        description = input("Enter description: ").strip() # asks for the description
        if not description:
            print("❌ Description cannot be empty.")
            return

        amount_str = input("Enter amount: ").strip() # asks for the amount
        if not amount_str:
            print("❌ Amount cannot be empty.")
            return
        
        if not validate_amount(amount_str):
            print("❌ Invalid amount. Please enter a valid number.")
            return
        
        amount = float(amount_str)

        with open("expenses.csv", "a", newline='') as file: # opens the file in append mode 
            writer = csv.writer(file) 
            writer.writerow([date, category, description, amount]) # writes the expense to the opened file

        print("✅ Expense added successfully.")

    except Exception as e:
        print(f"❌ Error adding expense: {e}") 

def view_expenses(): # This function views all the expenses
    try:
        with open("expenses.csv", "r") as file: # opens the file in read mode
            reader = csv.reader(file) # reads the file
            rows = list(reader) # converts the file to a list
            
            if len(rows) <= 1: # checks if the file is empty
                print("\n📝 No expenses recorded yet.")
                return
            
            print("\n--- All Expenses ---") # prints the header of the expenses
            print(f"{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<10}") #defines the columns of the expenses
            print("-" * 65)
            
            for row in rows[1:]:  # prints the expenses after the header
                if len(row) >= 4:
                    print(f"{row[0]:<12} {row[1]:<15} {row[2]:<25} ${row[3]:<10}") # prints the expenses in a neat table format

    except FileNotFoundError: # if the file is not found, it prints an error message
        print("❌ Expenses file not found.")
    except Exception as e: # if there is an error, it prints an error message
        print(f"❌ Error reading expenses: {e}")

while True: # main lopp of the program
    show_menu()
    choice = input("Choose an option (1-3): ").strip() # asks for the choice of the user as 1,2 or 3

    if choice == '1': # adds a new expense
        add_expense()
    elif choice == '2': # views all the expenses
        view_expenses()
    elif choice == '3': #exits the program
        print("👋 Exiting the tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.") # if the choice is not 1,2 or 3, it prints an error message




    