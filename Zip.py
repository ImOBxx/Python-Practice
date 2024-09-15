a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]

#Lambda Expression
test = map(lambda pair: max(pair), zip(a, b))
result = list(test)
print(result)

result = list(map(lambda pair: max(pair), zip(a, b)))

print(result)

def custom_function(x, y):
    return x - y

# Use zip to pair elements, map to apply the custom function using a lambda, and convert the result to a list
result = list(map(lambda pair: custom_function(pair[0], pair[1]), zip(a, b)))

print(result)








"""myFunction = lambda x, y: x * y
r = myFunction(2, 3)
print(r)"""
