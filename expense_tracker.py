import json
print("Welcome to the Expense tracker!")
expenses = []

def view_expenses():
    if not expenses:
        print("No expenses recorded")
    else:
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. Category : {expense['category']}, Amount: ${expense['amount']}, Description: {expense['description']}")

def search_expenses(category):
    found = [expense for expense in expenses if expense['category'].lower() == category.lower()]
    if found:
        for expense in found:
            print(f"Category: {expense['category']}, Amount: ${expense["amount"]}, Description: {expense['description']}")
        else:
            print(f"No expenses found in category: {category}")

def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total}")

def save_expense():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved to file!")

def load_expense():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        print("Expenses loaded from file")
    except FileNotFoundError:
        print("No saved expenses found")


def add_expense(category, amount, description):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount must be positive.")
        expenses.append({"category": category, "amount": amount, "description": description})
        print(f"Expense added: {category} - ${amount}: {description}")
    except ValueError as e:
        print(f"Invalid amount: {e}")

def sum_expense():
    total = sum(expense['amount'] for expense in expenses)
    print(f"total amount = ${total}")


while True:
    print("\nOptions: [1] Add Expense [2] View Expenses [3] Search Expenses [4] Calculate Total [5] Save [6] Load [7] Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")
        add_expense(category, amount, description)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category = input("Enter category to search: ")
        search_expenses(category)
    elif choice == "4":
        calculate_total()
    elif choice == "5":
        save_expense()
    elif choice == "6":
        load_expense()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
