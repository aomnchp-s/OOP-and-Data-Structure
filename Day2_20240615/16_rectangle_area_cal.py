def cal_rectangle_area(width: float, height: float) -> float:
    area = width * height
    return area

def main():
    width: float = float(input('Enter Width (cm): '))
    height: float = float(input('Enter Height (cm): '))
    rect_area = cal_rectangle_area(width,height)
    print(f'Rectangle area is {rect_area:.2f} sq cm')
    
if __name__ == '__main__':
    main()