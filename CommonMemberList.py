l1 = [1, 2, 3, 4, 5]
l3 = [5, 6, 7, 8, 9]
result = False

for x in l1:
    for y in l3:
        if x == y:
            res = True
            print(result)
if result:
    print("List has one common Member.")
else:
    print("List doesn't have any common member.")