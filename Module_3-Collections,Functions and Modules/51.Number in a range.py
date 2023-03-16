# Write a Python function to check whether a number is in a given range.

def test_range(n):
    if n in range(3,9):
        print( "The number is in the range",(n))
    else :
        print("The number is outside the given range.")

test_range(5)


# Second type of Example :

print("\n")
def range(a,b,n):
    if a <= n <= b:
            print(n,"is within the range",a,"-",b)
    else:
            print(n, "is not within the range", a,"-",b)

range(2,8,300)
