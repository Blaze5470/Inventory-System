"""
inventory_manager.py
Contains inventory management functions for Products, Vendors, and Purchase Orders
"""

from models import Product, Vendor, PurchaseOrder
from datetime import datetime

# ---------------- PRODUCT FUNCTIONS ----------------

def add_product(products, vendors):
    """Add a new product to inventory."""
    product_id = input("Enter product ID: ").strip()
    if any(p.product_id == product_id for p in products):
        print("Duplicate product ID. Cannot add.")
        return

    name = input("Enter product name: ").strip()
    category = input("Enter product category: ").strip()

    try:
        quantity = int(input("Enter quantity: "))
        reorder_level = int(input("Enter reorder level: "))
        reorder_quantity = int(input("Enter reorder quantity: "))
        unit_price = float(input("Enter unit price: "))
    except ValueError:
        print("Invalid number input.")
        return

    if not vendors:
        print("No vendors available. Add vendors first.")
        return

    vendor_id = input("Enter vendor ID: ").strip()
    if not any(v.vendor_id == vendor_id for v in vendors):
        print("Vendor not found.")
        return

    product = Product(product_id, name, category, quantity,
                      reorder_level, reorder_quantity, unit_price,
                      vendor_id)
    products.append(product)
    print(f"Product '{name}' added successfully.")


def view_products(products):
    """Display all products."""
    if not products:
        print("No products found.")
        return
    for product in products:
        product.display()


def search_product(products):
    """Search product by ID or Name."""
    query = input("Enter product ID or Name to search: ").strip()
    found = False
    for product in products:
        if query.lower() in product.product_id.lower() or query.lower() in product.name.lower():
            product.display()
            found = True
    if not found:
        print("No matching products found.")


def edit_product(products):
    """Edit product details."""
    product_id = input("Enter product ID to edit: ").strip()
    for product in products:
        if product.product_id == product_id:
            print("Leave blank to keep current value.")
            name = input(f"Name [{product.name}]: ").strip() or product.name
            category = input(f"Category [{product.category}]: ").strip() or product.category
            try:
                quantity = input(f"Quantity [{product.quantity}]: ").strip()
                quantity = int(quantity) if quantity else product.quantity
                reorder_level = input(f"Reorder Level [{product.reorder_level}]: ").strip()
                reorder_level = int(reorder_level) if reorder_level else product.reorder_level
                reorder_quantity = input(f"Reorder Quantity [{product.reorder_quantity}]: ").strip()
                reorder_quantity = int(reorder_quantity) if reorder_quantity else product.reorder_quantity
                unit_price = input(f"Unit Price [{product.unit_price}]: ").strip()
                unit_price = float(unit_price) if unit_price else product.unit_price
            except ValueError:
                print("Invalid number input.")
                return

            product.name = name
            product.category = category
            product.quantity = quantity
            product.reorder_level = reorder_level
            product.reorder_quantity = reorder_quantity
            product.unit_price = unit_price
            print("Product updated successfully.")
            return
    print("Product not found.")


def deactivate_product(products):
    """Deactivate a product."""
    product_id = input("Enter product ID to deactivate: ").strip()
    for product in products:
        if product.product_id == product_id:
            product.active = False
            print(f"Product '{product.name}' deactivated.")
            return
    print("Product not found.")


def display_low_stock(products):
    """Display products with quantity below reorder level."""
    low_stock_items = [p for p in products if p.quantity <= p.reorder_level]
    if not low_stock_items:
        print("No low stock products.")
        return
    for product in low_stock_items:
        product.display()


def sort_products(products):
    """Sort products by name, quantity, or price."""
    print("1. Sort by Name")
    print("2. Sort by Quantity")
    print("3. Sort by Unit Price")
    choice = input("Choose sort option: ").strip()
    if choice == "1":
        products.sort(key=lambda x: x.name.lower())
    elif choice == "2":
        products.sort(key=lambda x: x.quantity)
    elif choice == "3":
        products.sort(key=lambda x: x.unit_price)
    else:
        print("Invalid choice.")
        return
    print("Products sorted.")


