print()
km = int (input ("Enter Kilometers: "))
print()
if km < 10:
    sum = km * 11
    print ("Toll Bill: ", sum)
    print()
elif km >= 10 and km < 100:
    sum = ((km - 90) * 10) + ((km - 10) * 11)
    print ("Toll Bill: ", sum)
    print()
elif km > 100:
    sum = (((km - 10)) * 11) + ((km - 90) * 10) + (km * 9) 
    print ("Toll Bill: ", sum)
    print()