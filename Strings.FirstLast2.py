print()
s = input ("Enter String: ")
print()
x = (s[0:2])
y = (s[-2:])
print(x + y)
print()
if len(s) < 2:
    a = s[0:]
    print(a + a)
print()
if len(s) <= 1:
    print("Empty String.")
print()
