print()
u = int (input ("Enter Units Of Electrity: "))
print()
if u <= 100:
    print("Free Electricty") 
elif u > 100 and u <= 300:
    sum = (u - 100) * 2
    print ("Total Electricty Bill: ", sum)
elif u > 300:
    sum = ((u -100 - (200 * 2)) * 5)
    print("Total Electricity Bill: ", sum)
