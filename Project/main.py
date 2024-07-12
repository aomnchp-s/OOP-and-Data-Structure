import sqlite3
from sqlite3 import Error
from expense import Expense
from category import Category

def create_connection(database):
    try:
        cnx = sqlite3.connect(database)
    except Error as err:
        print(err)
    return cnx

def menuTracker(): 
    while True:
        description = input('\nEnter description (q to quit): ')
        if description == 'q' or description == 'Q':
            break

        amount = float(input('Enter amount: '))
        date = input('Enter date: ')

        while True:
            expense_type = input('Enter C:Cash T:Tranfer: ')
            if expense_type == 't' or expense_type == 'T':
                bank = input('Enter destinatiom bank: ')
                category = input('Enter Category: ')
                break
            elif expense_type == 'c' or expense_type == 'c':
                bank = None
                category = input('Enter Category: ')
                break
        print(description, amount, date, expense_type, bank, category)

def main():
    database = 'expense_tracker.sqlite3'
    #create database
    cnx = create_connection(database)

    #init category table
    cate = Category(cnx)
    cate.create_table_category()
    cate.add_category('Food','1')

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
            menuTracker()
        elif menu == '2':
            pass
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