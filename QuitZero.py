sum = 0
count = 0
while True:
    x = int (input ("Enter Number: "))
    if x == 0:
        print ("Number is Zero")
        print ("Total Sum Of Numbers is: ", sum)
        break
    else:
        sum = sum + x
        count = count + 1
print ("Average Of Value Is: ", sum / count)