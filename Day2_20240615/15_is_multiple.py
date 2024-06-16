#1
def is_multiple(m: int, n: int) -> bool:
    if (m%n) == 0:
        return True
    else:
        return False
# 2
# def is_multiple(m,n) -> bool:
#     return m%n == 0

def main():
    m = int(input('Enter number m: '))
    n = int(input('Enter number n: '))
    check_mul = is_multiple(m,n)
    print(f'n is a multiple of m is {check_mul}')
    
if __name__ == '__main__':
    main()