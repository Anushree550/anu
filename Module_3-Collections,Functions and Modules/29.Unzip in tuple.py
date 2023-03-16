# 1). Write a Python program to unzip a list of tuples into individual lists. 

# Create a tuple :

l1 = [(1,2), (3,4), (9,8)]

print(list(zip(*l1)))