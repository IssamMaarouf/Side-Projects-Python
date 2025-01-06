import numpy as np
from collections import Counter
import re

def append_coordinates(grid, antennas):
    # Convert the Counter dictionary into a new structure
    updated_dict = {char: {'count': count, 'coordinates': []} for char, count in antennas.items()}

    # Iterate through the grid to collect coordinates
    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element in updated_dict:
                updated_dict[element]['coordinates'].append((row_index, col_index))
    
    return updated_dict


def find_antinodes(antennas):
    # Convert the Counter dictionary into a new structure
    updated_dict = antennas
    outbounds = len(grid)

    for char, data in updated_dict.items():
        data['antinodes'] = []
    anti = set()
    # Iterate through coordinates to locate antinodes
    for char, data in updated_dict.items():
        for i in range(0,data['count']):
            for j in range(0,data['count']):
                if j != i:
                    antinode_cooridantes = (2 * data['coordinates'][i][0] - data['coordinates'][j][0], 2 * data['coordinates'][i][1] - data['coordinates'][j][1])
                    if (antinode_cooridantes[0] >= 0 and antinode_cooridantes[0] < outbounds) and (antinode_cooridantes[1] >= 0 and antinode_cooridantes[1] < outbounds) and antinode_cooridantes not in anti:
                        data['antinodes'].append(antinode_cooridantes)
                        anti.add(antinode_cooridantes)

    return updated_dict


def find_antinodes2(antennas):
    # Convert the Counter dictionary into a new structure
    updated_dict = antennas
    outbounds = len(grid)

    for char, data in updated_dict.items():
        data['antinodes'] = []
    anti = set()
    # Iterate through coordinates to locate antinodes
    for char, data in updated_dict.items():
        for i in range(0,data['count']):
            for j in range(0,data['count']):
                if j != i:
                    dx = data['coordinates'][j][0] - data['coordinates'][i][0]
                    dy = data['coordinates'][j][1] - data['coordinates'][i][1]

                    antinode_coordinates = (data['coordinates'][i][0] + dx , data['coordinates'][i][1] + dy)
                    while 0 <= antinode_coordinates[0] < outbounds and 0 <= antinode_coordinates[1] < outbounds:
                        if antinode_coordinates not in anti:
                            data['antinodes'].append(antinode_coordinates)
                            anti.add(antinode_coordinates)
                        antinode_coordinates = (antinode_coordinates[0] + dx, antinode_coordinates[1] + dy)

    return updated_dict

with open('Input2024_8.txt', 'r') as file:
#with open('test.txt', 'r') as file:
 grid_tot = file.read()
 grid = grid_tot.split("\n")
 grid = [list(x) for x in grid]

 grid_size = pow(2, len(grid))

 antennas = Counter(x for row in grid for x in set(row))
 del antennas['.']

 antennas = append_coordinates(grid, antennas)

 #print(antennas.items())

 antennas = find_antinodes(antennas)

 #sum = 0

 #for data in antennas.values():
    # sum += len(data['antinodes'])

 sum2 = 0

 for data in antennas.values():
     for x,y in data.get('antinodes',[]):
         if grid[x][y] != '#':
             grid[x][y] = '#'
             sum2 += 1

 print(sum2)



with open('Input2024_8.txt', 'r') as file:
#with open('test.txt', 'r') as file:
 grid_tot = file.read()
 grid = grid_tot.split("\n")
 grid = [list(x) for x in grid]

 grid_size = pow(2, len(grid))

 antennas = Counter(x for row in grid for x in set(row))
 del antennas['.']

 antennas = append_coordinates(grid, antennas)

 #print(antennas.items())

 antennas = find_antinodes2(antennas)

 #sum = 0

 #for data in antennas.values():
   #  sum += len(data['antinodes'])

 sum2 = 0

 for data in antennas.values():
     for x,y in data.get('antinodes',[]):
         if grid[x][y] != '#':
             grid[x][y] = '#'
             sum2 += 1

 print(sum2)