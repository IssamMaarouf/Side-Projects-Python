import numpy as np
import textwrap

def compare_string_halves(s):
    length = len(s)
    mid_point = length // 2

    # Even length: split exactly in half
    first_half = s[:mid_point]
    second_half = s[mid_point:]

    # Compare the two halves
    are_equal = (first_half == second_half)
    return are_equal

def repeated_n_times(s):
    length = len(s)

    for len_split in range(1,length):
        if length % len_split == 0:
            partitions = textwrap.wrap(s,len_split)
            if len(set(partitions)) > 1:
                continue
            else:
                return 1
        else:
            continue

with open('AOC_day2.txt', 'r') as file:
    ID_ranges = [x.split('-') for x in file.read().strip().split(',')] 
    
    part_flag = 1
    sum_invalid_IDs = 0

    if part_flag == 0:
        #part 1
        for ID_range in ID_ranges:
            min_ID = int(ID_range[0])
            max_ID = int(ID_range[1])

            for ID in range(min_ID + 1, max_ID):
                ID_range.insert(len(ID_range) - 1, f'{ID}')
                      
            for ID in ID_range:
                if len(ID) % 2 == 0:
                    if compare_string_halves(ID):
                        sum_invalid_IDs += int(ID)
                else:
                    continue
    else:
        #part 2
        for ID_range in ID_ranges:
            min_ID = int(ID_range[0])
            max_ID = int(ID_range[1])

            for ID in range(min_ID + 1, max_ID):
                ID_range.insert(len(ID_range) - 1, f'{ID}')
                
            for ID in ID_range:
                if repeated_n_times(ID):
                    sum_invalid_IDs += int(ID)

    print(sum_invalid_IDs)
    

