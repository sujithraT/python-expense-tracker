print("💰 Welcome to Expense Tracker")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: ₹"))

            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue

            category = input(
                "Enter category (Food/Travel/Shopping/Other): "
            )

            expenses.append({
                "amount": amount,
                "category": category
            })

            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\n--- Your Expenses ---")

            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. {expense['category']} - "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expense: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
