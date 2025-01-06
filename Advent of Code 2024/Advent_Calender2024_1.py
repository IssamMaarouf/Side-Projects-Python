import numpy as np


with open('Input2024_1.txt', 'r') as file:
    lines = file.read().split("\n")
    lists = [x.split() for x in lines]
    lists = np.transpose(lists).astype(int)
    lists2 = lists

    lists1 = np.sort(lists)
    
    dist = abs(lists1[0] - lists1[1])
    print(sum(dist))

    similarity = 0

    for numb1 in lists2[0]:
        similarity += numb1 * np.count_nonzero(lists2[1] == numb1) 

    print(similarity)