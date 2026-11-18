import sqlite3
import json
import os

def connect_db():
    connection = sqlite3.connect("inventory.db")
    return connection

def create_tables():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            category TEXT NOT NULL
            )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total REAL NOT NULL,
            sale_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
    connection.commit()
    connection.close()


def migrate_products():

    if not os.path.exists("products.json"):
        print("No products.json file found. Skipping initial migration.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    with open("products.json", "r") as file:
        products = json.load(file)

    for product in products:
        cursor.execute("""
            INSERT OR IGNORE INTO products
            (id, name, price, quantity, category)
            VALUES (?,?,?,?,?)
        """, (
            product["id"],
            product["name"],
            product["price"],
            product["quantity"],
            product["category"],
        ))
    connection.commit()
    connection.close()

    print("Products transfered successfully!")

def verify_database():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("PRAGMA integrity_check")

    result = cursor.fetchone()

    print("\n===== DATABASE INTEGRITY =======")
    print(f"Database status: {result[0]}")

    cursor.execute("SELECT COUNT(*) FROM products")

    product_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales")
    sales_count = cursor.fetchone()[0]

    print(f"Total products: {product_count}")
    print(f"Total sales: {sales_count}")

    connection.close()

if __name__ == "__main__":
    create_tables()
    migrate_products()
    verify_database()
    print("\nDatabase setup completed!")    