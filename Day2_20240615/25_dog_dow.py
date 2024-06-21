import csv

def read_data(filename) -> dict:
    with open(filename) as in_file:
        csv_reader = csv.DictReader(in_file)
        data = [row for row in csv_reader]
    return data

def find_yields(company,symbol,dividen, price_begin, price_end):
    #print(company,symbol, (float(price_end)-float(price_begin))/float(dividen))
    x = company,symbol, (float(price_end)-float(price_begin))/float(dividen)
    return x
  
def main():
    filename = 'dow.csv'
    data = read_data(filename)
    dog_lst = []
    
    for item in data:
        #print(item)
        line = find_yields(item.get('company'),item.get('symbol') , item.get('dividend'), item.get('price_begin'), item.get('price_end') )  
        dog_lst.append(line)

    dog_lst.sort(key=lambda a: a[1])
    print(f'{"Company":40} {"Symbol":30} {"Yield":30}')
    print(f'{"-"*80}')
    for i in dog_lst[0:10]:
        print(f'{i[0]:40} {i[1]:30} {i[2]:.2f} %')
    
if __name__=='__main__':
    main()