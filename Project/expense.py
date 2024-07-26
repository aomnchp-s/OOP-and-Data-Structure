from connect_db import ConnectDB
from datetime import datetime
from category import Category

class Expense:
    def __init__(self,cnx, description, amount, date, expense_chanel, bank, category, types) -> None:
        self.description = description
        self.amount = amount
        self.date = date
        self.expense_chanel = expense_chanel
        self.bank = bank
        self.types = types
        self._cnx = cnx
        self._db = ConnectDB()
        self.catex = Category(self._cnx)
        self.category = category

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description_value):
        if not description_value:
            print('Description is empty!')
            self._description = False
        else:
            self._description = description_value
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount_value):
        try:
            if not amount_value:
                print('Amount is empty!')
                self._amount = False
            elif float(amount_value) <= 0:
                print('Amount must be greater than 0!')
                self._amount = False
            else:
                self._amount = amount_value
        except:
            print('Invalid amount. Must enter a number!')
            self._amount = False

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date_value):
        if not date_value:
            print('Date is empty!')
            self._date = False
        try:
            datetime.strptime(date_value, "%Y-%m-%d")
            self._date = date_value
        except:
            print('Invalid date format. Please enter the date in YYYY-MM-DD!')
            self._date = False

    @property
    def expense_chanel(self):
        return self._expense_chanel
    
    @expense_chanel.setter
    def expense_chanel(self, expense_chanel_value):
        if not expense_chanel_value:
            print('Channel is empty!')
            self._expense_chanel = False
        elif expense_chanel_value == 'c' or expense_chanel_value == 't':
            self._expense_chanel = expense_chanel_value
        else:
            print('Invalid channel!')
            self._expense_chanel = False         
    
    @property
    def bank(self):
        return self._bank
    
    @bank.setter
    def bank(self, bank_value):
        if bank_value == '' or bank_value is None:
            self._bank = None
        self._bank = bank_value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_value):
        chk = self.catex.check_exist_category(category_value)
        if not category_value:
            print('Category is empty!')
            self._category = False
        elif chk is False:
            print("Category doesn't exist!")
            self._category = False
        else:
            self._category = category_value

    @property
    def types(self):
        return self._types
    
    @types.setter
    def types(self, types_value):
        self._types = types_value
        
    def add_expense(self):
        self._db.insert_expense(self._cnx, self.description,self.amount, self.date, self.expense_chanel, self.bank, self.category, self.types)

    def expense_transaction(self):
        print('expense_transaction')