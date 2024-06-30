class Employee:
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
    emp1.detail("Natchaporn", 1000, "IT")
    emp1.show_data()

if __name__ == '__main__':
    main()
