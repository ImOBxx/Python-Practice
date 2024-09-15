print()
n1 = int (input ("Enter Triangle Side 1: "))
n2 = int (input ("Enter Triangle Side 2: "))
n3 = int (input ("Enter Triangle Side 3: "))
print()
if (n1 == n2 == n3):
    print ("The Triangle Is An Equilateral Triangle.")
    print()
elif (n1 != n2 != n3):
    print ("The Triangle Is An Scalene Triangle.")
    print()
elif (n1 == n2 or n2 == n3 or n3 == n1):
    print ("The Triangle Is An Isoceles Triangle.")
    print()