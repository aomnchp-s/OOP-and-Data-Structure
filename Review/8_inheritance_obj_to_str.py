class Employee:
    _minSalary = 500
    _maxSalary = 2000
    _companyName = 'XYZ Company'

    def __init__(self, name, saraly, department) -> None:
        self.__name = name
        self.__salary = saraly
        self.__department = department
    
    def _show_data(self):
        print(f'{"Name":12} {self.__name}')
        print(f'{"Saraly":12} {self.__salary}')
        print(f'{"Department":12} {self.__department}')

    def _income(self):
        return self.__salary*12

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
    print(f'Income per year of Accounting: {account._income()}')

    programmer = Programmer('BBB',2000)
    print(f'Income per year of Programmer: {programmer._income()}')

    sale = Sale('CCC', 3000)
    print(f'Income per year of Sale: {sale._income()}')


if __name__ == '__main__':
    main()