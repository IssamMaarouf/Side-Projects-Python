
import numpy as np

def convert2binary(pattern, pattern_bin):
    for i in range(0, len(pattern)):
        for j in range(0, len(pattern[i])):
            for k in range(0, len(pattern[i][j])):
                if(pattern[i][j][k] == "#"):
                    pattern_bin[i][j][k] = 1
                else:
                    pattern_bin[i][j][k] = 0

def bin2dec(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


def find_reflection(pattern):

    ref_line = 0;
    ref_length_max = -1;

    for i in range(0, len(pattern) - 1):
        ref_length = 0
        flag = 0
        j = 0

        if pattern[i] == pattern[i + 1]:
            flag = 1
            for j in range(i + 2, len(pattern)):
                if pattern[j] == pattern[i - (j - i) + 1]:
                    ref_length += 1
                else:
                    break
        else:
            continue

        if flag ==1:
            if ref_length > ref_length_max and (i - (j - i) + 2 == 0 or j == len(pattern) - 1) or i == len(pattern) - 2:
                ref_length_max = ref_length
                ref_line = i + 1
            else:
                continue

    return([ref_line, ref_length_max + 1])

with open('input_13.txt') as f:
    pattern = f.read().split('\n\n')
    pattern = [x.split('\n') for x in pattern]
    
    pattern_bin = [0] * len(pattern) 

    for i in range(0, len(pattern)):
        pattern_bin[i] = [0] * len(pattern[i])
        for j in range(0, len(pattern[i])):
            pattern_bin[i][j] = [0] * len(pattern[i][j]) 

    convert2binary(pattern, pattern_bin)

    pattern_dec_row = [0] * len(pattern_bin) 
    pattern_dec_col = [0] * len(pattern_bin) 

    for i in range(0, len(pattern_bin)):
        pattern_dec_row[i] = [0] * len(pattern_bin[i])
        pattern_dec_col[i] = [0] * len(pattern_bin[i][0])


    for i in range(0,len(pattern_bin)):
        for j in range (0, len(pattern_bin[i])):
            pattern_dec_row[i][j] = bin2dec(pattern_bin[i][j])
        
        for j in range (0, len(pattern_bin[i][0])):
            #print([row[j] for row in pattern_bin[i]])
            pattern_dec_col[i][j] = bin2dec([row[j] for row in pattern_bin[i]])

    reflect_row = [0] * len(pattern);
    reflect_col = [0] * len(pattern);

    reflect = [0] * len(pattern);

    for i in range(0,len(pattern)):
        reflect_row[i] = find_reflection(pattern_dec_row[i])
        reflect_col[i] = find_reflection(pattern_dec_col[i])
  
    for i in range(0,len(pattern)):
        if reflect_row[i][1] > reflect_col[i][1]:
            reflect[i] = reflect_row[i]
            reflect[i].append(0)
        else:
            reflect[i] = reflect_col[i]
            reflect[i].append(1)

    total = 0

    for i in range(0,len(pattern)):
        if reflect[i][2] == 0:
            total += 100 * reflect[i][0]
            print(total, "\n")
        else:
            total += reflect[i][0]
            print(total, "\n")

    print(total)

    
    

    

