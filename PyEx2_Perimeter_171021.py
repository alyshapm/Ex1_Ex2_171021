edge1 = eval(input("Enter length of edge1: "))
edge2 = eval(input("Enter length of edge2: "))
edge3 = eval(input("Enter length of edge3: "))

if edge1 + edge2 > edge3 and edge1 + edge3 > edge2 and edge3 + edge2 > edge1:
    print("The perimeter is {}".format(edge1 + edge2 + edge3))
else:
    print("Input is invalid and perimeter cannot be calculated")