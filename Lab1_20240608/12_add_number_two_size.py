line1 = input('Enter 4 number for set1 (e.g. 0,3,4,5) : ')
numb1 = [int(m) for m in line1.split(',')]

line2 = input('Enter 4 number for set2 (e.g. 0,3,4,5) : ')
numb2 = [int(n) for n in line2.split(',')]

sum=[x + y for x, y in zip(numb1, numb2)]
print(f'Summary set1 and set2 are: {sum}')