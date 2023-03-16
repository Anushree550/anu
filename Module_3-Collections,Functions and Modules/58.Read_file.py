"""
58) Write a Python program to read a random line from a file. 

"""

import random

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module_3-Collections,Functions and Modules\\Read.txt",'r')

lines = f.read().splitlines() 

print(lines)
print(lines[0])

print(random.choice(lines))