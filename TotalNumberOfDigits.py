n = int (input ("Enter Number: "))
sum = 0
count = 0
while (n > 0):
    r = n % 10
    count = count + 1
    n = n // 10
print ("Count Of Digits: ", count)

