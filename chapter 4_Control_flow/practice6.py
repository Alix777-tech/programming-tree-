# This program simulates a switch statement using a dictionary

# Assign a value to choice
choice = 2

# Create a dictionary to act like a switch
switch = {
    1: "Apple",
    2: "Banana",
    3: "Orange"
}

# Get the result based on the choice
result = switch.get(choice, "Invalid choice")

# Print the result
print(result)
