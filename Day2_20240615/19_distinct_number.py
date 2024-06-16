def check_distinct(seq_num: list[int]) -> bool:
    number: list[int] = []
    for n in seq_num:
        if n not in number:
            number.append(n)
    return len(seq_num) == len(number)

def main():
    enter_num = input('Enter the sequence of number: ')
    seq_num = [int(n) for n in enter_num.split(',')]
    is_distinct = check_distinct(seq_num)
    print(f'They are distinct: {is_distinct}')

if __name__=='__main__':
    main()