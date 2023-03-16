# 9). Write a Python program to count the number of lines in a text file. 

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\9).CountNooflines.txt")

lines = len(f.readlines())

print("Total Number of lines : ", lines)