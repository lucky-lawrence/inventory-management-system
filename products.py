from database import connect_db

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    category = input("Enter product category: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products (name, price, quantity, category)
        VALUES(?,?,?,?)
    """, (name, price, quantity, category))
    
    connection.commit()
    connection.close()

    print("Product added successfully!")

def view_products():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    print("\n====== INVENTORY ========")

    for product in products:
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Price: {product[2]:,.2f}")
        print(f"Quantity: {product[3]}")
        print(f"Category: {product[4]}")
        print("--------------------------")

def search_product():
    search_term = input("Enter product name or Id: ").strip()

    connection = connect_db()
    cursor = connection.cursor()

    if search_term.isdigit():
        cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (int(search_term),)
        )
    else:    
        cursor.execute(
            "SELECT * FROM products WHERE name LIKE ?",
            (f"%{search_term}%",)
        )        
    product = cursor.fetchone()
    connection.close()

    if product:
        print("\nProduct found!")
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Price: {product[2]:,.2f}")
        print(f"Quantity: {product[3]}")
        print(f"Category: {product[4]}")
    else:
        print("Product not found.")

def update_product():
    product_id = input("Enter product ID to update: ")

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

    print("Leave a field empty to keep its current value.")

    new_name = input("New product name: ")
    new_price = input("New product price: ") 
    new_quantity = input("New product quantity: ") 
    new_category = input("New product category: ") 

    name = new_name if new_name else product[1]
    price = new_price if new_name else product[2]
    quantity = new_quantity if new_quantity else product[3]
    category = new_category if new_category else product[4]

    cursor.execute("""
        UPDATE products
        SET name = ?, price = ?, quantity =? , category = ?
        WHERE id = ?
    """, (name , price, quantity, category, product_id))
    connection.commit()
    connection.close()

    print("Product updated successfully!")

def delete_product():
    product_id = input("Enter product id to delete: ")

    confirmation = input(
        "Are you sure you want to delete this product? (yes/no): "
    )
    if confirmation != "yes":
        print("Delection cancelled.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    if cursor.rowcount > 0:
        print("Product deleted successfully!")
    else:
        print("Product not found.")

    connection.commit()
    connection.close()

def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value <=0 :
                print("Please enter a whole number greater than zero.")
            else :
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")     
        

if __name__ == "__main__":
    view_products()    