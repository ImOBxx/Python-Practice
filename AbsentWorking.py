print()
a = int (input ("Enter Abentism Days: "))
w = int (input ("Enter Present Days: "))
print()
t = (w + a)
sum = (w - a)
per = (sum / t) * 100
print("Present Percentage: ", per)
if (per > 75):
    print ("The Student is permitted to sit in the exams.")
else:
    print ("The Student is not permitted to sit in the exams.")