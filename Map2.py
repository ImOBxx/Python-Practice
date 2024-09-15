def add(a, b):
    return a + b

n1 = [1, 2, 3, 4]
n2 = [5, 6, 7, 8]

sums = map(add, n1, n2)
print(list(sums))