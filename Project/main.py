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
                    bank = input('Enter bank: ')
                else: 
                    bank = None
                cate.display_category()
                category = input('Enter category (q to quit to add category): ')
                if category.lower() == 'q':
                    break

                exp = Expense(cnx, description, amount, date, expense_chanel.lower(), bank, category, types)
                if exp.description is False or exp.amount is False or exp.date is False or exp.expense_chanel is False or exp.category is False:
                    print('Please try again!')
                else:
                    exp.add_expense()

        elif menu == '2':
            while True:
                types = 'income'
                description = input('\nEnter description (q to quit): ')
                if description.lower() == 'q':
                    break

                amount = input('Enter amount: ')
                date = input('Enter date (YYYY-MM-DD): ')
                expense_chanel = input('Enter chanel (C:Cash T:Tranfer): ')
                if expense_chanel.lower() == 't':
                    bank = input('Enter bank: ')
                else: 
                    bank = None
                cate.display_category()
                category = input('Enter category (q to quit to add category): ')
                if category.lower() == 'q':
                    break

                exp = Expense(cnx, description, amount, date, expense_chanel.lower(), bank, category, types)
                if exp.description is False or exp.amount is False or exp.date is False or exp.expense_chanel is False or exp.category is False:
                    print('Please try again!')
                else:
                    exp.add_expense()

        elif menu == '3':
            pass

        elif menu == '4':
            # cate.display_category()
            while True:
                cate.display_category()
                action = input('A:Add U:Update D:Delete (q to quit): ')
                if action.lower() == 'a':
                    new_category = input('Enter new category: ')
                    type_category = input('Enter type of category: ')
                    chk_new = cate.check_exist_category(new_category.lower())
                    if chk_new == False:
                        cate.add_category(new_category.lower(), type_category.lower())
                    elif is_exist == True:
                        print('Category is exist!')
                        continue
                elif action.lower() == 'u':
                    category_name = input('Enter category which update: ')
                    if cate.check_exist_category(category_name.lower()) == True:
                        category_edit = input('Enter category: ')
                        if cate.check_exist_category(category_edit.lower()) == True:
                            print('Category is exist!')
                        else:
                            cate.update_category(category_name.lower(), category_edit.lower())
                    else:
                        print('Category is not exist, canot update!')
                elif action.lower() == 'd':
                    category_name = input('Enter category which delete: ')
                    if cate.check_exist_category(category_name.lower()) == True:
                        cate.delete_category(category_name.lower())
                    else:
                        print('Category is not exist, canot delete!')
                elif action.lower() == 'q':
                    break

        elif menu == '5':
            pass
        elif menu == '0':
            print('Thank you.......')
            break
      
if __name__ == '__main__':
    main()