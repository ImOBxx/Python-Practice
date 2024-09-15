def factorial(n):
    
    if n == 0 or n == 1:
        return 1
   
    else:
        return n * factorial(n - 1)

n = int (input ("Enter Number: "))
print(f"Factorial Of {n} is {factorial(n)}")
