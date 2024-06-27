def compute_commission(sales_amount):
    if sales_amount <= 100000:
        commission = sales_amount*0.06
        print(commission)

    elif sales_amount <= 500000:
        commission1 = 100000*0.06
        commission2 = (sales_amount-100000)*0.08
        print(commission1)
        print(commission2)
    
    elif sales_amount<= 1000000:
        commission1 = 100000*0.06
        commission2 = 500000*0.06

def main():
    salr = int(input('Enter Salary: '))
    commission_rate = compute_commission(salr)

if __name__=='__main__':
    main()