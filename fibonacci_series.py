print("""this code shows the fibonacci series upto nth digit""")
n = int(input('How many digits you want to see?: '))


def fibo():
    n1 = 0
    n2 = 1
    print('your series is: ')
    for i in range(n):
        if i == 0:
            print(n1, end=' ')
        elif i == 1:
            print(n2, end=' ')
        else:
            n3 = n2 + n1
            print(n3, end=' ')
            n1 = n2
            n2 = n3


fibo()
