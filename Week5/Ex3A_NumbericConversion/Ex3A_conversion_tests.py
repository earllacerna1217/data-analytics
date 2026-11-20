# Exercise 3A Conversion Tests
# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer


import string


a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# 3 For each variable above, perform the following transformations, creating a new variable for each.

# a = float(101.1)
b = int(55)
# c = int(402 Stevens)
# d = int(Number 5)

# 4 
print(a)
print(b)


# 5

a = float(101.1) # Casting A as a float
b = int(55) # Casting B as an Integer

print(int(float(a))) # Casting into a float then integer

new_c= int(c[0:3])
print(new_c) # d) Use slicing to add just the numeric portion of the string to a new variable (remember, indexing always starts with 0!),
        # and cast the number as an integer or string, whichever is appropriate

a = float(a) #e) For variables a and d, use the .strip() method to remove the leading/trailing spaces, within a print statement.
print(d.strip())
