"""l = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    l[i - 1] = l[i]
for i in range(0, 6):
    #print(l[i], end = " ")





#print(l.__getitem__(3))

i = 4
j = 5
#print(i.__add__(j))

va = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = va[0][0]
for l in va:
    for element in l:
        if v > element:
            v = element
#print(v)"""

class book:  
    def __init__(a, b):  
        a.o1 = b  
   
class child(book):  
    def __init__(a, b):  
        a.o2 = b  
   
obj = page(32)  
print "%d %d" % (obj.o1, obj.o2)  



