"""

29) Write a Python program to unzip a list of tuples into individual lists. 

"""

l1 = [('jay','gohil'),('jay','gohil'),('jay','gohil'),('jay','gohil')]

data = list(zip(*l1))

print(data)