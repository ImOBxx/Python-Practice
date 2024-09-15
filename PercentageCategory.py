print()
per = int (input ("Enter Percentage: "))
print("Your Percenatge: ", per, "%")
print()
if (per < 40):
    print("Category: Failed")
    print()
elif (per >= 40 and per < 55):
    print("Category: Fair")
    print()
elif (per >= 55 and per < 65):
    print("Category: Good")
    print()
elif (per >= 65):
    print("Category: Excellent")
    print()


