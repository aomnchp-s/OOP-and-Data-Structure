def read_text(filename):
    data = []
    try:
        with open(filename) as f:
            for line in f:
                data.append(line)
        return data

    except FileNotFoundError as err:
        print(f'File Not Found')

def display(data):
    conv_data = []
    for line in data:
        print(line)
        conv_data.append(line.lower().split())  

def main():
    while True:
        filename = input('Enter Filename: ')
        data = read_text(filename)
        if data is not None:
            display(data)
            break

if __name__=='__main__':
    main()