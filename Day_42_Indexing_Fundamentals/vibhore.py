transactions = [
    {"category": "Books", "amounts": 450},
    {"category": "Electronics", "amount": 2200},
    {"category": "Books", "amount": 300},
    {"category": "Groceries", "amount": 900},
    {"category": "Electronics", "amount": 1800}
]

total_amount = 0

for transaction in transactions:
    total_amount += transaction.get("amount", 0)
    # total_amount += transaction["amount"]
    print(transaction)


print(f'Average amount: {total_amount / len(transactions)}')