import math

def compute_distance(x,y):
    return math.sqrt(pow(x[0] - y[0],2) + pow(x[1] - y[1],2) + pow(x[2] - y[2],2))

with open('AOC_day8.txt', 'r') as file:
    junction_boxes = [list(map(int, x.split(","))) for x in file.read().strip().split('\n')]
    len_jb = len(junction_boxes)

    distances = []

    circuits = [[] for _ in range(len_jb)]
    for i in range(len_jb):
        circuits[i].append(i)

    junction_in_curcuit = list(range(len_jb))

    for i in range(len_jb):
        jb1 = junction_boxes[i]
        for j in range(i, len_jb):
            if i != j:
               jb2 = junction_boxes[j]
               distance = compute_distance(jb1,jb2)
               distances.append([i,j,distance])

    distances.sort(key=lambda x: x[2])

    part_flag = 2

    if part_flag == 1:
        
        i = 0
        while i < 1000:
            jb1_idx = distances[i][0]
            jb2_idx = distances[i][1]

            if junction_in_curcuit[jb1_idx] != junction_in_curcuit[jb2_idx]:

                circuits[junction_in_curcuit[jb1_idx]].extend(circuits[junction_in_curcuit[jb2_idx]])
                junc_idx_temp = junction_in_curcuit[jb2_idx]

                for junction in circuits[junction_in_curcuit[jb2_idx]]:
                    junction_in_curcuit[junction] = junction_in_curcuit[jb1_idx]

                circuits[junc_idx_temp] = []
            i += 1

        circuits.sort(key=lambda x:len(x), reverse=True)

        result_p1 = 1
        for i in range(3):
            result_p1 *= len(circuits[i])
        print(result_p1)
    else:

        while circuits.count([]) < len_jb - 1:
            jb1_idx, jb2_idx = distances[0][0],distances[0][1]
            distances.pop(0)

            if junction_in_curcuit[jb1_idx] != junction_in_curcuit[jb2_idx]:

                circuits[junction_in_curcuit[jb1_idx]].extend(circuits[junction_in_curcuit[jb2_idx]])
                junc_idx_temp = junction_in_curcuit[jb2_idx]

                for junction in circuits[junction_in_curcuit[jb2_idx]]:
                    junction_in_curcuit[junction] = junction_in_curcuit[jb1_idx]

                circuits[junc_idx_temp] = []

        result_p2 = junction_boxes[jb1_idx][0] * junction_boxes[jb2_idx][0]
        print(result_p2)



