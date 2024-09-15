a = {"Ram", "Shayam", "Venom"}
b = {78, 90, 89}
l = dict(zip(a, b))
print(l)

def percentage(a):
    return (a * 10) / 100

ml = [i for i in map (percentage, b)]
print(ml)

nl = [name for name in map(lambda x : x.upper(), a)]
print(nl)

fm = [mark for mark in filter (lambda m : m >= 90, b)]
print(fm)


