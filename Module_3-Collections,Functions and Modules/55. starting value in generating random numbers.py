# 1). How will you set the starting value in generating random numbers ?

"""
# Definition and Usage :

                The seed() method is used to initialize the random number generator.

                    The random number generator needs a number to start with (a seed value), to be able to generate a random number.

""" 

# Example (1) :-

import random

random.seed(10)
print(random.random())


# Example (2) :- Note :-  If you use the same seed value twice you will get the same random number twice. See example below.

print("\n")
import random

random.seed(10)
print(random.random())

random.seed(5)
print(random.random())


# Example (3) :- Using For loop.

print("\n")
import random
for i in range(5):
 
    random.seed(0)
 
    print(random.randint(1, 1000)) 