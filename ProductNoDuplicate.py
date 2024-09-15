l = [2, 1, 2, 4, 6, 4, 3, 2, 1]
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
sum = 1
for i in x:
    sum = sum * i
print("Product Of List: ", sum)
