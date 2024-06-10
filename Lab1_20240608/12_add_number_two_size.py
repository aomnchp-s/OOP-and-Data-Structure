line1 = input('Enter number for list 1 : ')
numb1 = [int(m) for m in line1.split()]

line2 = input('Enter number for list 2 : ')
numb2 = [int(n) for n in line1.split()]

sum=[numb1+ numb2 for numb1, numb2 in zip(numb1, numb2)]
print(sum)