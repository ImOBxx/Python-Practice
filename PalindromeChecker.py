print ()
n = int (input ("Enter Number: "))
temp = n
print ()
sum = 0
while (n > 0):
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10
if temp == sum:
    print ("The Number Is A Palindrome. ")
    print ()
else:
    print ("The Number is Not A Palindrome. ")
    print ()