class Account:
    def __init__(self, amount:float) -> None:
        self._amount: float = amount
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value

    def deposit(self, amount:float):
        if self._amount > 0:
            self._amount += amount
        else:
            print('Amount must be positive !!')
    
    def withdraw(self, amount: float):
        if amount <= self._amount:
            self._amount -= amount
        else:
            print('Amount must be less than or equal to amount !!')
        
class SavingsAccount(Account):
    def __init__(self, amount:float) -> None:
        super().__init__(amount)
        self._account = Account(amount)

    def calculate_interest(self, rate):
        self._rate = rate

        intrest = self._amount*(self._rate/100)
        self._amount+=intrest
        return self._amount

    def __str__(self) -> str:
        return f'Balance: {self._amount}'

def main() -> None:
    save = SavingsAccount(500)
    save.deposit(100)
    save.calculate_interest(2.5)
    save.deposit(50)
    save.withdraw(65)
    print(save)

    
    
if __name__=='__main__':
    main()