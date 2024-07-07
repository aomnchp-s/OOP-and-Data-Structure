class Employee:
    def detail(self):
        #สร้าง Attribute
        self.name = 'Natchaporn'
        self.salary = 1000

        print(f'Print attribute Name: {self.name}, Saraly: {self.salary}')
        print('{}'.format(self.name))
        print('{}'.format(self.salary))

def main():
    emp = Employee()
    #เรียกใช้ method detail
    emp.detail()

if __name__ == '__main__':
    main()

