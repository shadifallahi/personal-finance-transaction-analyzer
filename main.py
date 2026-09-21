transactions = []

transaction_type = input("Enter transaction type (income/expense): ")
category = input("Enter category: ")
amount = float(input("Enter amount: $"))
description = input("Enter description: ")

transaction = {
    "type": transaction_type,
    "category": category,
    "amount": amount,
    "description": description
}

transactions.append(transaction)

print("\nTransaction added!")
print(transaction)

balance = 0

for transaction in transactions:
    if transaction["type"] == "income":
        balance += transaction["amount"]
    elif transaction["type"] == "expense":
        balance -= transaction["amount"]

print(f"Current balance: ${balance:.2f}")
