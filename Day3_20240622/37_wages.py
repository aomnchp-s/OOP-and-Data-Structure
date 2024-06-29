class Wages:
    def __init__(self, hours:float=0.0, rate:float=0.0) -> None:
        self._hours: float = hours
        self._rate: float = rate

    @property
    def payment(self) -> float:
        if self._hours>40:
            return ((self._hours-40)*(self._rate*1.5))+(self._rate*40)
        else:
            return self._hours*self._rate

    def __str__(self) -> str:
        return f'{self.payment}'

def main() -> None:
    wage = Wages(45,10)
    print(wage)

if __name__=='__main__':
    main()