"""
1) Differentiate between append () and extend () methods ? 

A) Append : It can add single element in the form of  list.

B) Extend : It can add multiple element in the form of  list.

"""
# Append syntax :

l1 = []

for i in range(1,6):
    num = int(input("Enter the  number : "))
    l1.append(num)
    print(l1)

l1 = [25,13,45,9]

l1.append(56)
print(l1)


# Extend syntax :

l1 = []
l1.extend([1,2,3,4,56])

print(l1)