# ---------------- VENDOR FUNCTIONS ----------------

def add_vendor(vendors):
    """Add a new vendor."""
    vendor_id = input("Enter vendor ID: ").strip()
    if any(v.vendor_id == vendor_id for v in vendors):
        print("Duplicate vendor ID.")
        return

    name = input("Enter vendor name: ").strip()
    contact = input("Enter contact name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    vendor = Vendor(vendor_id, name, contact, phone, email, address)
    vendors.append(vendor)
    print(f"Vendor '{name}' added successfully.")


def view_vendors(vendors):
    """Display all vendors."""
    if not vendors:
        print("No vendors found.")
        return
    for vendor in vendors:
        vendor.display()


def search_vendor(vendors):
    """Search vendor by ID or Name."""
    query = input("Enter vendor ID or Name to search: ").strip()
    found = False
    for vendor in vendors:
        if query.lower() in vendor.vendor_id.lower() or query.lower() in vendor.vendor_name.lower():
            vendor.display()
            found = True
    if not found:
        print("No matching vendors found.")


def edit_vendor(vendors):
    """Edit vendor details."""
    vendor_id = input("Enter vendor ID to edit: ").strip()
    for vendor in vendors:
        if vendor.vendor_id == vendor_id:
            print("Leave blank to keep current value.")
            vendor.vendor_name = input(f"Name [{vendor.vendor_name}]: ").strip() or vendor.vendor_name
            vendor.contact_name = input(f"Contact [{vendor.contact_name}]: ").strip() or vendor.contact_name
            vendor.phone = input(f"Phone [{vendor.phone}]: ").strip() or vendor.phone
            vendor.email = input(f"Email [{vendor.email}]: ").strip() or vendor.email
            vendor.address = input(f"Address [{vendor.address}]: ").strip() or vendor.address
            print("Vendor updated successfully.")
            return
    print("Vendor not found.")


# ---------------- PURCHASE ORDER FUNCTIONS ----------------

def create_purchase_order(purchase_orders, products, vendors):
    """Create a new purchase order."""
    if not vendors or not products:
        print("Vendors or products are missing. Add them first.")
        return

    po_number = input("Enter PO Number: ").strip()
    if any(po.po_number == po_number for po in purchase_orders):
        print("Duplicate PO number.")
        return

    vendor_id = input("Enter vendor ID: ").strip()
    if not any(v.vendor_id == vendor_id for v in vendors):
        print("Vendor not found.")
        return

    items_ordered = []
    while True:
        product_id = input("Enter product ID to order (or 'done' to finish): ").strip()
        if product_id.lower() == "done":
            break
        product = next((p for p in products if p.product_id == product_id), None)
        if not product:
            print("Product not found.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {product.name}: "))
        except ValueError:
            print("Invalid quantity.")
            continue
        items_ordered.append({
            "product_id": product.product_id,
            "product_name": product.name,
            "quantity": quantity,
            "unit_price": product.unit_price
        })

    if not items_ordered:
        print("No items added. PO canceled.")
        return

    po = PurchaseOrder(po_number, vendor_id, datetime.today().strftime("%Y-%m-%d"), items_ordered)
    po.calculate_total()
    purchase_orders.append(po)
    print(f"Purchase Order '{po_number}' created successfully.")


def view_purchase_orders(purchase_orders):
    """Display all purchase orders."""
    if not purchase_orders:
        print("No purchase orders found.")
        return
    for po in purchase_orders:
        po.display()


def receive_shipment(purchase_orders, products):
    """Mark PO as received and update inventory."""
    po_number = input("Enter PO Number to receive: ").strip()
    po = next((po for po in purchase_orders if po.po_number == po_number), None)
    if not po:
        print("PO not found.")
        return
    if po.status == "RECEIVED":
        print("PO has already been received.")
        return

    for item in po.items_ordered:
        product = next((p for p in products))