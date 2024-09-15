print()
print("~ FLAT OFF ~")
print()
mp = int (input ("Enter Marked Price: "))
print()
if (mp > 10000):
    dp = (20 / 100) * mp
    print("Total Discount Applied: ", 20, "%")
    print ("Total Discount: ", dp)
    print()
    tp = dp + mp
    print("Total Price Of The Product: ", tp)
    print()
elif (mp > 7000 and mp <= 10000):
    dp = (15 / 100) * mp
    print("Total Discount Applied: ", 15, "%")
    print ("Total Discount: ", dp)
    print()
    tp = dp + mp
    print("Total Price Of The Product: ", tp)
    print()
elif (mp <= 7000):
    dp = (10 / 100) * mp
    print("Total Discount Applied: ", 10, "%")
    print ("Total Discount: ", dp)
    print()
    tp = dp + mp
    print("Total Price Of The Product: ", tp)
    print()
    