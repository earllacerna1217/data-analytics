def display_mailing_label (name, address, city, state, zip):
    return f"{name}\n{address}\n{city}\n{state}\n{zip}"

name = "Earl"
address = "310 somewhere"
city = "San Francisco city"
state = "California"
zip = "99999"

name2 = "Lillianna"
address2 = "310 somewhereelse"
city2= "San Francisco city"
state2= "California"
zip2= "99999"

print(display_mailing_label(name, address, city, state, zip))
print(display_mailing_label(name2, address2, city2, state2,zip2))

def add_numbers (*numbers):
    result = sum(numbers)
    return result

print(add_numbers(20))
print(add_numbers(10,30))
print(add_numbers(20,40,60))


def display_receipt (total_due, amount_paid):
    change_due = amount_paid - total_due
 

    return f"Total due:{total_due: .2f}\nAmount Paid: ${amount_paid}\nChange Due: ${change_due: .2f}"

print(display_receipt(25,40))
print(display_receipt(63, 63))
print(display_receipt(25,19))