# 12). Write a Python program to copy the contents of a file to another file.

f1 = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\12).file.txt","r")
f2 = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\12).file1.txt","w")

for line in f1:
    f2.write(line)  