# Warehouse Management System

A simple Warehouse Management System built with **Python** and **MySQL** using an object-oriented architecture.

## Features

- Product management
  - Create product
  - Update product
  - Deactivate product
  - View all products

- Inventory management
  - Receive stock
  - Issue stock
  - Low stock validation

- Order management
  - Create orders
  - Update order status
  - View all orders

- Supplier management
  - Create supplier
  - Update supplier
  - View all suppliers

- Product activity logs

## Technologies

- Python 3
- MySQL
- mysql-connector-python
- DataGrip (database management)

## Project Structure

```
db/
models/
services/
repositories/
errors/
sql/
main.py
```

## Database

The SQL script for creating the database is located in:

```
sql/warehouse_management.sql
```

## Running the Project

1. Execute the SQL script to create the database.
2. Configure the database connection in `db/connection.py`.
3. Install dependencies:

```bash
pip install mysql-connector-python
```

4. Run:

```bash
python main.py
```

## Author

Luka
