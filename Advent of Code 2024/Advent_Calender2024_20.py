from collections import Counter

def find_cheat_patterns(grid, cheat_patterns):
    total_allowed_cheats = 0

    # Function to count overlapping occurrences of a pattern in a string
    def count_overlapping(string, pattern):
        count = 0
        start = 0
        while True:
            start = string.find(pattern, start)
            if start == -1:  # No more occurrences
                break
            count += 1
            start += 1  # Move start by 1 to allow overlaps
        return count

    transposed_grid = [''.join(col) for col in zip(*grid)]

    for row in grid:
        row_str = ''.join(row)  # Convert row to string
        for pattern in cheat_patterns:
            total_allowed_cheats += count_overlapping(row_str, pattern)

    for col_str in transposed_grid:
        for pattern in cheat_patterns:
            total_allowed_cheats += count_overlapping(col_str, pattern)
    return total_allowed_cheats

def find_start_and_end(grid):
    Start_position = []
    End_position = []

    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element != 'E' and element != 'S':
                continue
            elif element == 'E':
                End_position = [row_index, col_index]
            elif element == 'S':
                Start_position = [row_index, col_index]
    return Start_position, End_position

def find_normal_path(grid, S, E):
    normal_path = []
    i = S[0]
    j = S[1]
    
    prev = -1
    normal_path.append((i,j))
    while i != E[0] or j != E[1]:
        #move up
        if grid[i-1][j] == '.' and prev != 1:
            i -= 1
            prev = 0
        #move down
        elif grid[i+1][j] == '.' and prev != 0:
            i += 1
            prev = 1
        #move left
        elif grid[i][j-1] == '.' and  prev != 3:
            j -= 1
            prev = 2
        #move right
        else:
            j += 1
            prev = 3
        normal_path.append((i,j))

    return normal_path        
        
def find_cheat_tracks(grid, S, E, normal_path, normal_track_time, max_cheat_step, cheat_tracks):
    max_idx = len(grid) - 1
    min_idx = 0

    # Precompute indices for normal_path for O(1) lookup
    path_indices = {pos: idx for idx, pos in enumerate(normal_path)}

    cheat_idx = 0
    path_index = 0

    # Helper function to update cheat_tracks
    def update_cheat_tracks(cheat_idx, idx, offset, saved_time):
        cheat_tracks[cheat_idx]['1'] = offset
        cheat_tracks[cheat_idx]['2'] = idx
        cheat_tracks[cheat_idx]['saved time'] = saved_time

    while path_index < len(normal_path):
        i, j = normal_path[path_index]
        i_next, j_next = normal_path[min(path_index + 2, len(normal_path) - 1)]

        # Define possible cheat directions
        directions = []
        for step in range(2, max_cheat_step + 1):  # Loop from 1 to max_cheat_steps
            for di in range(-step, step + 1):  # Vertical offsets
                for dj in range(-step, step + 1):  # Horizontal offsets
                    if abs(di) + abs(dj) == step:  # Ensure exact step length
                        new_i = max(min_idx, min(max_idx, i + di))
                        new_j = max(min_idx, min(max_idx, j + dj))
                        directions.append(((new_i, new_j), (i + di // 2, j + dj // 2), step))

        for idx, offset, step in directions:
            if (
                grid[idx[0]][idx[1]] in ['.', 'E'] and
                (i_next, j_next) != idx and
                idx in path_indices and
                path_indices[idx] > path_index
            ):
                saved_time = path_indices[idx] - path_index - step
                update_cheat_tracks(cheat_idx, idx, offset, saved_time)
                cheat_idx += 1
                #break  # Only one cheat allowed per iteration

        path_index += 1
    return cheat_idx

 

with open('Input2024_20.txt', 'r') as file:
#with open('test.txt', 'r') as file:
 cheat_patterns = [".#.", "S#.", ".#S", "E#.", ".#E"]
 
 grid = file.read().strip().split("\n")
 grid = [list(line) for line in grid]

 #total_allowed_cheats = find_cheat_patterns(grid, cheat_patterns)

 S,E = find_start_and_end(grid)
 normal_path = find_normal_path(grid, S, E)

 normal_track_time = len(normal_path) - 1

 cheat_tracks = {i: {} for i in range(2000000)}

 max_cheat_step = 20

 total_allowed_cheats = find_cheat_tracks(grid, S, E, normal_path, normal_track_time, max_cheat_step, cheat_tracks)
 cheat_tracks = dict(list(cheat_tracks.items())[0:total_allowed_cheats])

 cheat_tracks = dict(sorted(cheat_tracks.items(), key=lambda item: item[1]['saved time'], reverse = True))

 count = sum(1 for key, val in cheat_tracks.items() if val['saved time'] >= 100)

 print(count)