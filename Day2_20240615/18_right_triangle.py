def right_triangle(a: int, b: int, c: int) -> bool:
    print((a**2)+(b**2), (c**2))
    return (a**2)+(b**2) == (c**2)

def main():
    enter = input('Enter 3 number to check is it Right Triangle: ')
    sides: list[int] = [int(s) for s in enter.split()]
    is_right_tri = right_triangle(sides[0], sides[1], sides[2])
    print(f'Is it Right Triangle: {is_right_tri}')

if __name__ == '__main__':
    main()