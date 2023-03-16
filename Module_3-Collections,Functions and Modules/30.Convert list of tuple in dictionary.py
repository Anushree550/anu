# 1). Write a Python program to convert a list of tuples into a dictionary. 

tuple = [(1,"Monday"),(2,"Tuesday"),(3,"Wednesday"),(4,"Thursday"),(4,"Friday"),(5,"Saturday"),(7,"Sunday")]
x = dict(tuple)
print(x)

# Second type of example :

print("\n")
list = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in list:
    d.setdefault(a, []).append(b)
print (d)