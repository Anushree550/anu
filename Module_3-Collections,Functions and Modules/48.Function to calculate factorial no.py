# 1). Write a Python function to calculate the factorial of a number (a nonnegative integer).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Input a number for factorial : "))
print(factorial(n))

"""
Example for understanding about factorial :

 n! = n* (n-1) * (n-2) *........1  
 4! = 4x3x2x1 = 24  
 
"""
# Example : 3 -

# Using built-in function
# ---->> We will use the math module, which provides the built-in factorial() method. Let's understand the following example.
print("\n")

import math 

def fact(n):  
    return(math.factorial(n))  
  
num = int(input("Enter the number:"))  
f = fact(num)  
print("Factorial of", num, "is : ", f)  