import numpy as np


def is_safe(x, sign):
    i = 1
    while i < len(x):
        temp = x[i] - x[i - 1]

        if sign != np.sign(temp):
            return 1
            
        temp = abs(temp)

        if temp < 1 or temp > 3:
            return 1
        i += 1

    fail = 0
    return 0

with open('Input2024_2.txt', 'r') as file:
    reports = file.read().split("\n")
    levels = [x.split() for x in reports]
   
    safe1 = len(reports)
    safe2 = len(reports)

    for x in levels:
        x = np.array(x).astype(int)

        if x[0] > x[1]:
            sign = -1
        else:
            sign = 1

        if is_safe(x,sign):
            safe1 -= 1
            safe2 -= 1
            for i in range(0,len(x)):
                x_temp = np.delete(x, i)

                if x_temp[0] > x_temp[1]:
                    sign = -1
                else:
                    sign = 1

                if is_safe(x_temp, sign):
                    continue
                else:
                    safe2 += 1
                    break
        else:
            continue

    print(safe1, safe2)