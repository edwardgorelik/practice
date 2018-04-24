def Fib():
    fibs = [0,1]
    num = int(input("How many Fibonnaci numbers?"))
    for x in range (len(fibs),num):
        fibber = fibs[x-2] + fibs[x-1]
        fibs.append(fibber)
    print(fibs)


Fib()