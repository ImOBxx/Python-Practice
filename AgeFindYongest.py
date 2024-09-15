print()
print("Youngest Age Finder: ")
print()
a = int (input("Enter Age 1: "))
print()
b = int (input("Enter Age 2: "))
print()
c = int (input("Enter Age 3: "))
print()
d = int (input("Enter Age 4: "))
print()
if a < b and a < c and a < d:
    print ("1 is the Youngest")
elif b < a and b < c and b < d:
    print ("2 is the Youngest")
elif c < a and c < b and c < d:
    print ("3 is the Youngest")
elif d < a and d < b and d < c:
    print ("4 is the Youngest")
elif a == b == c == d:
    print("Ages are equivalent.")
elif a == b > c == d:
    print("3 & 4 are the Youngest")
elif c == d > a == b:
    print("1 & 2 are the Youngest")
elif a == b == c > d:
    print("4 is the Youngest")
elif b == c == d > a:
    print("1 is the Youngest")
elif c == d == a > b:
    print("2 is the Youngest")
elif a == b == d > c:
    print("3 is the Youngest")

