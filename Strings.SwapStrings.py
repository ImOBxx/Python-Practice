"""print()
s = input("Enter String: ")
x = s.split()
a = x[0]
b = x[1]
c = list(a)
e = list(b)
for i in c:
    f = a.replace(c[0], b[0])

    

for j in e:
    g = b.replace(b[0], c[0])
    


print(f + " " + g)"""

a = input("Enter String 1: ")
b = input("Enter String 2: ")
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a + new_b)


