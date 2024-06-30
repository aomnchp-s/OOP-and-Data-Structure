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

#สืบทอดคุณสมบัติมาจาก Employee
class Accounting(Employee):
    __departmentName = 'Accounting'

    #โยนค่า parameter เข้ามาใน classลูก
    def __init__(self, name, saraly):
        #แล้วเรียกใช้ constructure ของclassแม่
        super().__init__(name, saraly, self.__departmentName)
        #เรียกใช้ method ในclassแม่
        super()._show_data()

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
    programmer = Programmer('BBB', 2000)
    programmer._show_data()


if __name__ == '__main__':
    main()