print()
per = int (input ("Enter Percentage: "))
print ()
print("Your Percentage: ", per,"%")
if (per < 25):
    print ("Grade: D")
elif (per >= 25 and per < 45):
    print("Grade: C")
elif (per >= 45 and per < 50):
    print("Grade: B")
elif (per >= 50 and per < 60):
    print("Grade: B+")
elif (per >= 60 and per < 80):
    print("Grade: A")
elif (per >= 80):
    print("Grade: A+")