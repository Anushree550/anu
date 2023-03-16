# 3). Write a Python program to append text to a file and display the text.

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\3).Myfile1.txt","a")

name = input("Enter Anything Here : ")
f.write("\n"+name)

f.close()