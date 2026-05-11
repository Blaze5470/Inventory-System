"""
models.py
Contains all class definitions for Inventory System
"""

# ---------------- PRODUCT CLASS ----------------

class Product:
    """Represents a product in inventory."""

    def __init__(self, product_id, name, category,
                 quantity, reorder_level,
                 reorder_quantity, unit_price,
                 vendor_id, active=True):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.unit_price = unit_price
        self.vendor_id = vendor_id
        self.active = active

    def display(self):
        """Display product information."""
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.unit_price:.2f}")
        print(f"Vendor ID: {self.vendor_id}")
        print(f"Active: {self.active}")
        print("-" * 40)

    def to_dict(self):
        """Convert product to dictionary."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "reorder_level": self.reorder_level,
            "reorder_quantity": self.reorder_quantity,
            "unit_price": self.unit_price,
            "vendor_id": self.vendor_id,
            "active": self.active
        }

    @classmethod
    def from_dict(cls, data):
        """Create Product from dictionary."""
        return cls(**data)


# ---------------- VENDOR CLASS ----------------

class Vendor:
    """Represents a vendor."""

    def __init__(self, vendor_id, vendor_name,
                 contact_name, phone,
                 email, address):
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.contact_name = contact_name
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        """Display vendor information."""
        print(f"Vendor ID: {self.vendor_id}")
        print(f"Vendor Name: {self.vendor_name}")
        print(f"Contact: {self.contact_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print("-" * 40)

    def to_dict(self):
        """Convert vendor to dictionary."""
        return {
            "vendor_id": self.vendor_id,
            "vendor_name": self.vendor_name,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @classmethod
    def from_dict(cls, data):
        """Create Vendor from dictionary."""
        return cls(**data)


# ---------------- PURCHASE ORDER CLASS ----------------

class PurchaseOrder:
    """Represents a purchase order."""

    def __init__(self, po_number, vendor_id, date_created, items_ordered, status="OPEN"):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.date_created = date_created
        self.items_ordered = items_ordered  # list of dicts: {product_id, product_name, quantity, unit_price}
        self.total_cost = 0
        self.status = status

    def calculate_total(self):
        """Calculate total cost from items_ordered."""
        self.total_cost = sum(item["quantity"] * item["unit_price"] for item in self.items_ordered)

    def mark_received(self):
        """Mark the PO as received."""
        self.status = "RECEIVED"

    def display(self):
        """Display purchase order details."""
        print(f"\nPO Number: {self.po_number}")
        print(f"Vendor ID: {self.vendor_id}")
        print(f"Date Created: {self.date_created}")
        print(f"Status: {self.status}")
        print("Items Ordered:")
        for item in self.items_ordered:
            print(
                f"  Product ID: {item['product_id']}, "
                f"Name: {item['product_name']}, "
                f"Quantity: {item['quantity']}, "
                f"Unit Price: ${item['unit_price']:.2f}, "
                f"Subtotal: ${item['quantity']*item['unit_price']:.2f}"
            )
        print(f"Total Cost: ${self.total_cost:.2f}")
        print("-" * 40)

    def to_dict(self):
        """Convert PO to dictionary for JSON saving."""
        return {
            "po_number": self.po_number,
            "vendor_id": self.vendor_id,
            "date_created": self.date_created,
            "items_ordered": self.items_ordered,
            "total_cost": self.total_cost,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Create PurchaseOrder from dictionary."""
        return cls(
            data["po_number"],
            data["vendor_id"],
            data["date_created"],
            data["items_ordered"],
            data.get("status", "OPEN")
        )