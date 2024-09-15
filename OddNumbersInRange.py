sum = 0
s = int (input ("Enter Starting Point: "))
e = int (input ("Enter Ending Point: "))
for i in range (s, e + 1):
    if (i % 2 != 0):
        print (i)
        sum = sum + i
print (sum)