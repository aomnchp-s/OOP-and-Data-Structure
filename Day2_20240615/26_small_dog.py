import csv

def read_data(filename) -> dict:
    with open(filename) as in_file:
        csv_reader = csv.DictReader(in_file)
        data = [row for row in csv_reader]
    return data


  
def main():
    filename = 'dow.csv'
    data = read_data(filename)
    select_lst = []

    for i in data:
        #print(i['company'], i['symbol'], i['price_end'])
        x = i['company'], i['symbol'], float(i['price_end'])
        select_lst.append(x)
 
    x = sorted(select_lst, key=lambda t: (t[2]))
    print(f'{"Company":40} {"Symbol":30} {"Price":30}')
    print(f'{"-"*80}')
    for i in x[0:10]:
        print(f'{i[0]:40} {i[1]:30} {i[2]:.2f}')
   
    
    
if __name__=='__main__':
    main()