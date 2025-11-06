"""
Inventory Management System.

This module provides basic inventory management functionality including
adding items, removing items, checking quantities, and persisting data
to JSON files.
"""

import json
from datetime import datetime


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add an item to the inventory with proper validation."""
    if logs is None:
        logs = []

    # Validate inputs
    if not isinstance(item, str) or not item:
        print(f"Error: Invalid item name '{item}'")
        return logs

    if not isinstance(qty, int) or qty < 0:
        print(f"Error: Invalid quantity '{qty}' for item '{item}'")
        return logs

    stock_data[item] = stock_data.get(item, 0) + qty
    log_message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_message)
    return logs


def remove_item(stock_data, item, qty):
    """Remove an item from inventory with proper error handling."""
    try:
        if item not in stock_data:
            print(f"Warning: Item '{item}' not found in inventory")
            return

        if not isinstance(qty, int) or qty < 0:
            print(f"Error: Invalid quantity '{qty}'")
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        print(f"Error removing item: {e}")
    except TypeError as e:
        print(f"Error with quantity type: {e}")


def get_qty(stock_data, item):
    """Get the quantity of an item in inventory."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    stock_data = {}
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        msg = f"Warning: File '{file}' not found. Starting with empty."
        print(msg)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{file}'")
    return stock_data


def save_data(stock_data, file="inventory.json"):
    """Save inventory data to a JSON file using context manager."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
    except IOError as e:
        print(f"Error saving data: {e}")


def print_data(stock_data):
    """Print the current inventory report."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items below the specified threshold."""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system."""
    stock_data = {}
    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", 5)
    # The following would now show error messages:
    # add_item(stock_data, 123, "ten")  # invalid types - now caught
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)
    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")
    save_data(stock_data)
    # stock_data = load_data()  # Can load if needed
    print_data(stock_data)
    # eval() removed - security risk


if __name__ == "__main__":
    main()
