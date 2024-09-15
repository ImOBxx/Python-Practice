print()
print ("        THE CALCULATOR         ")
print()
x = float (input ("Enter First Number: "))
print()
y = float (input ("Enter Second Number: "))
print()
print ("List of Operators: +, /, *, -, %, **, //")
print()
chr = (input ("Enter Operator: "))
print()
if (chr == '+'):
    print("Operator: +")
    sum = x + y
    print("Addition: ", sum)
elif (chr == '-'):
    print("Operator: -")
    sum = x - y
    print("Subtraction: ", sum)
elif (chr == '*'):
    print("Operator: *")
    sum = x * y
    print("Multiplication: ", sum)
elif (chr == '%'):
    print("Operator: %")
    sum = x % y
    print("Modulus: ", sum)
elif (chr == '/'):
    print("Operator: /")
    sum = x / y
    print("Division: ", sum)
elif (chr == '**'):
    print("Operator: **")
    sum = x ** y
    print("Power: ", sum)
elif (chr == '//'):
    print("Operator: //")
    sum = x // y
    print("Floor Division: ", sum)

