s = int (input ("Enter Starting Point: "))
e = int (input ("Enter Ending Point: "))
e_count = 0
o_count = 0
t_count = 0
for i in range (s, e):
    if i % 2 == 0:
        e_count += 1
    elif i % 2 != 0:
        o_count += 1
t_count = e_count + o_count
print ("Total Number Of Even Numbers ", e_count)
print ("Total Number Of Odd Numbers: ", o_count)