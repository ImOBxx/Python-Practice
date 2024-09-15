def insert(s, w):
    return s[:2] + w + s[2:]

print(insert('[[]]', 'Python'))
print(insert('{{}}', 'PHP'))
print(insert('<<>>', 'HTML'))
