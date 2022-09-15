num = int(input('Введите число:  '))
def fib(num):
    lst = []
    f1, f2 = 1, 1
    for i in range(abs(num)):
        lst.append(f1)
        f1, f2 = f2, f1 + f2
    return lst
     
def neg_fib(num):
    lst = []
    f1, f2 = 1, -1
    for i in range(abs(num)):
        lst.append(f1)
        f1, f2 = f2, (f1 + 1) - (f2 + 1)
    return lst

print(neg_fib(num)[::-1] + [0] + fib(num))