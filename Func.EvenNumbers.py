def evensep(s):
    x = []
    for i in s:
        if i % 2 == 0:
            x.append(i)
    print(x)



s = []
n = int (input ("Enter List Length: "))
for i in range(n):
    l = int (input ("Enter List Values: "))
    s.append(l)
evensep(s)

