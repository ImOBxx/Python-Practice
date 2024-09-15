print()
cp = int (input ("Enter Cost Price of the Bike: "))
print()
if cp > 100000:
   t = (15 / 100) * cp
   print("Total Road Tax: ", t)
   print("Total Price Of Bike w/ Tax: ", t + cp)
   print()
elif cp <= 100000 and cp > 50000:
   t = (10 / 100) * cp
   print("Total Road Tax: ", t)
   print("Total Price Of Bike w/ Tax: ", t + cp)
   print()
elif cp <= 50000:
   t = (5 / 100) * cp
   print("Total Road Tax: ", t)
   print("Total Price Of Bike w/ Tax: ", t + cp)
   print()