import csv

def read_data(filename:str) -> dict:
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        data = [i for i in csv_reader]
    return data

def cal_daily_return(data:dict[str]) -> None:
    adj_close: list[float] = []
    daily_return: list[float] = []
    result = []
    for i in data:
        adj_close.append(float(i['Adj Close']))
    
    for j in range(len(adj_close)):
        daily_return.append((adj_close[j]-adj_close[j-1])/adj_close[j-1])

    for k,l in zip(data,daily_return):
        result.append((k['Date'],k['Open'],k['High'],k['Low'],k['Close'],k['Volume'],k['Adj Close'], l))

    return result

def display_result(daily_return) -> None:
    print(f'{"Date":15} {"Open":15} {"High":15} {"Low":15} {"Close":20} {"Volume":20} {"Adj Close":20} {"Daily Return"}')
    print('-'*135)
    for i in daily_return:
        print(f'{i[0]:15} {i[1]:15} {i[2]:15} {i[3]:15} {i[4]:20} {i[5]:20} {i[6]:20} {i[7]:.4f}')

def main():
    filename:str = 'META.csv'
    data:dict[str] = read_data(filename)
    daily_return = cal_daily_return(data)
    display_result(daily_return)
    
    
if __name__=='__main__':
    main()