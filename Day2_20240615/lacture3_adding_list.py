list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]

#1
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(f'#1: {list3}')

#2
list3 = []
for a,b in zip(list1, list2):
    list3.append(a+b)
print(f'#2: {list3}')

#3
list4: list[int] = [a+b for a,b in zip(list1, list2)]
print(f'#3: {list4}')

