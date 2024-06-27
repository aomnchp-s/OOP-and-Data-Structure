class Vector:
    def __init__(self,v1:float, v2:float) -> None:
        self.v1:float = v1
        self.v2:float = v2

    @property
    def v1(self) -> float:
        return self._v1
    
    @property
    def v2(self) -> float:
        return self._v2
    
    @v1.setter
    def v1(self, v1:float) -> None:
        self._v1:any = v1
    
    @v2.setter
    def v2(self, v2:float) -> None:
        self._v2:any = v2

    def __str__(self) -> str:
        return f'Vector: {self.v1} {self.v2} \nMagnitude: {((self.v1)**2 + (self.v2)**2)**1/5}'


def main() -> None:
    enter = input('Enter a vector e.g.1 2: ')
    number = enter.split()

    vec = Vector(float(number[0]),float(number[1]))
    print(vec)

if __name__=='__main__':
    main()