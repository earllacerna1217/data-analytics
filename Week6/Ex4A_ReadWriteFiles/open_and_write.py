#with open("about_me.txt", "x") as file:
    #file.write("Appending the file that's empty")

file = open("about_me.txt", "w")
file.write("Name: Earl Lacerna")
file.write("Place of birth: Philippines")
file.write("Did I have pets growing up? I did have a cat first then dog, then turtle for a little bit then a bunny then a few spiders")
file.write("If you could live anywhere in the world for a year, where would you want to live? I would love to live in the Portland for a year")
file.close()

file = open("about_me.txt", "r")
#print(file.read())
file.close()

file = open("about_me.txt", "w")
file.write("Name: Earl Lacerna\n")
file.write("Place of birth: Philippines\n")
file.write("Did I have pets growing up? I did have a cat first then dog, then turtle for a little bit then a bunny then a few spiders\n")
file.write("If you could live anywhere in the world for a year, where would you want to live? I would love to live in the Portland for a year\n")
file.close()

file = open("about_me.txt", "r")
#print(file.read(50))
file.close()

file = open("about_me.txt", "r")
#print(file.readlines(50)) 

lines = []
line = file.readline()

while line != "":
    lines.append(line)
    line = file.readline()

file.close()

print(lines)