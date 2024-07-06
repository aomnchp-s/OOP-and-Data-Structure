class Ingredient:
    def __init__(self, name:str, amount:float, unit:str) -> None:
        self.name = name
        self.amount = amount
        self.unit = unit

        @property
        def amount(self):
            return self._amount
        
        @amount.setter
        def amount(self, value):
            self._amount = value

    def __str__(self) -> str:
        return f'{self.name} {self.amount} {self.unit}'

class Recipe:
    def __init__(self, name:str, description:str) -> None:
        self._name = name
        self._description = description
        self._ingredientList = []

    def add_ingredient(self, ingredient):
            self._ingredientList.append(ingredient)


    def display(self):
        print(self._name)
        print(self._description)
        for i in self._ingredientList:
            print(f'- {i}')

def main():
    while True:
        print('Main menu')
        print(f'{"1.":3} {"Enter a new Reciep."}')
        print(f'{"2.":3} {"Display the Reciepe Book."}')
        print(f'{"q.":3} {"Quit."}')
        menu = input('Enter Selection: ')

        if menu == '1':
            recipe_name = input('Enter the reciep name: ')
            recipe_descrip = input('Enter the reciep description: ')
            recipe = Recipe(recipe_name, recipe_descrip)

            while True:
                ingre_name = input('Enter ingredient name: ')
                if ingre_name == 'q':
                    break
                ingre_amount = input('Enter amount: ')
                if ingre_amount == 'q':
                    break               
                ingre_unit = input('Enter unit: ')
                if ingre_unit == 'q':
                    break   
                ingredient = Ingredient(ingre_name, float(ingre_amount), ingre_unit)
                recipe.add_ingredient(ingredient)

        elif menu == '2':
            recipe.display()
        elif menu == 'q':
            break


if __name__=='__main__':
    main()