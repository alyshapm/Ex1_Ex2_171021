import math

s = eval(input("Enter the side of the hexagon: "))
a = (3 * math.sqrt(3)/2) * math.pow(s, 2)

print("The area of a hexagon with side length {} is {:.3f}.".format(s, a))
