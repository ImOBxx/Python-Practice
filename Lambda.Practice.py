calc = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(calc(20))

string = "GeeksForGeeks"
print(lambda string : string)

def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y

lambda_cube = lambda num: num ** 3

print("invoking function defined with def keyword: ")
print(cube(30))
print("invoking lambda function: ", lambda_cube(30))


ml = [1, 2, 3, 4, 5]

nl = list(filter(lambda x: x % 2 != 0, ml))
print(nl)


num = 30
lc = lambda num : num ** 3
print(lc(30))


