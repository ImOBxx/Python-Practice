x = int(input("Enter the integer number: "))
revs_number = 0
while (x > 0):
    remainder = x % 10
    revs_number = (revs_number * 10) + remainder
    x = x // 10
    print ("The reversed number is: ", revs_number)
