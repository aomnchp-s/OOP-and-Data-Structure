import random

def my_shuffle(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):  
        j = random.randrange(i + 1)  
        lst[i], lst[j] = lst[j], lst[i] 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_shuffle(my_list)
print("Shuffled list:", my_list)
