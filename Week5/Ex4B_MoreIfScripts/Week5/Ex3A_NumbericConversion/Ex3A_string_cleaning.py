# Lab 2 

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# 3. Use .lower() to convert all three names to lowercase, and print each result.
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# 4. Use .title() to convert all three names to title case (first letter of each word capitalized), and print each result. 
print(name_1.title())
print(name_2.title())
print(name_3.title())

# 5. Use .replace() to remove the $ from both salary strings, and print each result. Add another print statement to test what data type these values are now. 
# What would you need to do next to perform math on them?

#print(salary_1.replace("$", ""))
#print(salary_2.replace("$",""))

salary_1.replace("$", "")
salary_2.replace("$", "")

clean_salary_1 = salary_1.replace("$", "").replace(",", "")
clean_salary_2 = salary_2.replace("$", "").replace(",", "")

clean_salary_1 = int(clean_salary_1)
clean_salary_2 = int(clean_salary_2)
print (type(clean_salary_1))
print (type(clean_salary_2))

print (clean_salary_1 + clean_salary_2)