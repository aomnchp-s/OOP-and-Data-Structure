import csv

def readcsv(filename):
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        data = [i for i in csv_reader]
    return data

def display_monthly(data):
    print('-'*107)
    print(f'{"Year":7} {"Jan":7} {"Feb":7} {"Mar":7} {"Apr":7} {"May":7} {"Jun":7} {"Jul":7} {"Aug":7} {"Sep":7} {"Oct":7} {"Nov":7} {"Dec":7}')
    print('-'*107)
    for i in data:
        print(f'{i.get("ï»¿Year"):7} {i.get("Jan"):7} {i.get("Feb"):7} {i.get("Mar"):7} {i.get("Apr"):7} {i.get("May"):7} {i.get("Jun"):7} {i.get("Jul"):7} {i.get("Aug"):7} {i.get("Sep"):7} {i.get("Oct"):7} {i.get("Nov"):7} {i.get("Dec"):7}')
    print('-'*107)
    print()

def display_quarter(data):
    print('-'*40)
    print(f'{"Year":7} {"Q1":7} {"Q2":7} {"Q3":7} {"Q4":7} ')
    print('-'*40)
    for i in data:
        print(f'{i.get("ï»¿Year"):7} {int(i.get("Jan")) + int(i.get("Feb")) + int(i.get("Mar")):7} {int(i.get("Apr")) + int(i.get("May")) + int(i.get("Jun")):7} {int(i.get("Jul")) + int(i.get("Aug")) + int(i.get("Sep")):7} {int(i.get("Oct")) + int(i.get("Nov")) + int(i.get("Dec")):7}')
    print('-'*40)
    print()

def display_yearly(data):
    total = 0
    print('-'*40)
    print(f'{"Year":25} {"Sales"}')
    print('-'*40)
    for i in data:
        print(f'{i.get("ï»¿Year"):25} {int(i.get("Jan")) + int(i.get("Feb")) + int(i.get("Mar")) + int(i.get("Apr")) + int(i.get("May")) + int(i.get("Jun")) + int(i.get("Jul")) + int(i.get("Aug")) + int(i.get("Sep")) + int(i.get("Oct")) + int(i.get("Nov")) + int(i.get("Dec"))}')
        total += int(i.get("Jan")) + int(i.get("Feb")) + int(i.get("Mar")) + int(i.get("Apr")) + int(i.get("May")) + int(i.get("Jun")) + int(i.get("Jul")) + int(i.get("Aug")) + int(i.get("Sep")) + int(i.get("Oct")) + int(i.get("Nov")) + int(i.get("Dec"))
    print('-'*40)
    print(f'{"Total sales: ":25} {total}')

def main():
    filename = 'tesla_car_sales.csv'
    data = readcsv(filename)
    print(data)
    display_monthly(data)
    display_quarter(data)
    display_yearly(data)

if __name__=='__main__':
    main()

