year = int(input('Input year to check the Leap Year: '))
leabYear = year%4

if year%4 == 0 and year%400 == 0 :
    print(f'{year} is Leab Year')
else:
    print(f'{year} is not Leab Year')