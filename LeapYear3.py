print()
y = int (input ("Enter The Year: "))
print()
if y % 100 == 0 and y % 400 == 0 and y % 4 == 0:
        print ("Entered Year is a leap year.")
        print()
else:
        print ("Entered Year is not a leap year.")
        print()

