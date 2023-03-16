# 6).Write a Python program to read a file line by line and store it into a list.

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\6).Readlinebyline.txt","r")

lines = f.readlines()
print(lines)


lines = [x.strip() for x in lines]
print(lines)