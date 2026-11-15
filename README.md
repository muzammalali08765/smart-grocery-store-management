# Smart Grocery Store Management System

## Project Overview

The Smart Grocery Store Management System is a menu-driven Python application for a small grocery shop. It helps the store owner manage products, update inventory, process customer purchases, review sales, and generate a store report.

## Project Structure

```text
smart-grocery-store-management/
├── grocery_store.py
└── README.md
```

## Product Information

Each product is stored as a dictionary inside the `products` list. A product contains:

- `id`: unique product ID
- `name`: product name
- `category`: product category
- `price`: unit price
- `stock`: available quantity

The program starts with four sample products (Milk, Bread, Rice, and Eggs) so that the menu can be tested immediately. New products can be added while the program is running. Product data and sales records are held in memory and reset when the program is closed.

## Features

1. **Add New Product:** asks for product details, rejects duplicate IDs, creates a dictionary, and appends it to the products list.
2. **View All Products:** displays the product ID, name, category, price, and stock.
3. **Search Product:** finds a product by numeric ID or by all/part of its name.
4. **Update Product Stock:** allows the user to add units or set a new stock quantity.
5. **Process Customer Sale:** checks that the product exists and enough stock is available, calculates the total, deducts stock, and records the completed sale.
6. **View Sales Records:** displays all completed transactions.
7. **Generate Store Report:** displays product count, total stock, transaction count, revenue, products with fewer than five units, and highest/lowest priced products.
8. **Exit:** closes the program.

## Python Concepts Used

- **Lists:** `products` and `sales_records` hold multiple records.
- **Dictionaries:** each product and sale is stored as a dictionary with named keys.
- **`append()`:** adds new product and completed sale dictionaries to their lists.
- **Functions:** separate functions handle input validation, product search, inventory updates, sales, and reports.
- **Loops:** iterate through products and sales and keep the menu running.
- **Conditions:** handle menu choices, duplicate IDs, missing products, and insufficient stock.
- **Input validation:** `try/except ValueError` handles invalid numeric input. Product IDs and quantities are checked, prices must be positive, and stock cannot be negative.

## How to Run

Python 3 is required. Open a terminal in the project folder and run:

```bash
python grocery_store.py
```

Follow the on-screen menu and enter the requested information.

## Sample Run

The following is an example of processing a sale for two units of Milk (product ID 101):

```text
SMART GROCERY STORE SYSTEM
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice: 5
Enter product ID to purchase: 101
Enter purchase quantity: 2

--- Purchase Summary ---
Product       : Milk
Product ID    : 101
Quantity      : 2
Unit price    : Rs. 250.00
Total amount  : Rs. 500.00
Remaining stock: 18
```

If a customer requests more units than are available, the program cancels the sale and does not change the stock.

## Important Note

This is a beginner-level, in-memory application. Product and sales data are not saved to a file or database, so they are reset when the program exits. Persistent storage can be added as a future improvement.

## GitHub Submission

Create a public repository named `smart-grocery-store-management`, upload `grocery_store.py` and `README.md`, commit the files, and submit the public repository URL to your LMS.
