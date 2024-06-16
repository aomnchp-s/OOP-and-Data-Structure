hours = float(input('Input hours of works (per week): '))
hourRate = float(input('Input hourly rate of works: '))

if hours <= 40:
    total = hours*hourRate
    print(f'{total}')
else:
    totalNormal = hourRate*40
    rateOver = hourRate*1.5
    overTime = (hours-40)*rateOver
    # print(totalNormal)
    # print(overTime)
    # print(rateOver)
    print(f'The total wages of week: {totalNormal+overTime}')
