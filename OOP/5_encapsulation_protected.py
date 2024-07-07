class Employee:
    def __init__(self, name, saraly, department) -> None:
        #สร้าง Protected Attribute มี _ ตัวเดียว
        self._name = name
        self._salary = saraly
        self._department = department
    
    #สร้าง Protected Method มี _ ตัวเดียว
    def _show_data(self):
        print(f'{"Name":12} {self._name}')
        print(f'{"Saraly":12} {self._salary}')
        print(f'{"Department":12} {self._department}')

def main():
    emp1 = Employee('Natchaporn', 1000, 'IT')
    #ขอสิทในการเข้าไปแก้ชื่อ
    emp1._name = "Aom"
    print(emp1._name)
    
    emp2 = Employee('Anurak', 2000, 'IT')
    #ถ้าไม่ใส่ _ ไม่สามารถแก้ไขชื่อได้
    emp2.name = "Aum"
    print(emp2._name)

if __name__ == '__main__':
    main()
