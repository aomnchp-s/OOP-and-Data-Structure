class Employee:
    def __init__(self, name, saraly, department) -> None:
        #ประกาศเป็น Private Attribute
        self.__name = name
        self.__salary = saraly
        self.__department = department
    
    def _show_data(self):
        print(f'{"Name":12} {self.__name}')
        print(f'{"Saraly":12} {self.__salary}')
        print(f'{"Department":12} {self.__department}')

    #set ให้นอก class passค่าใหม่มาให้ self.__name
    def setName(self, new_name):
        self.__name = new_name

    def setSaraly(self, newSaraly):
        self.__salary = newSaraly

def main():
    emp = Employee('Natchaporn', 1000, 'IT')
    emp.setName('AoooM')
    emp.setSaraly(5000)
    emp._show_data()



if __name__ == '__main__':
    main()
