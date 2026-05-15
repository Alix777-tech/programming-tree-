# Simple Vending Machine Program

# Dictionary storing items and prices
items = {
    "chips": 5,
    "soda": 4,
    "chocolate": 7,
    "water": 2
}

# Welcome message
print("Welcome to the Vending Machine!")
print("--------------------------------")

# Show available items
print("Available Items:")

for item, price in items.items():
    print(item.capitalize(), "-", price, "AED")

print("--------------------------------")

# Take user input and convert it to lowercase
choice = input("Enter the item you want to buy: ").lower()

# Check if item exists
if choice in items:

    # Ask for money
    money = int(input("Insert your money (AED): "))

    # Get item price
    price = items[choice]

    # Check payment
    if money >= price:

        # Calculate change
        change = money - price

        print("Processing your order...")
        print("Dispensing", choice.capitalize())
        print("Your change is:", change, "AED")
        print("Thank you for using the vending machine!")

    else:
        print("Not enough money!")
        print("Please insert at least", price, "AED")

else:
    print("Item not available!")
    