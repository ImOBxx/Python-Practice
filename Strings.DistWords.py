s = "red, white, black, red, green, black"
x = s.split()
l = []
for i in x:
    if i not in l:
        l.append(i)
        l.sort()
d = ' ,'.join(l)
print(d)
