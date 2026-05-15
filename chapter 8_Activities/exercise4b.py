def find_square(num):
    square = num * num
    return square

number = float(input("Enter a number: "))

result = find_square(number)

print("The square of the number is:", result)