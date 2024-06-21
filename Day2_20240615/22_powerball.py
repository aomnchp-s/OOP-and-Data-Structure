from random import randint, choice

def whitballs(start: int, end: int):
    for s in range(5):
        yield randint(start, end)

def powerball(start: int, end: int):
    yield randint(start, end)

def main():
    whiteB = [w for w in whitballs(1, 60)]
    powerB = [p for p in powerball(1, 35)]
    print(f'White Balls: {whiteB}')
    print(f'Powerball: {powerB}' )

if __name__ == '__main__':
    main()