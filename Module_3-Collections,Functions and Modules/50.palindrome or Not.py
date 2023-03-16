# Write a Python function that checks whether a passed string is palindrome or not .



# Find reverse of string
# Check if reverse and original are same or not.

# function which return reverse of a string
 
def isPalindrome(str):
    return str == str[::-1]
 
str = "malayalam"
ans = isPalindrome(str)
 
if ans:
    print("Yes !")
else:
    print("No !")


# Example - 1:Palindrome string.

print("\n")
str = 'abababa'  
strstr = str.casefold()  
  
# This string is reverse.  
rev = reversed(str)  
  
if list(str) == list(rev):  
   print("PALINDROME !")  
else:  
   print("NOT PALINDROME !")  

# Example - 2: Palindrome string program.

print("\n")
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")  