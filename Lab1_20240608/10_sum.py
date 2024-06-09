line = input('Enter sequence of number: ')
numb = [int(n) for n in line.split()]
pos_number = []

for i in numb:
    #print(i)
    if i > 0:
        pos_number.append(i)

print(pos_number)




