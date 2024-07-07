class Employee:
    _minSalary = 500
    _maxSalary = 2000
    _companyName = 'XYZ Company'

    def __init__(self, name, saraly, department) -> None:
        self.__name = name
        self.__salary = saraly
        self.__department = department

    def _income(self):
        return self.__salary*12
    
    def __str__(self) -> str:
        return f'Name: {self.__name} Department: {self.__department} Income: {self._income()}'

class Accounting(Employee):
    __departmentName = 'Accounting'
    def __init__(self, name, saraly):
        super().__init__(name, saraly, self.__departmentName)

class Programmer(Employee):
    __departmentName = 'Programmer'
    def __init__(self, name, saraly):
        super().__init__(name, saraly, self.__departmentName)

class Sale(Employee):
    __departmentName = 'Sale'
    def __init__(self, name, saraly):
        super().__init__(name, saraly, self.__departmentName)

def main():
    account = Accounting('AAA', 1000)
    print(account.__str__())

    programmer = Programmer('BBB',2000)
    print(programmer.__str__())

    sale = Sale('CCC', 3000)
    print(sale.__str__())


if __name__ == '__main__':
    main()