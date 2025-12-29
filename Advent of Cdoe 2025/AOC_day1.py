import numpy as np

with open('AOC_day1.txt', 'r') as file:
    instructions = file.read().strip().split('\n')
    
    sum = 50
    sum_zero_p1 = 0
    sum_zero_p2 = 0

    #part 1
    for instruction in instructions:
        rotation = instruction[0]

        if rotation == 'L':
            sum -= int(instruction[1:])
        else:
            sum += int(instruction[1:])

        if sum % 100 == 0:
            sum_zero_p1 += 1

        sum %= 100

    sum = 50

    #part 2
    for instruction in instructions:
        oriention = instruction[0]
        rotation = int(instruction[1:])

        sum_zero_p2 += abs(rotation) // 100
 
        if oriention == 'L':
            rem = -(abs(rotation) % 100)
        else: 
            rem = abs(rotation) % 100 
        
        sum += rem

        if sum >= 100 or (sum <= 0 and sum != rem):
            sum_zero_p2 += 1

        sum %= 100

    print(sum_zero_p1)
    print(sum_zero_p2)