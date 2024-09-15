d = {"john" : 40, "peter" : 45}
print(d["john"]) 

t = (1, 2)
print(2 * t)

#l = (1, 2, 3, 4)
#l.append(5, 6, 7)
#print(len(l))

a = (1, 2, (4 ,5))
b = (1, 2, (3, 4))


a = ("Check") * 3
print(a)

a = (0, 1, 2, 3, 4)
b = slice(0, 2)
print(a[b])

a, b, c = 1, 2, 3
print(a, b, c)

a = (1, 2)
b = (3, 4)
c = a + b
print(c)

a, b = 6, 7
a, b = b, a
print(a, b)

a = 2, 3, 4, 5
print(a)





a = set([1, 1, 2, 3, 3, 3, 4, 4])
print(len(a))

a = {5, 4}
b = {1, 2, 4, 5}
print(a < b)

"""a = {4, 5, 6}
b = {2, 8, 6}
print(a ^ b)"""

import sys
#print(len(sys.argv))
#print(sys.version)
print(dir(sys))

import random
print(random.random())

x = [1, 2, 3];
print(x)
