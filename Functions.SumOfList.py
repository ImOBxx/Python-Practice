def listsum(x):
    sum = 0
    for i in x:
        sum = sum + i
    print("Sum Of List: ", sum)
print()
x = []
n = int (input ("Enter List Length: "))
print()
for i in range(n):
    l = int (input ("Enter List Values: "))
    print()
    x.append(l)
listsum(x)