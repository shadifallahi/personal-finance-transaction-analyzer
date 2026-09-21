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
search_category = input("\nEnter a category to search (or press Enter to skip): ")

if search_category:
    print(f"\nTransactions in {search_category}:")

    found = False

    for transaction in transactions:
        if transaction["category"].lower() == search_category.lower():
            print(
                f"{transaction['type'].capitalize()} | "
                f"${transaction['amount']:.2f} | "
                f"{transaction['description']}"
            )
            found = True

    if not found:
        print("No transactions found for this category.")

spending_summary = {}

for transaction in transactions:
    if transaction["type"] == "expense":
        category = transaction["category"]

        if category in spending_summary:
            spending_summary[category] += transaction["amount"]
        else:
            spending_summary[category] = transaction["amount"]

print("\nSpending Summary:")

for category, total in spending_summary.items():
    print(f"{category}: ${total:.2f}")
