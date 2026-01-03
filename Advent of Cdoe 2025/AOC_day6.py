#part 1

with open('AOC_day6.txt', 'r') as file:
    data = [x.split() for x in file.read().strip().split('\n')] 
    numbers = data[:-1]
    operations = data[-1]


    numbers_p1 = [list(map(int, col)) for col in zip(*numbers)]

    sum_total = 0
    row = 0
    for row_numbers in numbers_p1:
        sum_partial = row_numbers[0]
        for i in range(1, len(row_numbers)):
            if operations[row] == '*':
                 sum_partial *= row_numbers[i]
            else:
                sum_partial += row_numbers[i]
        sum_total += sum_partial
        row += 1

    print(sum_total)


#part 2
with open('AOC_day6.txt', 'r') as file:
    data = [x for x in file.read().strip().split('\n')] 
    numbers = data[:-1]

    len_divide = [0] * (len(operations) + 1)
    operations_temp = data[-1]
    len_divide[-1] = len(numbers[0])
    
    iter_len = 0
    for i in range(0,len(operations_temp)):
        symbol = operations_temp[i]
        if symbol == '*' or symbol == '+':
            len_divide[iter_len] = i
            iter_len += 1
    
    numbers_p2 = [[s[a:b] for a, b in zip(len_divide, len_divide[1:])] for s in numbers]
    numbers_p2 = list(map(list, zip(*numbers_p2)))
    operations = operations[::-1]

    sum_total = 0
    row = 0
    for row_numbers in reversed(numbers_p2):
        number = ''
        len_idx = len(row_numbers[0])

        for i in range(0, len(row_numbers)):
            numb = row_numbers[i][len_idx - 1]
            if(numb != ' '):
                number += numb

        if(number != ''):
            sum_partial = int(number)
        else:
            if operations[row] == '*':
                sum_partial = 1
            else:
                sum_partial = 0
        
        for digit_iter in range(len_idx - 2,-1,-1):
            number = ''
            for i in range(0, len(row_numbers)):
                numb = row_numbers[i][digit_iter]
                if(numb != ' '):
                    number += numb

            if number != '':
                if operations[row] == '*':
                    sum_partial *= int(number)
                else:
                    sum_partial += int(number)
            else:
                continue

        sum_total += sum_partial
        row += 1

    print(sum_total)
    
