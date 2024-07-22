from connect_db import ConnectDB

class Category:
    def __init__(self, cnx) -> None:
        self._cnx = cnx
        self._db = ConnectDB()

    def check_exist_category(self, value):
        # db = ConnectDB()
        category = self._db.select_category(self._cnx)
        self._category_list = [i[1] for i in category]
        if value in self._category_list:
            return True
        elif value not in self._category_list:
            return False
        # return self._category_list
    
    def add_category(self, category, type):
        self._db.insert_category(self._cnx, category,type)
    
    def display_category(self):
        category = self._db.select_category(self._cnx)
        for i in category:
            print(f'{i[1]}')
