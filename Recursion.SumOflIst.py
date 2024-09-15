def sumup(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sumup(l[1:])
    
l = []
for i in range(1, 6):
    print()
    x = int (input ("Enter Number: "))
    l.append(x)
print()
print("Sum: ", sumup(l))
print()
