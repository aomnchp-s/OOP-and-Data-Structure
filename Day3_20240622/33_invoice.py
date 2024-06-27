def read_file(filename:str) -> list[str]:
    data: list[str] = []
    with open(filename) as f:
        for line in f:
            data.append(line.split(','))
    return data

def sum_product(data:list[str]) -> int:
    total_amount = 0
    for i, j, k in data[1:]:
        total_amount = total_amount+(int(j) * float(k.strip()))
    return total_amount

def display_items(data:list[str]) -> None:
    for i, j, k in data[1:]:
        print(f'{i:20} {j:10} {k.strip():10} {int(j)*float(k):15}')

def display_invoice(data:list[str]) -> None:
    print(f'{"Description":20} {"Qty":10} {"Unit Price":10} {"Line Total":^27}')
    print('-'*65)
    display_items(data)
    print('-'*65)
    total_amount = sum_product(data)
    tax = total_amount*0.07
    total = total_amount+tax
    print(f'{"Subtotal:":50} {total_amount:>5}')
    print(f'{"Tax:":31} {"7.00%":18} {tax:>5.2f}')
    print(f'{"Total:":50} {total:>5.2f}')
    
def main():
    filename:str = 'product.txt'
    data: list[str] = read_file(filename)
    display_invoice(data)
    
if __name__=='__main__':
    main()