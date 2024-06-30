class Employee:
    #สร้าง Constructure
    #Constructure เป็น method พิเศษ ถูกเรียกใช้งานทุกครั้งที่มีการสร้าง object มาเรียกใช้งาน class
    #จะสร้างหรือไม่สร้างก็ได้ ถ้าไม่สร้างก็จะ defaultให้ มีโครงสร้างแบบนี้เช่นกัน
    #กำหนดค่าเริ่มต้นให้กับ object
    def __init__(self) -> None:
        print('Default Constructure !!')
    
    def detail(self, name, saraly, department):
        self._name = name
        self._salary = saraly
        self._department = department

    def show_data(self):
        print(f'{"Name":12} {self._name}')
        print(f'{"Saraly":12} {self._salary}')
        print(f'{"Department":12} {self._department}')

def main():
    emp1 = Employee()
    emp2 = Employee()

if __name__ == '__main__':
    main()
