word = ["madem", "3634", "apple", "3765"]
ch = 0
for w in word:
    if len(w) > 1 and w[0] == w[-1]:
        ch += 1
print(ch) 