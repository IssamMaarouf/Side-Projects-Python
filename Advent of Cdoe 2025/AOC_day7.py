from collections import Counter

def common_elements(a, b):
    i = j = 0
    common = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return common

with open('AOC_day7.txt', 'r') as file:
    tachyon_manifold = [list(x) for x in file.read().strip().split('\n')] 
    len_tm = len(tachyon_manifold)
    len_tm_row = len(tachyon_manifold[0])
    
    tachyon_manifold[1][int(len_tm_row/2)] = '|'
    beams_timelines = [0] * len_tm_row
    beams_timelines[int(len_tm_row / 2)] = 1

    beam = '|'
    splitter = '^'

    beam_split = 0

    for row in range(1,len_tm - 1):
        beams_idx = [i for i, c in enumerate(tachyon_manifold[row]) if c == beam]
        splitters_idx = [i for i, c in enumerate(tachyon_manifold[row + 1]) if c == splitter]

        beam_split_positions = common_elements(beams_idx,splitters_idx)
        lone_beams = sorted(set(beams_idx)^set(beam_split_positions))

        for splitter_idx in beam_split_positions:
            tachyon_manifold[row + 1][splitter_idx - 1] = beam
            tachyon_manifold[row + 1][splitter_idx + 1] = beam
            
            beams_timelines[splitter_idx - 1] += beams_timelines[splitter_idx]
            beams_timelines[splitter_idx + 1] += beams_timelines[splitter_idx]
            beams_timelines[splitter_idx] = 0

        for lone_beam in lone_beams:
            #if tachyon_manifold[row + 1][lone_beam] != '^'
                tachyon_manifold[row + 1][lone_beam] = beam

        if(splitters_idx != []):
            beam_split += len(beam_split_positions)

    #part 1
    print(beam_split)

    #part 2
    print(sum(beams_timelines))

    import json

    with open("output.txt", "w") as f:
        for row in tachyon_manifold:
            f.write("".join(map(str, row)) + "\n")


