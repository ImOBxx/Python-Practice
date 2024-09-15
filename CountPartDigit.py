n = int (input ("Enter A Number: "))
x = int (input ("Enter Digit TO Search: "))

count = 0

temp = n
while temp > 0:
    rem = temp % 10
    if rem == x:
        count = count + 1
       
    temp = temp // 10

print ("The Number ", n, " has digit ", x, " times " , count)