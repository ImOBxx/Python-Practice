def find(a, b, c):
    if a > b and a > c:
        print("A is The Greatest.")
    elif b > a and b > c:
        print("B is The Greatest.")
    elif c > a and c > b:
        print("C is The Greatest.")

print()
a = int (input ("Enter A: "))
b = int (input ("Enter B: "))
c = int (input ("Enter C: "))
find(a, b, c)
