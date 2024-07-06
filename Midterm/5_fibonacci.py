def fibonacci(n):
    fib_num = [0,1]
    number = 0
    for i in range(0, n+1):
        number = fib_num[-1] + fib_num[-2]
        fib_num.append(number)
        yield number

def main():
    for i in fibonacci(20):
        print(i)


if __name__=='__main__':
    main()