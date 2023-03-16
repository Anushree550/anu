# 1). Write a Python script to check if a given key already exists in a dictionary.

"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

"""
# Second type of example :

"""

def checkKey(dic, key):
     
    if key in dic:
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")
 
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
 
key = 'w'
checkKey(dic, key)

"""
# Third type of example :
"""

dict = {'Mon':3,'Tue':5,'Wed':6,'Thu':9}
print("The given dictionary is : ",dict)
check_key = "Tue"
if check_key in dict:
   print(check_key,"is Present.")
else:
   print(check_key, " is not Present.")

"""
# Fourth type of example :

my_dict = {1: 'a', 2: 'b', 3: 'c'}

if 2 in my_dict:
    print("Key is present")
else:
    print("Not Present")