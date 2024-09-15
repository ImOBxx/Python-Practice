def perf_num(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
            print("The Number Is A Perfect Number.")
            break
        else:
            print("The Number Is Not A Perfect Number.")

n = int (input ("Enter Number: "))
perf_num(n)