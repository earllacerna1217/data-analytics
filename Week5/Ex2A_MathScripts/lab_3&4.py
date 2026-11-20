# Lab 3 
# The input() function allows you to create a variable that asks for the user running the script to input a value. For example  

# Example: bank_bal = input("What is your current bank balance? ") 
# print("Your balance is " + bank_bal)

bank_bal = input("What is your bank balance? ")
print("Your balance is " + bank_bal)
if int(bank_bal) < 300:
    print("You're kinda broke")
elif int(bank_bal) > 1000:
     print("You're doing kind of okay")
elif int(bank_bal) > 4000:
    print("You're doing better than most")
elif int(bank_bal) > 6000:
     print("You're doing well for yourself")

# What possible pitfalls with using inpit() can you think of?  What happens if the user inputs a string instead of a number? 

#Lab 4 

# Define known values
# A str() function used is to convert a value to a string.
# it's being used here to convert the total_due value to a string.
food_cost = 79.25 
tax = 6.54
tip = 12.00

# Calculate total cost
total_due = food_cost + tax + tip
print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + "  and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))