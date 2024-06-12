line = input('Enter the set of number (e.g. 0,-3,4,-5): ')
numb = [int(n) for n in line.split(',')]
pos_number = []

for i in numb:
    if i > 0:
        pos_number.append(i)

print(f'The positive number is {pos_number}')




