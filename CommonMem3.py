l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8, 9]
res = False
for x in l1:
    for y in l2:
        if x == y:
            res = True
            if res == True:
                print("There is one common member")
            else:
                print("there is no common member")

