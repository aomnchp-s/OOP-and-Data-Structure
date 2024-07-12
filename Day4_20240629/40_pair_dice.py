from random import randint

class PairOfDice:
    def __init__(self) -> None:
        self._red_die = 0
        self._blue_die = 0
    
    @property
    def red_die(self):
        return self._red_die
    
    @property
    def blue_die(self):
        return self._blue_die
    
    def roll(self):
        self._red_die = randint(1, 6)
        self._blue_die = randint(1, 6)

    def sum_die(self):
        return self._red_die + self._blue_die

def main():
    # person1.roll()
    # print(person1.sum_die())
    while True:
        person1 = PairOfDice()
        person2 = PairOfDice()
        
        person1.roll()
        print(f'Player1 -- Red Die: {person1.red_die} -- Blue Die: {person1.blue_die} -- Sum: {person1.sum_die()}')
        person2.roll()
        print(f'Player2 -- Red Die: {person2.red_die} -- Blue Die: {person2.blue_die} -- Sum: {person2.sum_die()}')

        if person1.sum_die() > person2.sum_die():
            print('Player1 Win !!')
        elif person2.sum_die() > person1.sum_die():
            print('Player2 Win !!')
        else:
            print('--- TIE ---')

        enter = input('Do you want to play again? y/n : ')
        if enter == 'y':
            continue
        elif enter == 'n':
            break

if __name__ == '__main__':
    main()