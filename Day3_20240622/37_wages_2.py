class Wages:
    def __init__(self, hours=0.0, rate=0.0) -> None:
        self.__hours = hours
        self.__rate = rate
        
    def payment(self):
        self.__amount = 0
        if self.__hours > 40:
            amount = ((self.__hours-40)*(self.__rate*1.5))+(self.__rate*40)
        else:
            amount = self.__hours*self.__rate
        return amount

class Woker:
    def __init__(self, name:float, rate:float) -> None:
        self.__name = name
        self.__rate = rate
        self.__total_hours = 0
    
    def work(self, hours:float):
        self.__total_hours += hours
        return self.__total_hours

    def payment(self):
        wage = Wages(self.__total_hours, self.__rate)
        print(f'{"Name:":20}{self.__name}')
        print(f'{"Total Hours:":20}{self.__total_hours}')
        print(f'{"Rate:":20}{self.__rate}')
        print(f'{"Payment:":20}{wage.payment()}')

def main():
    worker1 = Woker('Natchaporn', 1000)
    worker1.work(8)
    worker1.work(8)
    worker1.work(8)
    worker1.work(8)
    worker1.work(10)
    worker1.payment()

    worker2 = Woker('Anurak', 500)
    worker2.payment()


if __name__=='__main__':
    main()