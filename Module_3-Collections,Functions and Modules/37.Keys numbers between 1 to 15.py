# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

d=dict()
for x in range(1,16):
    d[x]=x**2
print(d) 


# Second example : Accept values from user.

print("\n")
num = int(input("Input a number : "))
d = dict()

for x in range(1,num+1):
    d[x]=x*x

print(d) 

# 1 and 2 are combined here :

print("\n")
l=int(input("Enter the Limit : "))
d = dict()
for x in range(1,l+1):
    d[x]=x**2
print(d)