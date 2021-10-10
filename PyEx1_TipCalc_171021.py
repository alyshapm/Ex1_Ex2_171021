subtotal = eval(input("Enter the subtotal: $"))
tip = eval(input("Enter tip amount, in %: "))/100

tip_total = subtotal * tip
total = tip_total + subtotal

print("Subtotal = ${:,.2f}".format(subtotal))
print("Tip = ${:,.2f}".format(tip_total))
print("Total = ${:,.2f}".format(total))