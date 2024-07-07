class Employee:
    def __init__(self, name, saraly, department) -> None:
        #ประกาศเป็น Private Attribute
        self.__name = name
        self.__salary = saraly
        self.__department = department
    
    def _show_data(self):
        print(f'{"Name":12} {self.getName}')
        print(f'{"Saraly":12} {self.getSaraly}')
        print(f'{"Department":12} {self.getDepartment}')

    #set ให้นอก class passค่าใหม่มาให้ self.__name
    def setName(self, new_name):
        self.__name = new_name

    def setSaraly(self, newSaraly):
        self.__salary = newSaraly
    
    def setDepartment(self, newDepartment):
        self.__department = newDepartment

    #getter method ส่งค่าไปใช้งานนอก class
    def getName(self):
        return self.__name
    
    def getSaraly(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department

def main():
    emp = Employee('Natchaporn', 1000, 'IT')
    print(f'{emp.getName()} : {emp.getSaraly()}')

if __name__ == '__main__':
    main()
