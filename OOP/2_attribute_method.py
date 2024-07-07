class Employee:
    #สร้าง method (เหมือนกันกับ function, 
    #สร้างใน class เรียก method อยู่นอก class เรียก function)
    def detail(self):
        print('Call method detail !!')

def main():
    emp = Employee()
    #เรียกใช้ method detail
    emp.detail()

if __name__ == '__main__':
    main()

