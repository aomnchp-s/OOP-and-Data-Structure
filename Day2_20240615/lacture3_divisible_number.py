n = int(input('Enter a number: '))
divisible_numbers = []

#1
for i in range(n+1):
    if i%3 == 0 and i%5 == 0:
        divisible_numbers.append(i)
print(f'#1: {divisible_numbers}')

#2: list comprehension
divisible_numbers2 = [num for num in range(n+1) if num%3 == 0 and num%5 == 0]
print(f'#2: {divisible_numbers2}')