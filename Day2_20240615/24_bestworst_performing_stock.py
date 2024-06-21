import csv

def read_data(filename) -> dict:
    with open(filename) as in_file:
        csv_reader = csv.DictReader(in_file)
        data = [row for row in csv_reader]
    return data

def cal_percentag(price_end,price_begin):
    percent_change = (price_end-price_begin)/price_begin*100
    return percent_change
    
def main():
    filename = 'dow.csv'
    perform_dict = {}
    data = read_data(filename)
    for item in data:
        percent_change = cal_percentag(float(item.get('price_end')), float(item.get('price_begin')))
        perform_dict[item.get('company')] = percent_change
    
    sort_perform = {k: v for k, v in sorted(perform_dict.items(), key=lambda item: item[1])}
    print(f'Best performing stock: {list(sort_perform)[-1]} {list(sort_perform.values())[-1]:.2f}%')
    print(f'Worst performing stock: {list(sort_perform)[0]} {list(sort_perform.values())[0]:.2f}%')
    

if __name__=='__main__':
    main()