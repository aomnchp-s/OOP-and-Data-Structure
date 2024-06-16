def sqrange(n):
    for i in range(1, n+1):
        yield i**2

def main():
    for s in sqrange(10):
        print(s, end=',')

if __name__ == '__main__':
    main()