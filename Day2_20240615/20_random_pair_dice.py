from random import randint, choice

def random_dice(start: int, end: int):
    return randint(start,end)

def playgame():
    enter1 = input('Enter to start random a score of Person1 : ')
    person1 = random_dice(1,6)
    print(f'Score of Person1 : {person1}')

    enter2 = input('Enter to start random a score of Person2 : ')
    person2 = random_dice(1,6)
    print(f'Score of Person2 : {person2}')
    print()

    if person1 > person2:
        print('Person1 Win !!!')
    else:
        print('Person2 Win !!!')

def main():
    while True:
        enter = input('Do you want to play a game? Y/N : ')
        if enter == 'Y' or enter == 'y':
            playgame()
        elif enter == 'N' or enter == 'n':
            break

if __name__ == '__main__':
    main()