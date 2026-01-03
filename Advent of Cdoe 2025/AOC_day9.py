from collections import defaultdict

def build_tiles_hash(lst):
    index = defaultdict(list)
    for i, elem in enumerate(lst):
        index[elem[0]].append(i)
    return index

with open('AOC_day9.txt', 'r') as file:
    red_coordinates = [list(map(int, x.split(","))) for x in file.read().strip().split('\n')]
    red_coordinates.sort(key=lambda x: x[0])
    columns_max = red_coordinates[-1][0]
    columns_min = red_coordinates[0][0]

    tiles_hash = build_tiles_hash(red_coordinates)

    max_area = 0
    square_coordinates = []

    for col1 in tiles_hash.keys():
        for red_coordinate1 in  tiles_hash[col1]:
            tile_col1, tile_row1 = red_coordinates[red_coordinate1]
            for col2 in tiles_hash.keys():
                for red_coordinate2 in  tiles_hash[col2]:
                    tile_col2, tile_row2 = red_coordinates[red_coordinate2]
                    if tile_row2 > tile_row1 and red_coordinate1 != red_coordinate2:
                        area = abs(tile_col2 - tile_col1 + 1) * abs(tile_row2 - tile_row1 + 1)
                        if area > max_area:
                            max_area = area
                            square_coordinates = [[tile_col1, tile_row1],[tile_col1, tile_row2], [tile_col2, tile_row1], [tile_col2, tile_row2]]
    
    print(max_area)
    print(square_coordinates)
