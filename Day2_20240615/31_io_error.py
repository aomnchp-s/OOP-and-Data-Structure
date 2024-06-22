def read_data(filename):
    with open(filename) as in_file:
        for i in in_file:
            return i

def count_character(data):
    char_frequencies = {}
    for chr in data:
        if chr in char_frequencies.keys():
            char_frequencies[chr] += 1 
        else:
            char_frequencies[chr] = 1
    return char_frequencies

def main():
    filename = input('Enter a filename: ')
    try:
        data = read_data(filename)
        char_frequencies = count_character(data)
        for ch, fre in char_frequencies.items():
            print(f'{ch}: {fre}')

    except FileNotFoundError as errNotFound:
        print(f'File {filename} does not exist. Try again')
        main()

if __name__=='__main__':
    main()