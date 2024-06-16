def calculate_interest(principal: float, interest_rate: float = 0.5) -> float:
    interest: float = principal*interest_rate
    return interest

def main():
    principal: float = float(input('Enter Principal: '))
    intester_rate: float = float(input('Enter Interest Rate: '))
    #will calculate from the intester_rate argument that pass
    interest: float = calculate_interest(principal, intester_rate)
    print(f'Your interest is {interest:.2f}')

    #not pass the intester_rate argument, will calculate from the interest_rate parameter that default 0.5
    interest: float = calculate_interest(principal)
    print(f'Your interest is (use default) {interest:.2f}')

if __name__ == '__main__':
    main()