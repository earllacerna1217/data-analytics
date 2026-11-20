# Exercise 4A Using conditionals
# Lab 2 

#In a file named pay_rules.py, create a script to calculate gross pay given the variables
# pay_rate and hours_worked. If the person works more than 40 hours, pay the
# overtime hours at 1.5 times the rate of regular hours.

pay_rate = 20
hours_worked = 45

if hours_worked > 40:
    gross_pay = hours_worked * pay_rate * 1.5
else:
    gross_pay = hours_worked * pay_rate
print("Gross pay is: " + f"{gross_pay:.2f}")