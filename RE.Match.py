import re

txt = "the rain in spain"
x = re.search("ai", txt)
print(x)
print(txt[5:7])

y = re.search(r"\bS\w", txt)
print(x.span())

a = re.search(r"\bS\w+", txt)


b = re.search(r"\bS\w+", txt)
print(b.group())