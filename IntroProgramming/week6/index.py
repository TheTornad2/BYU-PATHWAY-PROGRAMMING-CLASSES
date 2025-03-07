"""
 Shopping Cart Program
 Description: This program allows users to manage a shopping cart by adding and removing items, viewing the cart with prices, computing totals, and displaying items with a 1-based index.
 Creative addition: Added item quantities to allow users to add more than one of the same item and display subtotal for each item type.
"""

# Initialize lists to store items, prices, and quantities
cart_items = []
cart_prices = []
cart_quantities = []


# Menu display function
def display_menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")


# Function to add items with price and quantity
def add_item():
    item_name = input(
        "-------------------------What item would you like to add?------------------------- \n "
    )
    item_price = float(input(f"What is the price of '{item_name}'? "))
    quantity = int(input(f"How many '{item_name}' would you like to add? "))

    cart_items.append(item_name)
    cart_prices.append(item_price)
    cart_quantities.append(quantity)

    print(
        f"{quantity} of '{item_name}' at ${item_price:.2f} each has been added to the cart."
    )


# Function to display cart contents with index and subtotal for each item type
def view_cart():
    print("\nThe contents of the shopping cart are:")
    for i, (item, price, quantity) in enumerate(
        zip(cart_items, cart_prices, cart_quantities), start=1
    ):
        subtotal = price * quantity
        print(f"{i}. {item} - ${price:.2f} x {quantity} = ${subtotal:.2f}")


# Function to remove items by index
def remove_item():
    view_cart()
    index = (
        int(
            input(
                "-------------------------Which item would you like to remove?------------------------- \n "
            )
        )
        - 1
    )  # Convert to 0-based index

    if 0 <= index < len(cart_items):
        removed_item = cart_items.pop(index)
        removed_price = cart_prices.pop(index)
        removed_quantity = cart_quantities.pop(index)
        print(f"Removed {removed_quantity} of '{removed_item}' from the cart.")
    else:
        print("Sorry, that is not a valid item number.")


# Function to compute and display total
def compute_total():
    total = sum(
        price * quantity for price, quantity in zip(cart_prices, cart_quantities)
    )
    print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")


# Main loop to interact with the user
def main():
    print(
        "-------------------------Welcome to the Shopping Cart Program!------------------------- \n"
    )
    while True:
        display_menu()
        choice = input("Please enter an action: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            compute_total()
        elif choice == "5":
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


main()
