from database import connect_db
from products import get_positive_integer

def record_sale():
    product_id = input("Enter product ID: ")
    quantity = get_positive_integer("Enter quantity sold: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    )

    product = cursor.fetchone()

    if product is None:
        print("Product not found.")
        connection.close()
        return

    if quantity <=0:
        print("Quantity must be greater than zero.")
        connection.close()
        return

    if quantity > product[3]: 
        print("Insufficient stock availabe.")
        connection.close()
        return

    product_name = product[1]
    unit_price = product[2]
    total = unit_price * quantity

    cursor.execute("""
        UPDATE products
        SET quantity = quantity -?
        WHERE id = ?
    """, (quantity, product_id))

    cursor.execute("""
        INSERT INTO sales
        (product_id, product_name, quantity, unit_price, total)
        VALUES (?,?,?,?,?)
    """, (
        product_id,
        product_name,
        quantity,
        unit_price,
        total
    ))

    connection.commit()
    connection.close()

    print("\nSale recorded successfully!")
    print(f"Product: {product_name}")
    print(f"Quantity sold: {quantity}")
    print(f"Total: ${total:,.2f}")
