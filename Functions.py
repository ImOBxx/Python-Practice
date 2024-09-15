def add(n):
    return n + n

numbers = (1, 2, 3, 4, 5)
r = map (add, numbers)
print(list(r))

r = map(lambda x : x + x, numbers)
print(list(r))

numbers2 = (4, 5, 6)
r = map(lambda x, y: x + y, numbers, numbers2)
print(list(r))

l = ['sat', 'bat', 'cat', 'mat']
t = list(map(list, l))
print(t)

def double(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


r = list(map(double, numbers))
print(r)