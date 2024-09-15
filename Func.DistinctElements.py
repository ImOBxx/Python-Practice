def distinct(x):
    s = []
    for i in x:
        if i not in s:
            s.append(i)
    print(s)


x = []
n = int (input ("Enter List Length: "))
for i in range(n):
    l = int (input ("Enter List Values: "))
    x.append(l)
distinct(x)

