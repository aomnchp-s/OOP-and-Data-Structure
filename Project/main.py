from connect_db import ConnectDB
from expense import Expense
from category import Category

def main():
    #create database
    db = ConnectDB()
    cnx = db.create_connection()
    #create table category
    db.create_table_category()
    #create table expense
    db.create_table_expense()
    #initail category
    init_cate = [['food','expense'], ['travel','expense'], ['salary','income']]
    cate = Category(cnx)
    for i in init_cate:
        is_exist = cate.check_exist_category(i[0])
        if is_exist == False:
            cate.add_category(i[0], i[1])
        elif is_exist == True:
            continue


    while True:
        print('\n----- Expense Tracker Menu -----')
        print('1. Expense Record')
        print('2. Income Record')
        print('3. Display Record')
        print('4. Add a New Category')
        print('5. Report')
        print('0. Quit')
        menu = input('Select a menu: ')

        if menu == '1':
            while True:
                types = 'expense'
                description = input('\nEnter description (q to quit): ')
                if description.lower() == 'q':
                    break

                amount = input('Enter amount: ')
                date = input('Enter date (YYYY-MM-DD): ')
                expense_chanel = input('Enter chanel (C:Cash T:Tranfer): ')
                if expense_chanel.lower() == 't':
                    bank = input('Ente destination bank: ')
                else: 
                    bank = None
                cate.display_category()
                category = input('Enter category (q to quit): ')
                if category.lower() == 'q':
                    break

                exp = Expense(cnx, description, amount, date, expense_chanel, bank, category, types)
                exp.add_expense()

        elif menu == '2':
            type = 'income'
        elif menu == '3':
            pass
        elif menu == '4':
            pass
        elif menu == '5':
            pass
        elif menu == '0':
            print('Thank you.......')
            break
      
if __name__ == '__main__':
    main()