class Employee:
    def detail(self, name, saraly):
        #attibute self._name = name ที่รับเข้ามา
        #attibute self._salary = salary ที่รับเข้ามา
        self._name = name
        self._salary = saraly

        print(f'Name: {self._name:15} Saraly: {self._salary}')

def main():
    emp1 = Employee()
    #pass value ไปให้ attribute ใน method detail
    emp1.detail('Natchaporn', 1000)
    
    emp2 = Employee()
    #pass value ไปให้ attribute ใน method detail
    emp2.detail('Anurak', 2000)

if __name__ == '__main__':
    main()

