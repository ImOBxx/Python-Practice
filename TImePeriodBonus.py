print()
t = int (input ("Time Of Service: "))
s = int (input ("Input Salary: "))
print()
if t > 10:
    b = (10 / 100) * s
    print ("Bonus: ", b)
    ts = b + s
    print ("Total Salary with Bonus Renumeration: ", ts)
    print()
elif (t >= 6 and t <= 10):
    b = (8 / 100) * s
    print ("Bonus: ", b)
    ts = b + s
    print ("Total Salary with Bonus Renumeration: ", ts)
    print()
else:
    b = (5 / 100) * s
    print ("Bonus: ", b)
    ts = b + s
    print ("Total Salary with Bonus Renumeration: ", ts)
    print()