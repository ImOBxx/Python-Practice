print()
a = int (input ("Enter Number 1: "))
print()
b = int (input ("Enter Number 2: "))
print()
c = int (input ("Enter Number 3: "))
print()
if (a > b and a < c or a < b and a > c):
    print ("A is the Second largest Number.")
    print()
elif (b > a and b < c or b < a and b > c):
    print("B is the Second Largest Number.")
    print()
elif (c > b and c < a or c < b and c > a):
    print ("C is the Second Largest Number.")
    print()