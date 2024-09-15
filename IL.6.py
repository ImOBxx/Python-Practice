print()
s = input ("Enter String: ")
print("Orignal String: ", s)
print()
v_count = 0
c_count = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
     v_count += 1
else:
    c_count += 1
print()
print("Vowel Count: ", v_count)
print("Consonant Count: ", c_count)
print()
