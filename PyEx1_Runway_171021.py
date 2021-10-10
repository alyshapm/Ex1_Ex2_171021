v = eval(input("Enter plane's take off speed in m/s: "))
a = eval(input("Enter plane's acceleration in m/s**2: "))
l = (v**2)/(2*a)

print("The minimum runway length needed for this airplane is {:.4f} meters.".format(l))