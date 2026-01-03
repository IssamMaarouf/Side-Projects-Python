import bisect

with open('AOC_day5.txt', 'r') as file:
    batches = file.read().splitlines()

    sep = batches.index("")

    ID_ranges = [list(map(int, r.split("-"))) for r in batches[:sep]]
    IDs = batches[sep + 1:]

    #Sort by the minumum element
    ID_ranges = sorted(ID_ranges, key=lambda x: x[0])

    part_flag = 1 #part 1: 0, part2: 1
    row = 1

    while row < len(ID_ranges):
        #Check if lower limit of current range is included in previous range 
        if ID_ranges[row][0] <= ID_ranges[row - 1][1]:
            #Check if upper of current range is included in previous range 
            if ID_ranges[row][1] > ID_ranges[row - 1][1]:
                ID_ranges[row - 1][1] = ID_ranges[row][1]

            del ID_ranges[row]
        else:
            row +=1

    if part_flag == 0:
        #part 1
        min_IDs = [x for x, _ in ID_ranges]

        def in_any_range(id):
            i = bisect.bisect_right(min_IDs, id) - 1
            return i >= 0 and id <= ID_ranges[i][1]

        sum_fresh = 0
        for id in IDs:
            id_int = int(id)
            sum_fresh += in_any_range(id_int)
    else:
        #part 2
        sum_fresh = 0
        for ID_range in ID_ranges:
            sum_fresh += ID_range[1] - ID_range[0] + 1
            print(sum_fresh)

    print(sum_fresh)







    