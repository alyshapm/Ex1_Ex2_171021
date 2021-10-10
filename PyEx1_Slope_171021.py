x1 = eval(input("Enter the x-coordinate for point1: "))
y1 = eval(input("Enter the y-coordinate for point1: "))
x2 = eval(input("Enter the x-coordinate for point2: "))
y2 = eval(input("Enter the y-coordinate for point2: "))

slope = (y2-y1)/(x2-x1)

print("The slope for the line that connects two points ({},{}) and ({},{}) is {:.5f}.".format(x1, y1, x2, y2, slope))