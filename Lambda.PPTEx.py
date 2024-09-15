def even(a):
    if a % 2 == 0: return True
    else: return False

l1 = [1, 2, 3, 8, 6, 11, 7]
nl = list(filter(lambda x: x % 2 == 0, l1))
print(nl)