x = int (input ("Enter Number: "))
temp = x
count = 0
while temp > 0:
    temp = temp // 10
    count = count + 1

print ("Number Of digits in: ", x, " is ", count)

