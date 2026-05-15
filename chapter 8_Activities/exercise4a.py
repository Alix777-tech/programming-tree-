def check_number(num):
    if num > 0:
        print("The number is greater than zero.")
    elif num < 0:
        print("The number is less than zero.")
    else:
        print("The number is equal to zero.")

number = float(input("Enter a number: "))

check_number(number)