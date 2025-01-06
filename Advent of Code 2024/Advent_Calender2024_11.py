def update_stone(stone):
    length = len(str(stone))
    if stone == 0:
        return [1]
    elif length % 2 == 0:
        mid_index = length // 2
        stone = str(stone)
        part1 = int(stone[:mid_index])
        part2 = int(stone[mid_index:])
        return [part1 , part2]
    else:
        return [int(stone) * 2024]

with open('Input2024_11.txt', 'r') as file:
#with open('test.txt', 'r') as file:
    stones = {i: 1 for i in map(int, file.read().split())}
    
    i = 0
    while i < 75:
        new_stones = {}
        for stone in stones.keys():
            new_stone = update_stone(stone)
            for new in new_stone:
                if new_stones.get(new) is None:
                    new_stones[new] = 0
                new_stones[new] += stones[stone]      
        stones = new_stones
        i +=1

    print(sum(stones.values()))
