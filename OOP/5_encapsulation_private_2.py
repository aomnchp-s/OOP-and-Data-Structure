class Employee:
    def __init__(self, name, saraly, department) -> None:
        self._name = name
        #สร้าง Provate Attribute ไม่สามารถแก้ไขได้
        self.__salary = saraly
        self.__department = department
        #เรียกใช้ Private Method จากใน Class
        self.__show_data()
    
    #สร้าง Provate Method นอก class จะไม่สามารถมองเห็น 
    def __show_data(self):
        print(f'{"Name":12} {self._name}')
        print(f'{"Saraly":12} {self.__salary}')
        print(f'{"Department":12} {self.__department}')

def main():
    emp1 = Employee("Natchaporn", 1000, "IT")

if __name__ == '__main__':
    main()
