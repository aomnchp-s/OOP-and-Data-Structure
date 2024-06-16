def describe_currency(symbol: str, name: str) -> None:
    print(f'Symbol: {symbol.upper()}')
    print(f'Name: {name.title()}')

def main():
    describe_currency('btc', 'bitcoin')
    describe_currency(symbol='eth', name='Etherium1')
    describe_currency(name='Etherium2', symbol='eth')

if __name__ == '__main__':
    main()