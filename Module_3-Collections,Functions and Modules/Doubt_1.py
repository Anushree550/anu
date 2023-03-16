"""
6) Write a Python program to count the number of strings where the string length is 2 or more and 
                            the first and last character are same from a given list of strings.

"""

# find length of string :

data = "Android"
print(len(data))

# find first character :
print(data[0])

# find last character :
print(data[-1])

# Solution :

l1 = ["Android",'red','blue','aba','aea','1221']

count = 0

for word in l1:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1
        
print(l1)
print("Ans = ",count)
