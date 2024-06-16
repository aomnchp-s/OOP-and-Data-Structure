def is_triangle(a: int, b: int, c: int) -> bool:
    # print(f'{a+b} > {c}')
    # print(f'{b+c} > {a}')
    # print(f'{c+a} > {b}')
    return (a+b) > c and (b+c) > a and (c+a) > b

def main():
    enter = input('Enter 3 number to check is it Triangle: ')
    sides: list[int] = [int(s) for s in enter.split()]
    is_tri = is_triangle(sides[0],sides[1],sides[2])
    print(f'Is it Triangle: {is_tri}')

if __name__ == '__main__':
    main()