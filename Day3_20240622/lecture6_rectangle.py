class Rectangle:
    def __init__(self, width:float, height:float) -> None:
        self.width:float = width
        self.height:float = height

    def __str__(self) -> str:
        return f'{self.width} x {self.height}'

def main() -> None:
    r1 = Rectangle(10, 12)
    print(r1)
    #accesscแบบโดยตรง
    r1.width = 20
    print(r1)

if __name__=='__main__':
    main()
