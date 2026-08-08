total = 0

while True:
    expense = input("Enter an expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative.")
            continue

        total = total + expense

    except ValueError:
        print("Please enter a valid number.")

print(f"\nTotal Spent: {total:.2f}")