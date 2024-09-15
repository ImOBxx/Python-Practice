print ()

print ("Largest Number Of The Three:")

print ()
a = int (input ("Enter A: "))
print()
b = int (input ("Enter B: "))
print()
c = int (input ("Enter C: "))
print()
if a > b and a > c:
    print("A is the Greatest.")
    print()
elif b > a and b > c:
    print("B is the Greatest.")
    print()
elif c > a and c > b:
    print("C is the Greatest.")
    print()
elif a == b == c:
    print ("Numbers Are Equal.")
    print()
elif a == b > c:
    print("A & B are the Greatest.")
    print()
elif a == c > b:
    print("A & C are the Greatest.")
    print()
elif b == c > a:
    print("B & C are the Greatest.")
    print()


