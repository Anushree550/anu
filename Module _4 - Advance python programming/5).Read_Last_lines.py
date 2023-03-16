# 5). Write a Python program to read last n lines of a file. 

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\5).Readlastline.txt","r")

lines = f.read().splitlines()

print(lines)
print(lines[-1])