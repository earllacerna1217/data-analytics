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

