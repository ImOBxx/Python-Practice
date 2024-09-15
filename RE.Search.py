import re

txt = "The rain in spain"
x = re.search("Portugal", txt)
print("The first white-space character is located in position:", x)