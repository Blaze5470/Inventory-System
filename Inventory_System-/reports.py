"""
reports.py
Contains reporting functions.
"""



def inventory_report(products):
    """Display complete inventory report."""

    print("\n--- Inventory Report ---")

    for product in products:
        product.display()



def low_stock_report(products):
    """Display low stock report."""

    print("\n--- Low Stock Report ---")

    found = False

    for product in products:
        if product.quantity <= product.reorder_level:
            product.display()
            found = True

    if not found:
        print("No low stock items.")



def inventory_value_report(products):
    """Display total inventory value."""

    print("\n--- Inventory Value Report ---")

    total_value = 0

    for product in products:
        total_value += product.quantity * product.unit_price

    print(f"Total Inventory Value: ${total_value:.2f}")



def open_purchase_orders_report(purchase_orders):
    """Display open purchase orders."""

    print("\n--- Open Purchase Orders ---")

    for po in purchase_orders:
        if po.status == "OPEN":
            po.display()



def reorder_suggestions(products):
    """Display reorder suggestions."""

    print("\n--- Reorder Suggestions ---")

    for product in products:

        if product.quantity <= product.reorder_level:
            print(
                f"{product.name} should reorder "
                f"{product.reorder_quantity} units."
            )