def multList(x):
    sum = 1
    for i in x:
        sum *= i
    print("Product Of List: ", sum)

x = []
n = int (input ("Enter List Length: "))
for i in range(n):
    l = int (input ("Enter List Values: "))
    x.append(l)
    
multList(x)
