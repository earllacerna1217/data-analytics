# Lab 3 

# Create a script named complex_taxes.py that will calculate federal tax based on the values of annual gross income (a number) and a filing status (‘single’ or ‘joint’).
# This script calculates federal tax based on annual gross income and filing status.
pay_rate = 20
hours_worked = 45
Annual_gross_income = (40 * pay_rate) * 52

Filing_status = input("Enter your filing status (single or joint): ").strip().lower()

if Filing_status == "single":
    tax_rate = 0.10
elif Filing_status == "joint":
    tax_rate = 0.05
else:
    tax_rate = 0


# Pay calculation based on hours worked and pay rate

if hours_worked > 40:
    gross_pay = hours_worked * pay_rate * 1.5
elif hours_worked <= 40:
    gross_pay = hours_worked * pay_rate
Federal_tax = gross_pay * tax_rate
print("Federal tax is: " + f"{Federal_tax:.2f}")

# Federal tax calculation based on annual gross income and filing status
if Filing_status == "single" and Annual_gross_income < 12000:
    tax_rate = 0.05
elif Filing_status == "single" and 12000 <= Annual_gross_income <= 24999:
    tax_rate = 0.10
elif Filing_status == "single" and 25000 <= Annual_gross_income <= 74999:
    tax_rate = 0.15
elif Filing_status == "single" and Annual_gross_income >= 75000:
    tax_rate = 0.20
elif Filing_status == "joint" and Annual_gross_income < 12000:
    tax_rate = 0.0
elif Filing_status == "joint" and 12000 <= Annual_gross_income <= 24999:
    tax_rate = 0.06
elif Filing_status == "joint" and 25000 <= Annual_gross_income <= 74999:
    tax_rate = 0.11
elif Filing_status == "joint" and Annual_gross_income >= 75000:
    tax_rate = 0.20




print("You worked " + str(hours_worked) + " hours this period. Because you earn $" + str(pay_rate) + "per hour, your gross pay is: " + f"{gross_pay:.2f}")
print("Your filing status is: " + Filing_status)
print("Your tax withholding for the week is $: " + f"{Federal_tax:.2f}")
print("Your net pay for the week is: " + f"{gross_pay - Federal_tax:.2f}")