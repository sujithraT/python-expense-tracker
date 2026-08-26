print("💰 Welcome to Expense Tracker")

total = 0

while True:
    print("\n1. Add Expense")
    print("2. View Total")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: ₹"))
        total += amount
        print("Expense added successfully!")

    elif choice == "2":
        print(f"Total Expense: ₹{total:.2f}")

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
