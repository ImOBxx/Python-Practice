def checkLeapYear (year) :
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 != 0 :
            return True
        else:
            return False;
year = int (input("Enter the year: "))
if (checkLeapYear(year)):
    print (year, "Leap Year")
else:
    print (year, "Is not a Leap Year")