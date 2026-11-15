# Smart Grocery Store Management System
# Manage products, stock, customer sales, and store performance reports.

products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250.0, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120.0, "stock": 15},
    {"id": 103, "name": "Rice", "category": "Grains", "price": 300.0, "stock": 8},
    {"id": 104, "name": "Eggs", "category": "Dairy", "price": 360.0, "stock": 30},
]

sales_records = []


def find_product_by_id(product_id):
    # Return the product with the matching ID, or None if it does not exist.
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def read_integer(prompt, minimum=None):
    # Read an integer and optionally enforce a minimum value.
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a value of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_price():
    # Read a positive product price.
    while True:
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print("Price must be greater than zero.")
                continue
            return price
        except ValueError:
            print("Invalid price. Enter a number, such as 150 or 150.50.")


def add_product():
    # Collect product details and append a new dictionary if its ID is unique.
    print("\n--- Add New Product ---")
    product_id = read_integer("Enter product ID: ", 1)

    if find_product_by_id(product_id) is not None:
        print("That product ID already exists. Product was not added.")
        return

    name = input("Enter product name: ").strip()
    while not name:
        print("Product name cannot be empty.")
        name = input("Enter product name: ").strip()

    category = input("Enter product category: ").strip().title()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter product category: ").strip().title()

    price = read_price()
    stock = read_integer("Enter available stock: ", 0)

    new_product = {
        "id": product_id,
        "name": name.title(),
        "category": category,
        "price": price,
        "stock": stock
    }
    products.append(new_product)
    print(f"{new_product['name']} was added successfully.")


def display_product(product):
    # Print all details for one product in a consistent format.
    print("-" * 52)
    print(f"Product ID : {product['id']}")
    print(f"Name       : {product['name']}")
    print(f"Category   : {product['category']}")
    print(f"Price      : Rs. {product['price']:.2f}")
    print(f"Stock      : {product['stock']} unit(s)")
    print("-" * 52)


def view_products():
    # Display every product currently stored in the product list.
    print("\n--- All Products ---")
    if not products:
        print("No products are currently available.")
        return

    print(f"{'ID':<8}{'NAME':<20}{'CATEGORY':<14}{'PRICE':>8}{'STOCK':>8}")
    print("-" * 58)
    for product in products:
        print(f"{product['id']:<8}{product['name']:<20}"
              f"{product['category']:<14}{product['price']:>8.2f}"
              f"{product['stock']:>8}")


def search_product():
    # Search for a product using either its numeric ID or its name.
    query = input("\nEnter product ID or name to search: ").strip()
    if not query:
        print("Search value cannot be empty.")
        return

    matches = []
    if query.isdigit():
        product = find_product_by_id(int(query))
        if product is not None:
            matches.append(product)
    else:
        matches = [
            product for product in products
            if query.casefold() in product["name"].casefold()
        ]

    if matches:
        for product in matches:
            display_product(product)
    else:
        print("No matching product was found.")


def update_stock():
    # Add units to stock or replace the current stock quantity.
    product_id = read_integer("\nEnter product ID: ", 1)
    product = find_product_by_id(product_id)

    if product is None:
        print("Product ID not found.")
        return

    print(f"Current stock for {product['name']}: {product['stock']}")
    print("1. Add stock")
    print("2. Set stock to a new quantity")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        quantity = read_integer("How many units should be added? ", 1)
        product["stock"] += quantity
    elif choice == "2":
        quantity = read_integer("Enter the new stock quantity: ", 0)
        product["stock"] = quantity
    else:
        print("Invalid stock update option.")
        return

    print(f"Updated stock for {product['name']}: {product['stock']} unit(s)")


def process_sale():
    # Check product and stock, calculate the bill, update inventory, and save sale details.
    product_id = read_integer("\nEnter product ID to purchase: ", 1)
    product = find_product_by_id(product_id)

    if product is None:
        print("Product not found. Sale cancelled.")
        return

    quantity = read_integer("Enter purchase quantity: ", 1)
    if quantity > product["stock"]:
        print(f"Insufficient stock. Available quantity: {product['stock']}")
        print("Sale cancelled; stock has not been changed.")
        return

    total_amount = product["price"] * quantity
    product["stock"] -= quantity

    sale = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total_amount
    }
    sales_records.append(sale)

    print("\n--- Purchase Summary ---")
    print(f"Product       : {product['name']}")
    print(f"Product ID    : {product['id']}")
    print(f"Quantity      : {quantity}")
    print(f"Unit price    : Rs. {product['price']:.2f}")
    print(f"Total amount  : Rs. {total_amount:.2f}")
    print(f"Remaining stock: {product['stock']}")


def view_sales():
    # Display all completed transactions stored in the sales list.
    print("\n--- Sales Records ---")
    if not sales_records:
        print("No sales have been completed yet.")
        return

    print(f"{'PRODUCT ID':<13}{'PRODUCT NAME':<20}{'QUANTITY':>10}{'TOTAL':>12}")
    print("-" * 55)
    for sale in sales_records:
        print(f"{sale['product_id']:<13}{sale['product_name']:<20}"
              f"{sale['quantity_sold']:>10}{sale['total_amount']:>12.2f}")


def generate_report():
    # Summarize inventory, revenue, low-stock products, and price extremes.
    print("\n" + "=" * 56)
    print("                 STORE REPORT")
    print("=" * 56)

    total_products = len(products)
    total_stock = sum(product["stock"] for product in products)
    total_transactions = len(sales_records)
    total_revenue = sum(sale["total_amount"] for sale in sales_records)

    print(f"Total number of products : {total_products}")
    print(f"Total available stock    : {total_stock}")
    print(f"Total sales transactions : {total_transactions}")
    print(f"Total revenue generated  : Rs. {total_revenue:.2f}")

    low_stock = [product for product in products if product["stock"] < 5]
    print("\nProducts with stock below 5 units:")
    if low_stock:
        for product in low_stock:
            print(f" - {product['name']} (ID: {product['id']}): {product['stock']} unit(s)")
    else:
        print(" - None")

    if products:
        highest_price = max(product["price"] for product in products)
        lowest_price = min(product["price"] for product in products)
        print("\nProduct(s) with highest price:")
        for product in products:
            if product["price"] == highest_price:
                print(f" - {product['name']}: Rs. {product['price']:.2f}")

        print("Product(s) with lowest price:")
        for product in products:
            if product["price"] == lowest_price:
                print(f" - {product['name']}: Rs. {product['price']:.2f}")
    else:
        print("\nNo product price information is available.")

    print("=" * 56)


def main():
    # Keep showing the menu until the user selects Exit.
    while True:
        print("\n" + "=" * 40)
        print("       SMART GROCERY STORE SYSTEM")
        print("=" * 40)
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product Stock")
        print("5. Process Customer Sale")
        print("6. View Sales Records")
        print("7. Generate Store Report")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            process_sale()
        elif choice == "6":
            view_sales()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Thank you for using the Smart Grocery Store System.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
