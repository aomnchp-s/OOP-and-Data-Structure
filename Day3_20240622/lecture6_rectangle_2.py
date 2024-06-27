class Rectangle:
    def __init__(self, width:float, height:float) -> None:
        #มี _underscore จุดประสงค์คือเพื่อ ไม่อยากให้ access variable โดยตรง ให้ใช้แบบเรียกผ่าน method ต่างๆ
        self._width:float = width
        self._height:float = height

    def __str__(self) -> str:
        return f'{self._width} x {self._height}'

def main() -> None:
    r1 = Rectangle(10, 12)
    print(r1)
    r1._width = 20
    print(r1)
    r1 = Rectangle(30, 12)
    print(r1)

if __name__=='__main__':
    main()
