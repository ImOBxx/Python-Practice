print()
s = input ("Enter String: ")
print()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print()
print(d) 
print()