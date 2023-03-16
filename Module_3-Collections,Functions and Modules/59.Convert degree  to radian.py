# Write a Python program to convert degree to radian ?

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)


# Example 2 :- Use math.pi and the degrees to radians formula to convert the angle from degrees to radians.

print("\n")

from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0

print(degrees_to_rads(180))
print(degrees_to_rads(90))

