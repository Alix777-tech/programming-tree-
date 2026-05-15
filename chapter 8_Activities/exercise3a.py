# Taking input from the user
name = input("Enter Student Name: ")
marks = float(input("Enter Marks (out of 100): "))

# Checking grade using if-elif-else
if marks > 100:
    print("Invalid Marks, Maximum marks are 100")
elif marks >= 90 and marks <= 100:
    print(f"{name}, your grade is A")
elif marks >= 80 and marks < 90:
    print(f"{name}, your grade is B")
elif marks >= 70 and marks < 80:
    print(f"{name}, your grade is C")
else:
    print(f"{name}, your grade is D")