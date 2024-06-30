class Employee:
    def __init__(self, name, saraly, department) -> None:
        self._name = name
        #สร้าง Provate Attribute ไม่สามารถแก้ไขได้
        self.__salary = saraly
        self.__department = department
    
    def _show_data(self):
        print(f'{"Name":12} {self._name}')
        print(f'{"Saraly":12} {self.__salary}')
        print(f'{"Department":12} {self.__department}')

def main():
    emp1 = Employee("Natchaporn", 1000, "IT")
    #แก้ไข salary ให้เป็น 50000 จะไม่สามารถแก้ไขได้เพราะประกาศเป็น private
    emp1.__salary = 50000
    emp1._name = 'Aoom'
    emp1._show_data()

if __name__ == '__main__':
    main()
