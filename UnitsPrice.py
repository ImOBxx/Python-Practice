print()
n = int (input ("Enter Units Of Electricity: "))
print()
if n <= 100:
    x = 0
elif n <= 200 and n >= 100: 
    x = (n - 100) * 5
elif n > 300: 
    x = 500 + (n - 200) * 10

print ("Amount To Be Paid: ", x)
print()
    