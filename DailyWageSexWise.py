print()
age = int (input ("Enter Age Between 18 & 40: "))
sex = str (input ("Enter Sex (M / F): "))
day = int (input ("Enter Days Worked: "))
print()
if (age >= 18 and age <30):
    if sex == 'M' or 'm':
        tw = 700 * day
        print ("Total Wage: ", tw)
        print()
    elif sex == 'F' or 'f':
        tw = 750 * day
        print ("Total Wage: ", tw)
        print()
elif (age >= 30 and age <= 40):
    if sex == 'M' or 'm':
        tw = 800 * day
        print ("Total Wage: ", tw)
        print()
    elif sex == 'F' or 'f':
        tw = 850 * day
        print("Total Wage: ", tw)
        print()
elif (age < 18 or age > 40):
    print ("Enter Appropriate Age.")