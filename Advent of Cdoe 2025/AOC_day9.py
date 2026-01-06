from collections import defaultdict

def build_tiles_hash(lst, flag):
    index = defaultdict(list)
    for i, elem in enumerate(lst):
        if flag == 0:
            index[elem[0]].append(i)
        else:
            index[elem[1]].append(i)
    return index

def def_boundaries(lst, hash_row, hash_col, flag):
    boundaries = defaultdict(list)
    if flag == 0:
        for lst_cord in  lst:
            col1, row1 = lst_cord

            for tile_right in hash_row[row1]:
                row_right = lst[tile_right][1]
                col_right = lst[tile_right][0]

                if row_right == row1:
                    for col in range(col1, col_right + 1):
                        if row1 in boundaries[col]:
                            continue        
                        else:
                            boundaries[col].append(row1)
            
            for tile_down in hash_col[col1]:
                col_down = lst[tile_down][0]
                row_down = lst[tile_down][1]

                if col_down == col1:
                    if row_down in boundaries[col1]:
                        continue
                    else:
                        boundaries[col1].append(row_down)
    else:
        for lst_cord in  lst:
            col1, row1 = lst_cord

            for tile_down in hash_col[col1]:
                col_down = lst[tile_down][0]
                row_down = lst[tile_down][1]

                if col_down == col1:
                    for row in range(row1, row_down + 1):
                        if col1 in boundaries[row]:
                            continue        
                        else:
                            boundaries[row].append(col1)
            
            for tile_right in hash_row[row1]:
                row_right = lst[tile_right][1]
                col_right = lst[tile_right][0]

                if row_right == row1:
                    if col_right in boundaries[row1]:
                        continue
                    else:
                        boundaries[row1].append(col_right)
        
    return(boundaries)
        
def check_boundaries(boundaries_row, boundaries_col, coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    xmin, xmax = (x1, x2) if x1 <= x2 else (x2, x1)
    ymin, ymax = (y1, y2) if y1 <= y2 else (y2, y1)

    br = boundaries_row
    bc = boundaries_col

    for col in range(xmin, xmax + 1):
        lo, hi = br[col]
        if ymin < lo or ymax > hi:
            return 0

    for row in range(ymin, ymax + 1):
        lo, hi = bc[row]
        if xmin < lo or xmax > hi:
            return 0

    return 1


with open('AOC_day9.txt', 'r') as file:
    red_coordinates = [list(map(int, x.split(","))) for x in file.read().strip().split('\n')]
    red_coordinates.sort(key=lambda x: x[0])
    columns_max = red_coordinates[-1][0]
    columns_min = red_coordinates[0][0]

    tiles_hash_col = build_tiles_hash(red_coordinates, 0)
    tiles_hash_row = build_tiles_hash(red_coordinates, 1)

    max_area = 0
    square_coordinates = []

    part_flag = 2 # 1: Part 1  2: Part 2
    keys = list(tiles_hash_col)

    if part_flag == 1:
        for i, col1 in enumerate(keys):
            for red_coordinate1 in tiles_hash_col[col1]:
                tile_col1, tile_row1 = red_coordinates[red_coordinate1]
                for col2 in keys[i:]:
                    for red_coordinate2 in tiles_hash_col[col2]:
                        tile_col2, tile_row2 = red_coordinates[red_coordinate2]
                        if tile_row2 > tile_row1 and red_coordinate1 != red_coordinate2:
                            area = abs(tile_col2 - tile_col1 + 1) * abs(tile_row2 - tile_row1 + 1)
                            if area > max_area:
                                max_area = area
                                square_coordinates = [[tile_col1, tile_row1],[tile_col1, tile_row2], [tile_col2, tile_row1], [tile_col2, tile_row2]]
    else:
        boundaries_row = []
        boundaries_col = []

        boundaries_row = def_boundaries(red_coordinates, tiles_hash_row, tiles_hash_col, 0)
        boundaries_col = def_boundaries(red_coordinates, tiles_hash_row, tiles_hash_col, 1)

        for k, v in boundaries_row.items():
            boundaries_row[k] = [min(v), max(v)]

        for k, v in boundaries_col.items():
            boundaries_col[k] = [min(v), max(v)]
        
        for col1 in keys:
            for red_coordinate1 in tiles_hash_col[col1]:
                tile_col1, tile_row1 = red_coordinates[red_coordinate1]
                for col2 in keys:
                    for red_coordinate2 in tiles_hash_col[col2]:
                        tile_col2, tile_row2 = red_coordinates[red_coordinate2]
                        if tile_row2 > tile_row1 and red_coordinate1 != red_coordinate2:
                            if check_boundaries(boundaries_row, boundaries_col,red_coordinates[red_coordinate1], red_coordinates[red_coordinate2]):
                                area = (abs(tile_col2 - tile_col1) + 1) * (abs(tile_row2 - tile_row1) + 1)
                                if area > max_area:
                                    max_area = area
                                    square_coordinates = [[tile_col1, tile_row1],[tile_col1, tile_row2], [tile_col2, tile_row1], [tile_col2, tile_row2]]
        
    print(max_area)
    print(square_coordinates)
