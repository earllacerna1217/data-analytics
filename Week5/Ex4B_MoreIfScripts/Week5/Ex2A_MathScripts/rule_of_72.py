# How long will it take a savings account worth X to double in value based on  an interest rate of IR? (Hint: Look up the "rule of 72")

# a) Figure out the formula and what the script would look like, making up example values as needed

# Core formula to double the value using the the rule of 72: Years to double: Year = 72/Annual rate of return
# Required Rate of Return: Rate = 72/ Years to double

savings = 7000
interest_rate = .12
years_to_double = 72 / (interest_rate * 100)
savings_after_dobuling = savings * 2

print(f"our current savings is {savings}. At a {interest_rate * 100} interest rate, your savings account"
      f" will be worth {savings * 2} in {years_to_double} years")


# Show your doubled balance with 2 digits to the right of the decimal point by using format(__, ".2f") and show years with 1 digit to the right of the decimal.
#  How can you do this using format()? I did change it into 1 digit for show years by changing the data type from float to int. 

print(format(savings_after_dobuling, ",.2f")) 
print(int(years_to_double))
print(format(interest_rate, ".0%"))

