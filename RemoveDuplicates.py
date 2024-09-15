l = [1, 2, 3, 7, 2, 1, 5, 6, 4, 8, 5, 4]
uniq = []
x = set()
for i in l:
    if i not in x:
        uniq.append(i)
        x.add(i)
print(x)
