line = input('Enter list1: ')
line1 = [int(i) for i in line.split()]
line = input('Enter list2: ')
line2 = [int(i) for i in line.split()]

#1
line3 = []
for i in range(len(line1)):
    line3.append(line1[i] + line2[i])
print(line3)

#2
line4 = []
for a,b in zip(line1, line2):
    line4.append(a+b)
print(line4)

#3-list comprehension
line5 = [x+y for x, y in zip(line1, line2)]
print(line5)