from database import create_tables
from products import (
    add_product,
    view_products,
    search_product,
    update_product,
    delete_product
)
from sales import record_sale
from reports import (
    low_stock_report,
    sales_report
)


def show_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Low Stock Report")
    print("7. Record Sale")
    print("8. Sales Report")
    print("9. Exit")


def main():
    create_tables()

    while True:
        show_menu()

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            low_stock_report()

        elif choice == "7":
            record_sale()

        elif choice == "8":
            sales_report()

        elif choice == "9":
            print("Thank you for using the Inventory Management System!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()