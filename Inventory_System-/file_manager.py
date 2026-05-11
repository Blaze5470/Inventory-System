"""
file_manager.py
Functions to save and load products, vendors, and purchase orders.
"""

import json
from models import Product, Vendor, PurchaseOrder

# ---------------- PRODUCTS ----------------

def load_products(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return [Product.from_dict(d) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_products(filename, products):
    with open(filename, "w") as f:
        json.dump([p.to_dict() for p in products], f, indent=4)

# ---------------- VENDORS ----------------

def load_vendors(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return [Vendor.from_dict(d) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_vendors(filename, vendors):
    with open(filename, "w") as f:
        json.dump([v.to_dict() for v in vendors], f, indent=4)

# ---------------- PURCHASE ORDERS ----------------

def load_purchase_orders(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return [PurchaseOrder.from_dict(d) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_purchase_orders(filename, purchase_orders):
    with open(filename, "w") as f:
        json.dump([po.to_dict() for po in purchase_orders], f, indent=4)