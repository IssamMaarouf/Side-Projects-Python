import numpy as np

with open('AOC_day3.txt', 'r') as file:
    banks = [list(x) for x in file.read().strip().split('\n')]
    
    n_batteries = 12 #Number of batteries to be turned on 2: part1, 12: part2
    sum_joltage = 0

    max_bat = [0] * n_batteries
    max_pos = [0] * n_batteries

    for bank in banks:
        bat_window = n_batteries
        len_bank = len(bank)
        sum_joltage_str = ''

        len_idx = len_bank - (bat_window - 1)

        max_bat[0] = max(bank[0:len_idx])
        max_pos[0] = np.argmax(bank[0:len_idx])

        for bat in range(1,n_batteries):
            bat_window -= 1
            len_idx = len_bank - (bat_window - 1)
            init_idx = max_pos[bat - 1] + 1

            max_bat[bat] = max(bank[init_idx:len_idx])
            max_pos[bat] = np.argmax(bank[init_idx:len_idx]) + init_idx

        for bat_max in max_bat:
            sum_joltage_str += bat_max

        sum_joltage += int(sum_joltage_str)


    print(sum_joltage)