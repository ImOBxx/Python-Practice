l = [1, 2, 4, 3, 6, 7, 5, 8, 9, 7, 8, 9, 10]
uniq = []
x = []
c = []
dup = set()
for i in l:
    if i not in dup:
        uniq.append(i)
        dup.add(i)
for y in dup:
    x.append(y)
for b in x:
    if b % 2 != 0:
        c.append(b)
print(c)

