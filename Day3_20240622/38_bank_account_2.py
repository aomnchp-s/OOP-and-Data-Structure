class Account:
    def __init__(self) -> None:
        self._balance = 0

    def deposit(self, amount:float):
        self.__amount = amount
        if self.__amount > 0:
            self._balance += self.__amount
        else:
            print('Deposit amount must be positive!!')
        return self._balance

    def withdraw(self, amount:float):
        self.__amount = amount
        if self.__amount <= self._balance:
            self._balance -= self.__amount
        else:
            print('Withdraw amount must be less than or equal balance !!')
        return self._balance

class SavingAccount(Account):
    def __init__(self) -> None:
        super().__init__()

    def calculate_interest(self, rate):
        self._rate = rate
        cal_rate = self._balance*(self._rate/100)
        self.deposit(cal_rate)
        return cal_rate

class CheckingAccount(Account):
    def __init__(self) -> None:
        super().__init__()

    def withdraw(self, amount: float, limit: int):
        return super().withdraw(amount)

def main():
    acc = SavingAccount()
    acc.deposit(1000)
    acc.deposit(500)
    acc.withdraw(100)
    acc.calculate_interest(2.6)
    print(acc)

    check = CheckingAccount()
    check.withdraw(1500,100)

if __name__=='__main__':
    main()