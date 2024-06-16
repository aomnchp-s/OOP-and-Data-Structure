line = input('Enter the set of number (e.g. 0,3,4,5): ')
numb = [int(n) for n in line.split(',')]
sum_even = 0

for i in numb:
    #print(i)
    if i%2 == 0:
        sum_even = sum_even + i

print(f'The summary even number is {sum_even}')