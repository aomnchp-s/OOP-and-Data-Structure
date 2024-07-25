from connect_db import ConnectDB
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class Transaction:
    def __init__(self,cnx,startDate,endDate) -> None:
        self.startDate = startDate
        self.endDate = endDate
        self._db = ConnectDB()
        self._cnx = cnx

    @property
    def startDate(self):
        return self._startDate
    
    @startDate.setter
    def startDate(self, startDate_value):
        if not startDate_value:
            print('Date is empty!')
            self._startDate = False
        try:
            datetime.strptime(startDate_value, "%Y-%m-%d")
            self._startDate = startDate_value
        except:
            print('Invalid date format. Please enter date in YYYY-MM-DD!')
            self._startDate = False

    @property
    def endDate(self):
        return self._endDate
    
    @endDate.setter
    def endDate(self, endDate_value):
        if not endDate_value:
            print('Date is empty!')
            self._endDate = False
        try:
            datetime.strptime(endDate_value, "%Y-%m-%d")
            self._endDate = endDate_value
        except:
            print('Invalid date format. Please enter date in YYYY-MM-DD!')
            self._endDate = False

    def inquiry_transaction(self):
        transections = self._db.inquiry_transaction(self._cnx, self.startDate, self.endDate)
        return transections
    
    def count_expense(self):
        expense = 0
        for i in self.inquiry_transaction():
            if i[7] == 'expense':
                expense += i[2]
        return expense
    
    def count_income(self):
        income = 0
        for i in self.inquiry_transaction():
            if i[7] == 'income':
                income += i[2]
        return income

    def display_transaction(self):
        dis = self.inquiry_transaction()
        if dis == False:
            print('Have no data in period!')
        else:
            print()
            print('-'*70)
            print(f'Transaction between {self.startDate} to {self.endDate}.')
            print('-'*70)
            for i in dis:
                if i[7] == 'expense':
                    print(f'{i[3]:13} {i[1]:36}- {i[2]:<5}')

                elif i[7] == 'income':
                    print(f'{i[3]:13} {i[1]:36}+ {i[2]:<5}')
            print('-'*70)
            print(f'Expense: {self.count_expense()} {"":6} Income: {self.count_income()} {"":12} Balance: {self.count_income()-self.count_expense()}')
            print('-'*70)
            print()
    
    def chart(self):
        types = 'expense'
        chart = self._db.group_transaction(self._cnx, self.startDate, self.endDate, types)
        # if chart == False:
        #     print('Have no data in period!')
        # else:
        return chart
        
    def display_chart(self):
        data = self.chart()
        print(data)
        if data is not None:
            value = [i[0] for i in data]
            keys = [i[1] for i in data]

            pie = plt.pie(value,autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            plt.legend( loc = 'right', labels=keys)
            plt.show()
                    
            # y = np.array(value)
            # my_key = keys
            # plt.pie(y, labels=my_key)
            # plt.show()
        else:
            print('Have no data in period!')