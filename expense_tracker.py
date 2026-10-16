
import csv
import os
from collections import defaultdict

filename = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ").strip().title()
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero!")
                continue
            break
        except ValueError:
            print("Enter a valid amount!")

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(filename):
        print("No expenses recorded yet!")
        return

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def filter_expenses():
    category = input("Enter category to filter: ").strip().lower()

    if not os.path.exists(filename):
        print("No expenses recorded yet!")
        return

    found = False
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Category"].lower() == category:
                print(row)
                found = True

    if not found:
        print("No expenses found in this category.")

def category_summary():
    totals = defaultdict(float)

    if not os.path.exists(filename):
        print("No expenses recorded yet!")
        return

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            totals[row["Category"]] += float(row["Amount"])

    print("\n--- Category Summary ---")
    for category, total in totals.items():
        print(category, ":", round(total, 2))

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
