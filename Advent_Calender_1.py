import numpy as np
import re
#exp = re.compile(r'[0-9]{1,6}$')

list = []
list2 = []
sum = 0
sum2 = 0

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        list.append([int(s) for s in line.strip() if s.isdigit()])

    for i in range(0,len(list)):
        if len(list[i]) > 1:
            sum += 10 * list[i][0] + list[i][len(list[i]) - 1]
        else:
            sum += 10 * list[i][0] + list[i][len(list[i]) - 1]
    print(sum)





