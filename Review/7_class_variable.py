class Employee:
    #class variable
    _minSalary = 500
    _maxSalary = 2000

    def __init__(self, name, saraly, department) -> None:
        #instance variable
        self.__name = name
        self.__salary = saraly
        self.__department = department
    
    def _show_data(self):
        print(f'{"Name":12} {self.__name}')
        print(f'{"Saraly":12} {self.__salary}')
        print(f'{"Department":12} {self.__department}')

def main():
    emp = Employee('Natchaporn', 1000, 'IT')
    #สามารถเรียกใช้ได้โดยชื่อ class.ตัวแปล
    print(Employee._minSalary)  


if __name__ == '__main__':
    main()