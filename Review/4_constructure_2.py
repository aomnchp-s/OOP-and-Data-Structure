class Employee:
    #สร้าง Constructure
    def __init__(self, name, saraly, department) -> None:
        self._name = name
        self._salary = saraly
        self._department = department
    
    def show_data(self):
        print(f'{"Name":12} {self._name}')
        print(f'{"Saraly":12} {self._salary}')
        print(f'{"Department":12} {self._department}')

def main():
    emp1 = Employee('Natchaporn', 1000, 'IT')
    #สามารถ access เข้าไปแก้attibuteได้ เนื่องจาก object ยังไม่ถูกห่อหุ้ม
    emp1._salary = 5000
    emp1.show_data()
    emp2 = Employee('Anurak', 2000, 'Sale')
    emp2.show_data()

if __name__ == '__main__':
    main()
