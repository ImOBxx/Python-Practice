import math
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
#print(k)

x = 'abcd'
for i in range(len(x)):
    #print(i)

    i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    """print(0)"""

list1 = [1, 3]
list2 = list1
list1[0] = 4
list1[1] = 5 
#print(list2)

class tester:
    def __init__(self, id):
        self.id = str(id)
        print("tester",self.id)
        
        self.id= "224"
 
temp = tester(12)
print(temp.id)


def addItem(listParam):
    listParam += [1]
 
mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))

z = set('abc$de')
'a' in z

print(math.pow(3, 2))



a = 42
print(id(a))  # This will print the unique identity (memory address) of the integer object 42.

x = 2 + 9 * ((3 * 12) - 8) / 10
print(x)

x = 24 // 6 % 3, 24 // 4 // 2
print(x)

x = float('10')
print(x)

"""x = int('10')
print(x)

x = int('10.8')
#print(x)

x = float (10.8)
print(x)"""


print(4 + 2 ** 5 // 10)

a = 'hello'
b = 'world'

print('{a}{b}{a}'.format(a = 'hello', b = 'world'))

x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)
