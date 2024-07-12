import json
import os

class Cryptocurrency:
    def __init__(self, symbol, name, amount):
        self.symbol = symbol
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name} ({self.symbol}): {self.amount}"

class Portfolio:
    def __init__(self, filename='cryptocurrency.json'):
        self.filename = filename
        self.cryptocurrencies = self.load_portfolio()

    def load_portfolio(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Cryptocurrency(item['symbol'], item['name'], item['amount']) for item in data]
        return []

    def save_portfolio(self):
        with open(self.filename, 'w') as file:
            data = [{'symbol': crypto.symbol, 'name': crypto.name, 'amount': crypto.amount} for crypto in self.cryptocurrencies]
            json.dump(data, file)

    def add(self, crypto):
        for c in self.cryptocurrencies:
            if c.symbol == crypto.symbol:
                c.amount += crypto.amount
                break
        else:
            self.cryptocurrencies.append(crypto)
        self.save_portfolio()

    def remove(self, symbol, amount):
        for c in self.cryptocurrencies:
            if c.symbol == symbol:
                if amount >= c.amount:
                    self.cryptocurrencies.remove(c)
                else:
                    c.amount -= amount
                break
        self.save_portfolio()

    def display(self):
        if not self.cryptocurrencies:
            print("No cryptocurrencies in the portfolio.")
        for c in self.cryptocurrencies:
            print(c)

def main():
    portfolio = Portfolio()

    while True:
        print("\nPortfolio Menu:")
        print("1. Add a cryptocurrency")
        print("2. Remove a cryptocurrency")
        print("3. Display portfolio")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter cryptocurrency symbol: ")
            name = input("Enter cryptocurrency name: ")
            amount = float(input("Enter amount: "))
            crypto = Cryptocurrency(symbol, name, amount)
            portfolio.add(crypto)
            print(f"Added {amount} of {name} ({symbol}) to the portfolio.")
        
        elif choice == '2':
            symbol = input("Enter cryptocurrency symbol to remove: ")
            amount = float(input("Enter amount to remove: "))
            portfolio.remove(symbol, amount)
            print(f"Removed {amount} of {symbol} from the portfolio.")

        elif choice == '3':
            portfolio.display()

        elif choice == '4':
            portfolio.save_portfolio()
            print("Portfolio saved. Exiting.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
