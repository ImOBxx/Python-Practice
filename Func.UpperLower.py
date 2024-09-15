def upper(x):
    u_count = 0
    for char in x:
        if char.isupper():
           u_count += 1
    print("UpperCase: ", u_count)

def lower(x):
    l_count = 0
    for char in x:
        if char.islower():
          l_count += 1
    print("LowerCase: ", l_count)
    

x = input ("Enter String: ")
upper(x)
lower(x)
