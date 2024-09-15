print()
e = int (input ("Enter English Marks: "))
m = int (input ("Enter Maths Marks: "))
s = int (input ("Enter Science Marks: "))
ss = int (input ("Enter Social Studies: "))
print()

if (e == m == s == ss >= 80):
    print ("You are in Science Stream.")
    print()
elif (e > 80 and m == s > 50 and ss > 10):
    print ("You are in Commerce Stream.")
    print()
elif (e > 80 and ss > 80 and m > 10 and s > 10):
    print ("You are in Humanities.")
    print()

