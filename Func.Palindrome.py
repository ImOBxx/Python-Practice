def palin(n):
    sum = 0
    temp = n
    while n > 0:
      r = n % 10
      sum = (sum * 10) + r
      n = n // 10

      if temp == sum:
          print("The Number Is An Palindrome. ")
          break
    else:
          print("The Number Is Not A Palindrome. ")

n = int (input ("Enter Number: "))
palin(n)

