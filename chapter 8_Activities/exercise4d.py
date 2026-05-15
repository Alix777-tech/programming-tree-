def calculate_gross_pay(hours_worked, hourly_rate):
    gross_pay = hours_worked * hourly_rate
    return gross_pay

hours1 = float(input("Enter hours worked for Employee 1: "))
rate1 = float(input("Enter hourly pay rate for Employee 1: "))

hours2 = float(input("Enter hours worked for Employee 2: "))
rate2 = float(input("Enter hourly pay rate for Employee 2: "))

gross1 = calculate_gross_pay(hours1, rate1)
gross2 = calculate_gross_pay(hours2, rate2)

print("Gross pay of Employee 1 is:", gross1)
print("Gross pay of Employee 2 is:", gross2)

print()