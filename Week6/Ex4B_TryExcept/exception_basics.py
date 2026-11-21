# Exception basics

try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")    
else:
    print(m)
finally:
    print("Let's try another one...")        