import math

m = float(input("Enter mass of cart (in kg): "))
F = float(input("Enter the force to push the cart (in N): "))

g = 9.8
angle = math.asin(F/(m*g))
angle_convert = math.degrees(angle)

print("The angle of the ramp is {:.1f} degrees.".format(angle_convert))
