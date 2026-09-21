
import sqlite3


def create_database():
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_transaction(transaction_type, category, amount, description):
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions (type, category, amount, description)
        VALUES (?, ?, ?, ?)
    """, (transaction_type, category, amount, description))

    connection.commit()
    connection.close()


def get_transactions():
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, type, category, amount, description
        FROM transactions
    """)

    transactions = cursor.fetchall()

    connection.close()

    return transactions
