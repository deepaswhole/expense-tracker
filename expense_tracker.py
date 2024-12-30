print("Welcome to the Expense tracker!")
expenses = []

def add_expense(category, amount, description):
    expenses.append({"category": category, "amount": amount, "description": description})
    print(f"Expense added: {category} - ${amount} : {description}")

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
            