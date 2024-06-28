class Stock:
    def __init__(self, name, symbol, previous_close, last) -> None:
        self.name:str = name
        self.symbol:str = symbol
        self.previous_close:float = previous_close
        self.last:float = last

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name:str) -> None:
        self._name:any = name

    @property
    def symbol(self) -> str:
        return self._symbol
    
    @symbol.setter
    def symbol(self, symbol:str) -> None:
        self._symbol:any = symbol

    @property
    def previous_close(self) -> float:
        return self._previous_close
    
    @previous_close.setter
    def previous_close(self, previous_close:float) -> None:
        self._previous_close:any = previous_close

    @property
    def last(self) -> float:
        return self._last
    
    @last.setter
    def last(self, last:float) -> None:
        self._last:float = last
    
    @property
    def pct_change(self):
        return ((self._last - self._previous_close) / self._previous_close) * 100
    
    @property
    def change(self):
        return self._last - self._previous_close
    

    def __str__(self):
        return f'{self._name} : {self._symbol} \nPercentage Change: {self.pct_change:2f} \nPrice Different: {self.change:2f}'
        

def main() -> None:
    stock = Stock('Advanced Info Service PCL', 'ADVANC', 25.3, 30.5)
    print(stock)

if __name__=='__main__':
    main()