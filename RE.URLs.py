import re

txt = '''cat mat pat bat
CoreyMSchafer@gmail.com
corey.scahfer@university.edu
corey-321-schafer@my-work.net
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov'''



pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(txt)

subbed_urls = pattern.sub(r'\2\3', txt)
print(subbed_urls)
#for match in matches:
    #print(match.group(3))


#pattern = re.compile(r'[^]')
"""matches = pattern.finditer(txt)

for match in matches:
    print(match)"""