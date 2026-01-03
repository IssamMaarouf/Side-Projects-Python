with open('AOC_day4.txt', 'r') as file:
    grid = [list(x) for x in file.read().strip().split('\n')]

    rows = len(grid)
    cols = len(grid[0])
    positions = [[-1,0],[0,1],[1,0],[0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]
    positions_last_col = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0]] 
    positions_last_row = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

    def build_adj_grid():
        g = [[0 for col in range(cols)] for row in range(rows)]
        if grid[0][0] == '@':
            if grid[0][1] == '@':
                g[0][0] += 1
                
            if grid[1][0] == '@':
                g[0][0] += 1
            
            if grid[1][1] == '@':
                g[0][0] += 1
        else:
            g[0][0] = -1

        if grid[rows-1][cols-1] == '@':  
            if grid[0][cols-2] == '@':
                g[rows-1][cols-1] += 1
                
            if grid[rows-2][cols-1] == '@':
                g[rows-1][cols-1] += 1
            
            if grid[rows-2][cols-2] == '@':
                g[rows-1][cols-1] += 1
        else:
            g[rows-1][cols-1] = -1

        for col in range(1,cols):
            if col < cols - 1:
                if grid[0][col] == '@':
                    if grid[0][col - 1] == '@':
                        g[0][col] += 1

                    if grid[0][col + 1] == '@':
                        g[0][col] += 1

                    if grid[1][col] == '@':
                        g[0][col] += 1

                    if grid[1][col - 1] == '@':
                        g[0][col] += 1

                    if grid[1][col + 1] == '@':
                        g[0][col] += 1
                else:
                    g[0][col] = -1
            else:
                if grid[0][col] == '@':
                    if grid[0][col - 1] == '@':
                        g[0][col] += 1
                    
                    if grid[1][col] == '@':
                        g[0][col] += 1
                    
                    if grid[1][col - 1] == '@':
                        g[0][col] += 1
                else: 
                    g[0][col] = -1

                
        for row in range(1,rows):
            if row < rows - 1:
                if grid[row][0] == '@':
                    if grid[row - 1][0] == '@':
                        g[row][0] += 1

                    if grid[row + 1][0] == '@':
                        g[row][0] += 1

                    if grid[row][1] == '@':
                        g[row][0] += 1

                    if grid[row - 1][1] == '@':
                        g[row][0] += 1

                    if grid[row + 1][1] == '@':
                        g[row][0] += 1
                else:
                    g[row][0] = -1
            else:
                if grid[row][0] == '@':
                    if grid[row - 1][0] == '@':
                        g[row][0] += 1
                    
                    if grid[row][1] == '@':
                        g[row][0] += 1
                    
                    if grid[row - 1][1] == '@':
                        g[row][0] += 1
                else:
                    g[row][0] = -1

        for row in range(1,rows):
            if row < rows - 1:
                for col in range(1,cols - 1):
                    if grid[row][col] == '@':
                        for pos in positions: 
                            if grid[row + pos[0]][col + pos[1]] == '@':
                                g[row][col] += 1
                    else:
                        g[row][col] = -1
            else:
                for col in range(1,cols - 1):
                    if grid[row][col] == '@':
                        for pos in positions_last_row: 
                            if grid[row + pos[0]][col + pos[1]] == '@':
                                g[row][col] += 1
                    else:
                        g[row][col] = -1

            
        for row in range(1,rows - 1):
            for pos in positions_last_col: 
                    if grid[row][cols - 1] == '@':
                        if grid[row + pos[0]][cols - 1 + pos[1]] == '@':
                            g[row][cols - 1] += 1
                    else:
                        g[row][cols - 1] = -1

        return g


sum_rolls = 0
removed_rolls = 0

#Part 1
grid_adj = build_adj_grid()

for row in range(0,rows):
    for col in range(0,cols):
        if grid_adj[row][col] < 4 and grid_adj[row][col] > -1:
            sum_rolls += 1
            grid[row][col] = '.'
            removed_rolls += 1

print(sum_rolls)

#Part 2
while removed_rolls != 0:
    removed_rolls = 0

    grid_adj = build_adj_grid()

    for row in range(0,rows):
        for col in range(0,cols):
            if grid_adj[row][col] < 4 and grid_adj[row][col] > -1:
                sum_rolls += 1
                grid[row][col] = '.'
                removed_rolls += 1

print(sum_rolls)
