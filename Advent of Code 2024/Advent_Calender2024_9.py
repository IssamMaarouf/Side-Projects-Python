import re
from collections import Counter
import time

start_time = time.time()

def find_dot_chains_in_list(lst, l, file_group):
    chains = -1
    n = len(lst)
    i = 0

    while i < n:
        if lst[i] == ".":
            start = i
            while i < n and lst[i] == ".":
                i += 1
            # Add the chain once it ends
            if (i - start) < file_group:
                continue
            else:
                chains = start + l
                break
        else:
            i += 1

    return chains

def arrange_files1(file_blocks):
 l = 0
 r = len(file_blocks) - 1
 
 while l < len(file_blocks) and r >= 0:

    if l == r:
        break

    if file_blocks[l] != ".":
        l += 1
        continue
    if file_blocks[r] == ".":
        r -= 1
        continue

    file_blocks[l] = file_blocks[r]
    file_blocks[r] = "."
    l += 1
    r -= 1
 return file_blocks 

def arrange_files2(file_blocks):
 l = 0
 r = len(file_blocks) - 1
 l_ult = 0

 file_group = 0

 while r >= l:

    if file_blocks[r] == ".":
        r -= 1
        continue
    else:
        id = file_blocks[r]
        while file_blocks[r] == id:
            file_group += 1
            r -= 1

    list_temp = file_blocks[l:r + file_group]

    spaces = find_dot_chains_in_list(list_temp, l, file_group)

    if(spaces != -1):
        for i in range(file_group):
            file_blocks[spaces + i] = file_blocks[r + 1 + i]
            file_blocks[r + 1 + i] = "."

    file_group = 0

    while file_blocks[l] != ".":
        l += 1

 return file_blocks

with open('Input2024_9.txt', 'r') as file:
#with open('test.txt', 'r') as file:
 disk_map = list(file.read())

 file_blocks = []
 for i,x in enumerate(disk_map):
     if i % 2 == 0:
         for j in range(int(x)):
            file_blocks.append(str(int(i / 2)))
     else:
         for j in range(int(x)):
            file_blocks.append(".")

 #file_blocks = arrange_files1(file_blocks)

 file_blocks = arrange_files2(file_blocks)

 checksum = sum([int(x) * i for i,x in enumerate(file_blocks) if x != "."])

 print(checksum)

print("--- %s seconds ---" % (time.time() - start_time))