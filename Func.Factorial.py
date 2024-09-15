
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print(f"Factorial Of {n}: {f}")
    print()

print()
n = int (input ("Emter Number: "))
print()
factorial(n)