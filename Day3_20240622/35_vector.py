class Vector:
    def __init__(self,v1:float, v2:float) -> None:
        self._v1:float = v1
        self._v2:float = v2

    def __str__(self) -> str:
        return f'Vector: {self._v1} {self._v2} \nMagnitude: {((self._v1)**2 + (self._v2)**2)**1/5}'


def main() -> None:
    enter = input('Enter a vector e.g.1 2: ')
    number = enter.split()

    vec = Vector(float(number[0]),float(number[1]))
    print(vec)

if __name__=='__main__':
    main()