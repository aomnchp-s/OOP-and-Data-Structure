def read_data(filename):
    data = []
    with open(filename) as in_file:
        for line in in_file:
            data.append(line.strip().split(','))
    return data

def calculate(data):
    data_sum = {}
    data_count = {}
    mpg_dict = {}

    for i in data:
        if i[0] in data_count.keys():
            data_count[i[0]] += 1
        else:
            data_count[i[0]] = 1
        
    for j in data:
        if j[0] in data_sum.keys():
            data_sum[j[0]] += float(j[1])
        else:
            data_sum[j[0]] = float(j[1])
    
    for x, y in data_sum.items():
        mpg = (100/y) * data_count[x]
        mpg_dict[x] = mpg
    return mpg_dict

        
def main():
    filename = 'mileage.txt'
    data = read_data(filename)
    mpg = calculate(data)
    print(f'{"Model":<20} {"MPG":<20}')
    print('-'*28)
    for x,y in mpg.items():
        print(f'{x:<20} {y:.2f}')

if __name__=='__main__':
    main()