def checkLeapYear (year) :
    import calendar
    return (calendar.isleap(year))
year = int (input ("Enter the year: "))
if (checkLeapYear(year)) :
    print (year, "is a Leap Year.")
else :
    print (year, "Not a Leap Year.")