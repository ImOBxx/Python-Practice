l = [1, 2, 4, 5, 6, 7, 8, 4, 9, 2, 3, 7, 5, 4]
uniq = []
x = []
dup = set()
for i in l:
    if i not in dup:
        uniq.append(i)
        dup.add(i)
for i in dup:
    x.append(i)
print(x)


