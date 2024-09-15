def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_n = filter(even, n)
print(list(even_n))