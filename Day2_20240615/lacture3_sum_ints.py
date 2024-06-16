#*args recieve parameter as tuple type.
def sum_ints(*args) -> int:
    total = 0
    for num in args:
        total += num #total = toal + num
    return total

def main():
    print(sum_ints(1,2,3,4,5))
    print(sum_ints(1,2,3,4,5,6,7,8,9))

if __name__ == '__main__':
    main()