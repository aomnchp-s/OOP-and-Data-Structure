class Rectangle:
    def __init__(self, width:float, height:float) -> None:
        self.width:float = width
        self.height:float = height

    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, width:float) -> None:
        self._width:any = width
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, height:float) -> None:
        self._height:any = height

    def __str__(self) -> str:
        return f'{self._width} x {self._height}'

def main() -> None:
    r1 = Rectangle(10, 12)
    print(r1)
    r1.width = 20
    r1.height = 40
    print(r1)


if __name__=='__main__':
    main()
