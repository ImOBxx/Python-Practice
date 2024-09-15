print()
a = int (input ("Enter Side A: "))
print()
b = int (input ("Enter Side B: "))
print()
c = int (input ("Enter Side C: "))
print()
if (a + b > c and b + c > a and c + a > b):
    print("The Triangle is Possible.")
    print()
else:
    print("Triangle Not Posiible.")
    print()