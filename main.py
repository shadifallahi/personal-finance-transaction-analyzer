transactions = []

while True:
    transaction_type = input("Enter transaction type (income/expense): ").lower()

    while transaction_type not in ["income", "expense"]:
        print("Invalid transaction type. Please enter income or expense.")
        transaction_type = input("Enter transaction type (income/expense): ").lower()

    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Enter description: ")

    transaction = {
        "type": transaction_type,
        "category": category,
        "amount": amount,
        "description": description
    }

    transactions.append(transaction)

    print("\nTransaction added!")

    another = input("Add another transaction? (yes/no): ").lower()

    if another != "yes":
        break

balance = 0

for transaction in transactions:
    if transaction["type"] == "income":
        balance += transaction["amount"]
    elif transaction["type"] == "expense":
        balance -= transaction["amount"]

print(f"\nCurrent balance: ${balance:.2f}")

print("\nTransaction History:")

for transaction in transactions:
    print(
        f"{transaction['type'].capitalize()} | "
        f"{transaction['category']} | "
        f"${transaction['amount']:.2f} | "
        f"{transaction['description']}"
    )
