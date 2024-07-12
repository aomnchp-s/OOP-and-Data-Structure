class Purchase:
    def __init__(self, description:str, price:float, quantity:int) -> None:
        self.description = description
        self.price = price
        self.quantity = quantity
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price < 0:
            print("Price must be positive !!")
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            print("Quantity must be positive !!")
        self._quantity = quantity

    def line_total(self):
        return self.price *self.quantity

class Cart:
    def __init__(self) -> None:
        self.purchase_item= []

    def add_cart(self,item):
        self.purchase_item.append(item)
    
    def sub_total(self):
        self.subtotal = 0
        for item in self.purchase_item:
            self.subtotal = self.subtotal + item.line_total()
        return self.subtotal

def print_receipt(cart):
    print('-'*80)
    print(f'{"Description":20} {"Qty":20} {"Unit Price":20} {"Line Total"}')
    print('-'*80)
    for i in cart.purchase_item:
        print(f'{i.description:7} {i.quantity:18} {i.price:20} {i.line_total():20}')
    print('-'*80)
    print(f'{"Sub Total: ":62} {cart.sub_total():2f}')
    print(f'{"Tax: ":62} {cart.sub_total()*(7/100):2f}')
    print(f'{"Total: ":62} {(cart.sub_total()*(7/100)) + cart.sub_total():2f}')

def main():
    cart = Cart()
    while True:
        description = input('Enter description of article (q to quit): ')
        if description == 'q':
            break

        price = float(input('Enter price: '))
        quantity = int(input('Enter quantity: '))

        purchase = Purchase(description, price, quantity)
        cart.add_cart(purchase)

    # print(f'-- {cart.sub_total()}')
    print_receipt(cart)

            

if __name__ == '__main__':
    main()