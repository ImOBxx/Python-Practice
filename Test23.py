m = [1, 2, 2, 3, 4, 2, 5]
r = [x for x in m if x % 2 == 0]
print(r)

words = ["apple", "banana", "orange"]
result = [word.upper() for word in words]
print(result)

d = {1: "OB", 2: "RAM"}


print(10 * (3 + 5) // 2)

print(8 / 2 + 2 * 3)

print(-5 // 2)


x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(z)

x = [1, 2, 3]
y = x[:]
x[0] = 4
print(y)

x = [1, 2, 3]
y = x[:]
x.append(4)
print(x)