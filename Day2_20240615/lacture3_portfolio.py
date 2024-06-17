def stock_value(symbol, nshares, price):
    value = nshares*price
    print(f'{symbol:5} {value:10.2f}')

#Passing by position argument
stock_value('TSLA', 150, 240)
#Passing by keyword argument
stock_value(symbol='TSLA', price=240, nshares=200)