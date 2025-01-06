import numpy as np
import re
import math

part = 2 #1: for part 1
         #2: for part 2

def dec_to_base_vector(decimal, base, leading_zeros):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    # Conversion to the desired base
    digits = []
    while decimal > 0:
        digits.append(decimal % base)
        decimal //= base

    # Reverse to get the correct order
    digits.reverse()

    # Add leading zeros if needed
    while len(digits) < leading_zeros:
        digits.insert(0, 0)

    return digits


def operations_part1(numbers):
    combs = pow(2,numbers - 1)
    leading_zeros = int(math.log2(combs))
    combinations = []
    for i in range (0,combs):
        combinations.append(dec_to_base_vector(i, 2, leading_zeros))

    return(combinations)

def calibration_part1(test_value, numbers, combinations):

    for i in range(0,len(combinations)):
        eval = int(numbers[0])

        j = 1
        for operation in combinations[i]:
            if operation == 0:
                eval += int(numbers[j])
            else:
                eval *= int(numbers[j])

            if eval > test_value:
                break

            j += 1

        if eval == test_value:
            return test_value
        else:
            continue

    return 0


def operations_part2(numbers):
    combs = pow(3,numbers - 1)
    leading_zeros = numbers -1
    combinations = []
    for i in range (0,combs):
        combinations.append(dec_to_base_vector(i, 3, leading_zeros))

    return(combinations)

def calibration_part2(test_value, numbers, combinations):

    for i in range(0,len(combinations)):
        eval = int(numbers[0])

        j = 1
        for operation in combinations[i]:
            if operation == 0:
                eval += int(numbers[j])
            elif  operation == 1:
                eval *= int(numbers[j])
            else:
                eval = int(str(eval) + numbers[j])

            #if eval > test_value:
             #   break

            j += 1

        if eval == test_value:
            return test_value
        else:
            continue

    return 0

with open('Input2024_7.txt', 'r') as file:
#with open('test.txt', 'r') as file:
    lines = file.read().splitlines()
    
    sum = 0
    
    for line in lines:
        values = line.strip().split(':')
        values[1] = values[1].split()
    
        if part == 1:
            combinations = operations_part1(len(values[1]))

            sum += calibration_part1(int(values[0]), values[1], combinations)
        else:
            combinations = operations_part2(len(values[1]))

            sum += calibration_part2(int(values[0]), values[1], combinations)

        #print(sum)
    print(sum)


