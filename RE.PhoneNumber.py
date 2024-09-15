import re

txt = ''' qdinciciejoekoeieeiieieieieieenniene
eienfrnfirnfiienfennicinanqn;nqnkc;q
nrvenrjnirfiiiwicic abc abc abc......
coreyms.com
321-555-4321
123.555.1234'''
#print(r'\tTab') #Raw String

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(txt)

    
for match in matches:
    print(match)

print(txt[95:98])
print(txt[113:124])
