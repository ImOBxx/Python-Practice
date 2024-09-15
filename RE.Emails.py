import re

txt = '''cat mat pat bat
CoreyMSchafer@gmail.com
corey.scahfer@university.edu
corey-321-schafer@my-work.net
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov'''



pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(txt)

for match in matches:
    print(match)


#pattern = re.compile(r'[^]')
"""matches = pattern.finditer(txt)

for match in matches:
    print(match)"""