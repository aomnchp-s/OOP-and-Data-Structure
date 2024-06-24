import json

def load_json(filename):
    with open(filename, 'r') as in_file:
        data = json.load(in_file)
    return data

def get_orderbook(data):
    highbid = data["highbid"]
    lowask = data["lowask"]
    orderbook = []

    for bid, ask in zip(highbid, lowask):
        orderbook.append((bid['amount'],bid['rate'], ask['rate'], ask['amount'] ))
    return orderbook

def display_orderbook(data):
    print(f'{"Bid Volume":20} {"Bid Rate":20} {"Ask Rate":20} {"Ask Volume":20}')
    for bidv, bidr, askr, askv in data:
        print(f'{bidv:20} {bidr:20} {askr:20} {askv:20}')


def main():
    filename = 'orderbook.json'
    data = load_json(filename)
    orderbook = get_orderbook(data)
    display_orderbook(orderbook)
    
if __name__=='__main__':
    main()