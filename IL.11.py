def power(b, e):
    
    if e == 0:
        return 1
    
    elif e == 1:
        return b
    
    elif e > 1:
        return b * power(b, e - 1)
 
    else:
        return 1 / power(b, -e)

if __name__ == '__main__':
    n = int (input ("Enter Base Number: "))
    p = int (input ("Enter Power Number: "))
    print("Base Exponent: ", power(n, p)) 

