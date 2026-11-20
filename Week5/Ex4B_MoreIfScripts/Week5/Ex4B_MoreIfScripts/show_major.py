
print(input("Student name: "))
student_name = input("Student name: ")
student_major = input("Major code: ").upper()

print(f"Student name: {student_name}")

if student_major == "BIOL":
    print("Major: Biology")
    print("Department office: Science Bldg, Room 310")

elif student_major == "CSCI":
    print("Major: Computer Science")
    print("Department office: Sheppard Hall, Room 314")

elif student_major == "ENG":
    print("Major: English")
    print("Department office: Kerr Hall, Room 201")

elif student_major == "HIST":
    print("Major: History")
    print("Department office: Kerr Hall, Room 114")

elif student_major == "MKT":
    print("Major: Marketing")
    print("Department office: Westly Hall, Room 310")

else:
    print("Invalid major code")
    



