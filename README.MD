# Inventory Management System
A Python-based inventory management application that uses SQLite to manage products, track stock levels, record sales and generate inventory reports.

## Features
* Add, view, search, update and delete products.
* Store product information in an SQLite database.
* Record sales transactions.
* Automatically reduce stock after successful sales.
* Generate low-stock reports.
* Generate sales reports and calculate revenue.
* Validate user input.

## Technologies Used
* Python – Application logic.
* SQLite – Database storage.
* SQL – Database queries and operations.
* JSON – Initial product data and migration.
* Git and GitHub – Version control and project hosting.

## Project Structure
Inventory-Management-System/
│
├── main.py
├── database.py
├── products.py
├── sales.py
├── reports.py
├── inventory.db
├── README.md
├── .gitignore
└── LICENSE

## Requirements
* Python 3
* SQLite (included with standard Python installations)

## How to Run
1. Clone or download the repository.
2. Open the project directory in your terminal.
3. Run the application:
python3 main.py

## Database
The application uses SQLite to store product and sales records in inventory.db.

## Learning Objectives
This project demonstrates:
* Python functions and modules.
* Working with multiple Python files.
* SQLite database connections.
* SQL CRUD operations.
* Database queries and reports.
* Input validation.
* Data persistence.

## Author
Lucky Lawrence

## License
This project is licensed under the MIT License.
