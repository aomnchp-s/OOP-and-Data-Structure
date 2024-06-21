import csv

def read_data(filename) -> dict:
    with open(filename) as in_file:
        csv_reader = csv.DictReader(in_file)
        data = [row for row in csv_reader]
    return data

def get_info(data, input_symb):
    for item in data:
        #print(item)
        if item.get("symbol") == input_symb:
            for k,v in item.items():
                print(f'{k.title():13} : {v}')
    
def main():
    filename = 'dow.csv'
    data = read_data(filename)
    symbols = [symb.get('symbol') for symb in data]

    for s in symbols:
        print(s, end=' ')
    
    input_symb = input('\nEnter a symbol: ')
    if input_symb in symbols:
        get_info(data, input_symb)
    else:
        print('Invalid Symbol !!')

if __name__=='__main__':
    main()