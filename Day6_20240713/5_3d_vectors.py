import numpy as np

def add_3d_datasets(dataset1, dataset2):
    array1 = np.array(dataset1)
    array2 = np.array(dataset2)
    
    if array1.shape != array2.shape:
        raise ValueError("Both datasets must have the same shape")
    
    result = array1 + array2
    
    return result.tolist()

dataset1 = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

dataset2 = [
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
    [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
]

result = add_3d_datasets(dataset1, dataset2)
for layer in result:
    print(layer)
