print()
x = {}
l = []
for i in range(0,3):
    a = input ("Enter Name: ")
    b = int (input ("Enter Number: "))
    x[a] = b
print()
print(x)
print()

for i in x:
    print(i, ":", x[i])
print()

print("List Of Names With Distinction")
for i in x:
    if (x[i] >= 90):
        print("Name: ", i)
        print("Marks: ", x[i])
        l.append(i)
print(l)
print()    







