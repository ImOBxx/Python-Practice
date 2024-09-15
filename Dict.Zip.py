import sys
from collections import OrderedDict

d = {"Akash", "Ram", "Shyam"}
l = {78, 56, 89}
x = OrderedDict(zip(d, l))
print("OrderedDict: ", x)


data = {name: mark for name, mark in zip(d, l)}
print(data)

xxxxxxx

# Unordered 

