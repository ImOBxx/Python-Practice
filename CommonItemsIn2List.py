l1 = [23, 45, 67, 78, 89, 34]
l2 = [34, 89, 55, 56, 39, 67]
dup = set()
for i in l1:
    for j in l2:
        if i == j:
            dup.add(j)
print(dup)
