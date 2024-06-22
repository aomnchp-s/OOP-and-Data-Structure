def future_investment_value(amount, monthly_interest_rate, years):
    total = []
    for i in range(1, years+1):
        future_investment_value = amount * (1 + monthly_interest_rate)**(i*12)
        x = i, future_investment_value
        total.append(x)
    return total

def main():
    amount = int(input('Enter amount invested: '))
    interest_rate = float(input('Annual interest rate (% per year): '))
    monthly_interest_rate = (interest_rate/100)/12

    total = future_investment_value(amount,monthly_interest_rate,30)
    
    print(f'{"Year":3} {"Future Value":3}')
    print(f'{"-"*20}')
    for i in total:
        print(f'{i[0]:3} {i[1]:3.2f}')
    

if __name__=='__main__':
    main()