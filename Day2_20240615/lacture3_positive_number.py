line: str = input('Enter a list of numbers: ')
print(line.split())
numbers: list[int] = [int(item) for item in line.split()]
print(numbers)

#1
positive_numbers:list[int] = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print(f'#1: {positive_numbers}')

#2
#synctax: new_list = [item for item in old_list if condition]
post_number = [num for num in numbers if num > 0]
print(f'#2: {post_number}')