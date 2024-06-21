def sqrange(n):
    for i in range(1, n+1):
        yield i**2

def main():
    returns = [r for r in sqrange(10)]
    print(f'Resturn: {returns}')

if __name__ == '__main__':
    main()