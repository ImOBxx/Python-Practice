
print()
days = int (input ("Enter Number Of Days: "))
print()
if days < 5:
    sum = days * 2
    print("The Library Charge: ", sum, "$")
    print()
elif days >= 5 and days < 10:
    sum = (days * 3) + (days * 2)
    print("The Library Charge: ", sum, "$")
    print()
elif days >= 10 and days < 15:
    sum = (days * 4) + (days * 3) + (days * 2)
    print("The Library Chrage: ", sum, "$")
    print()
elif days >= 15:
    sum = (days * 5) + (days * 4) + (days * 3) + (days * 2)
    print("The Library Chrage: ", sum, "$")
    print()
