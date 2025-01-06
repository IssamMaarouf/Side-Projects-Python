import numpy as np
import re

#mul_line = r"mul\(\d{3},\d{3}\)"
mul_line = r"mul\((\d{1,3}),(\d{1,3})\)"
inst = r"do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)"

with open('Input2024_3.txt', 'r') as file:
    line = file.read()

    sum = 0
    sum2 = 0
    
    matches = np.array(re.findall(mul_line, line)).astype(int)

    for numbers in matches:
        sum += numbers[0] * numbers[1]

    results = []
    matches2 = re.finditer(inst, line)

    allow_numbers = 1

    for match in matches2:
        if match[0] == 'do()':
            allow_numbers = 1
        elif match[0] == 'don\'t()':
            allow_numbers = 0
        else:
            if allow_numbers:
                results.append((int(match.group(1)), int(match.group(2))))  # Store as tuple of integers

    for numbers in results:
        sum2 += numbers[0] * numbers[1]

    print(sum, sum2)