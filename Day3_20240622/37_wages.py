class Wages:
    def __init__(self, hours:float=0.0, rate:float=0.0) -> None:
        self._hours: float = hours
        self._rate: float = rate

    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        self._hours = value

    def payment(self) -> float:
        amount = 0
        if self._hours>40:
            amount =((self._hours-40)*(self._rate*1.5))+(self._rate*40)
        else:
            amount = self._hours*self._rate
        self.hours = 0
        return amount

    def add_hours(self, hours):
        self._hours += hours

    def __str__(self) -> str:
        return f'{self.hours} {self._rate}'
    
class Woker:
    def __init__(self, name:str, rate:float) -> None:
        self._name = name
        self._wages = Wages(0, rate)
        
    def work(self, hours):
        self._wages.add_hours(hours)

    # def total_working_hours(self):
    #     return self._wages.hours

    def payment(self):
        payment = self._wages.payment()
        self._wages.hours = 0 
        return payment

def main() -> None:
    worker1 = Woker('Natchaporn', 10)
    worker1.work(45)
    worker1.work(10)
    worker1.work(15)
    payment = worker1.payment()
    print(payment)

if __name__=='__main__':
    main()