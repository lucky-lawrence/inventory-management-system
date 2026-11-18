from database import connect_db
def low_stock_report():
    threshold = int(input("Enter low-stock threshold: "))


    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM products
        WHERE quantity <= ?
        ORDER BY quantity ASC
    """, (threshold,))
    products = cursor.fetchall()

    connection.close()

    print("\n===== LOW STOCK REPORT =====")

    if not products:
        print("No products are running low.")
        return

    for product in products:
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Quantity remaining: {product[3]}")
        print("--------------------------------")

def sales_report():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*), COALESCE(SUM(total), 0)
        FROM sales
    """)

    result = cursor.fetchone()

    total_transactions = result[0]
    total_revenue = result[1]

    cursor.execute("""
        SELECT product_name, SUM(quantity), SUM(total)
        FROM sales
        GROUP BY product_id, product_name
        ORDER BY SUM(total) DESC
    """)

    sales = cursor.fetchall()

    connection.close()

    print("\n======= SALES REPORT ======")
    print(f"Total transactions: {total_transactions}")
    print(f"Total revenue: ${total_revenue:,.2f}")

    print("\n====== PRODUCT SALES ======")

    if not sales:
        print("No sales recorded yet.")
        return

    for sale in sales:
        print(f"Product: {sale[0]}")
        print(f"Units sold: {sale[1]}")
        print(f"Revenue: ${sale[2]:,.2f}")
        print("--------------------------")

