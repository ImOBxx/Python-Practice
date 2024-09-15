n = int (input ("Enter Number: "))
k = 0
if n == 0 and n == 1:
    k = 1
    for i in range(2, n):
     if n % i== 0:
        k = 1
    if k == 1:
        print("Number is not Prime")
    else:
        print("Number is Prime")