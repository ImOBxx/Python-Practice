import re

txt = "The rain in spain"
x = re.sub("\s", "9", txt)
print(x)

y = re.sub("\s", "9", txt, 2)
print(y)
