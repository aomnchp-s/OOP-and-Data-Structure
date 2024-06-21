from random import randint, choice

def random_dice(start: int, end: int):
    for i in range(2):
        yield randint(start,end)

def playgame():
    name1 = input('Enter your name to random score: ')
    person1 = [p1 for p1 in random_dice(1,6)] 
    print(f"Score's {name1.title()} {person1[0]}, {person1[1]}")

    name2 = input('Enter your name to random score: ')
    person2 = [p2 for p2 in random_dice(1,6)] 
    print(f"Score's {name2.title()} {person2[0]}, {person2[1]}")

    if (person1[0]+person1[1]) > (person2[0]+person2[1]):
        print(f'{name1.title()} Win!! ')
    else:
        print(f'{name2.title()} Win!! ')

def main():
    while True:
        enter = input('Do you want to play a game? Y/N : ')
        if enter == 'Y' or enter == 'y':
            playgame()
        elif enter == 'N' or enter == 'n':
            break

if __name__ == '__main__':
    main()