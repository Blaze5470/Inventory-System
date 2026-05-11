"""
index.py
Main menu system for Inventory and Purchase Order System
"""

from inventory_manager import (
    add_product,
    view_products,
    search_product,
    edit_product,
    deactivate_product,
    display_low_stock,
    sort_products,
    add_vendor,
    view_vendors,
    search_vendor,
    edit_vendor,
    create_purchase_order,
    view_purchase_orders,
    receive_shipment
)
from file_manager import load_products, load_vendors, load_purchase_orders, save_products, save_vendors, save_purchase_orders
from reports import inventory_report, low_stock_report, inventory_value_report, open_purchase_orders_report

PRODUCT_FILE = "products.json"
VENDOR_FILE = "vendors.json"
PO_FILE = "purchase_orders.json"

# Load data
products = load_products(PRODUCT_FILE)
vendors = load_vendors(VENDOR_FILE)
purchase_orders = load_purchase_orders(PO_FILE)


# ---------------- MENUS ----------------

def product_menu():
    """Display product management menu."""
    while True:
        print("\n--- Product Menu ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Edit Product")
        print("5. Deactivate Product")
        print("6. Display Low Stock Products")
        print("7. Sort Products")
        print("8. Back")

        choice = input("Enter choice: ")
        if choice == "1":
            add_product(products, vendors)
        elif choice == "2":
            view_products(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            edit_product(products)
        elif choice == "5":
            deactivate_product(products)
        elif choice == "6":
            display_low_stock(products)
        elif choice == "7":
            sort_products(products)
        elif choice == "8":
            break
        else:
            print("Invalid choice.")


def vendor_menu():
    """Display vendor management menu."""
    while True:
        print("\n--- Vendor Menu ---")
        print("1. Add Vendor")
        print("2. View Vendors")
        print("3. Search Vendor")
        print("4. Edit Vendor")
        print("5. Back")

        choice = input("Enter choice: ")
        if choice == "1":
            add_vendor(vendors)
        elif choice == "2":
            view_vendors(vendors)
        elif choice == "3":
            search_vendor(vendors)
        elif choice == "4":
            edit_vendor(vendors)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def purchase_order_menu():
    """Display purchase order menu."""
    while True:
        print("\n--- Purchase Order Menu ---")
        print("1. Create Purchase Order")
        print("2. View Purchase Orders")
        print("3. Receive Shipment")
        print("4. Back")

        choice = input("Enter choice: ")
        if choice == "1":
            create_purchase_order(purchase_orders, products, vendors)
        elif choice == "2":
            view_purchase_orders(purchase_orders)
        elif choice == "3":
            receive_shipment(purchase_orders, products)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def reports_menu():
    """Display reports menu."""
    while True:
        print("\n--- Reports Menu ---")
        print("1. Inventory Report")
        print("2. Low Stock Report")
        print("3. Inventory Value Report")
        print("4. Open Purchase Orders Report")
        print("5. Back")

        choice = input("Enter choice: ")
        if choice == "1":
            inventory_report(products)
        elif choice == "2":
            low_stock_report(products)
        elif choice == "3":
            inventory_value_report(products)
        elif choice == "4":
            open_purchase_orders_report(purchase_orders)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def main_menu():
    """Display main menu loop."""
    while True:
        print("\n=== Inventory & Purchase Order System ===")
        print("1. Product Management")
        print("2. Vendor Management")
        print("3. Purchase Orders")
        print("4. Reports")
        print("5. Save & Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            product_menu()
        elif choice == "2":
            vendor_menu()
        elif choice == "3":
            purchase_order_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            # Save all data before exiting
            save_products(PRODUCT_FILE, products)
            save_vendors(VENDOR_FILE, vendors)
            save_purchase_orders(PO_FILE, purchase_orders)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice.")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main_menu()