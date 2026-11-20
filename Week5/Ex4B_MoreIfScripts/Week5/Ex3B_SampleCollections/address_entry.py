
# Lab 3 
# Create a file named address_entry.py, and in it define a dictionary named contact_info
# that includes the following keys and the sample values of your choice:

contact_info = {
    "name": "Earl Lacerna",
    "phone": "123-456-7890",
    "email": "earllacerna@example.com",
    "address": "123 Flood Avenue, Anytown, USA"
}

# Print the address as properly formatted for mailing. Avoid using multiple print
# statements. Experiment with using a multi-line f-string (triple quotes), or use "\n" (new
# line) to break the address into multiple lines.

print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['phone']}\n{contact_info['email']}")
print(f"{contact_info}\n")

#  Remove the key:value pair for name
del contact_info["name"]
print(contact_info)

# Add a new variable for full_name and assign its value as a dictionary containing two
# key:value pairs. The first key:value pair should contain the key “first name” and a first
# name, and the second should contain the key “last name” and a last name.

add_contact_info = {"full_name": {"first_name": "Earl", "last_name": "Lacerna"}}

# Use the .update() method to add one more key:value pair to full_name, with the key
# “honorific” and the value set to Mr. / Ms. / Mx. / Dr. / Hon. / etc. as appropriate.
add_contact_info["full_name"].update({"honorific": "Mr."})
contact_info.update(add_contact_info)
print(contact_info)

honorific = contact_info["full_name"]["honorific"]
print(honorific)

# Use the .update() method to add full_name to contact_info.
contact_info.update(add_contact_info)
print(contact_info)