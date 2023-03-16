# 1). Write a Python function that takes two lists and returns true if they have at least one common member. 

list1=[1,3,5,7]
list2=[1,9,0,6]
result = 0
def find_common(list1, list2):
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
             else:
               result = False
               return result

print(find_common(list1, list2))


# Second type example for Return True values.

"""

def common_data(list1, list2):
    result = False
  
    
    for x in list1:
        for y in list2:
    
            if x == y:
                result = True
                return result 
                  
    return result
      
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))
  
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))

"""
