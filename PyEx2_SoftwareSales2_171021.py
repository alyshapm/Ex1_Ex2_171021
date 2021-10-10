pack = int(input("Enter the number of packages purchased: "))

if pack < 10:
    discount = 0
elif pack < 20:
    discount = 10
elif pack < 50:
    discount = 20
elif pack < 100:
    discount = 30
else:
    discount = 40
    
price = 99
subtotal = pack * price
discountAmount = pack * price * discount/100
grandTotal = subtotal - discountAmount

print("Discount amount @ {}% = ${:,.2f}".format(discount, discountAmount))
print("Total amount:${:,.2f}".format(grandTotal))