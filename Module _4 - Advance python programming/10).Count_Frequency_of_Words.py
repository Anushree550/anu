# 10). Write a Python program to count the frequency of words in a file.

count = 0

f = open("C:\\Users\\gohil\\OneDrive\\Documents\\GitHub\\Jay_Tops-Work\\Python_Language\\Assignments\\Module _4 - Advance python programming\\10).countFrequencyofwords.txt","r")

for line in f:
    word = line.split()
    count += len(word)

print("Total Number Of Words : ", count)