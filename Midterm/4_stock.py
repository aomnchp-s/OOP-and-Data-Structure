import json
def readfile(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def get_52_week_high(data):
    print(data)
    get_high = []
    for i in data.values():
        for j in i:
            get_high.append(j['High'])
    return get_high

def get_52_week_low(data):
    get_low = []
    for i in data.values():
        for j in i:
            get_low.append(j['Low'])
    return get_low

def get_average_volume(data):
    get_volume = []
    for i in data.values():
        for j in i:
            get_volume.append(j['Volume'])
    return get_volume

def get_average_adj_price(data):
    get_adjclose = []
    for i in data.values():
        for j in i:
            get_adjclose.append(j['Adj Close'])
    return get_adjclose

def get_day_range(data):
    get_date = []
    get_diff = []
    for i in data.values():
        for j in i:
            get_date.append(j['Date'])
            get_diff.append(float(j['Close'])-float(j['Open']))

    get_rang = []
    for x, y in zip(get_date, get_diff):
        get_rang.append((x,y))
    return get_rang

def main():
    filename = input('Enter file name: ')
    data = readfile(filename)
    get_high = get_52_week_high(data)
    get_low = get_52_week_low(data)
    get_volume = get_average_volume(data)
    get_adjclose = get_average_adj_price(data)
    get_rang = get_day_range(data)
    sort_get_rang = tuple(sorted(get_rang, key=lambda x: x[1], reverse=True))

    print(f'{"High":18} {"Low":18} {"Volume":18} {"Adj Close":18}')
    print('-'*80)
    for high, low, volume, adj in zip(get_high, get_low, get_volume, get_adjclose):
        print(f'{high:18} {low:18} {volume:18} {adj:18}')
    print('-'*80)
    print(f'{"Date":18} {"Low":18} ')

    for x in sort_get_rang:
        print(f'{x[0]:18} {x[1]:.4f} ')


if __name__=='__main__':
    main()