from itertools import product

with open('Input2024_25.txt', 'r') as file:
#with open('test.txt', 'r') as file:
    key_pattern = '.....'
    lock_pattern = '#####'

    schematics = file.read().split("\n\n")
    Keys_Locks = [list(schematic.split("\n")) for schematic in schematics]
    Keys_schematic = []
    Locks_schematic = []
    Keys = []
    Locks = []

    for schematic in Keys_Locks:
        if schematic[0] == key_pattern:
            Keys_schematic.append([list(line) for line in schematic])
        else:
            Locks_schematic.append([list(line) for line in schematic])

    for i in range(len(Locks_schematic)):
        Locks_schematic[i] = list(map(list, zip(*Locks_schematic[i])))
        Locks.append([line.count("#") - 1 for line in Locks_schematic[i]])

    for i in range(len(Keys_schematic)):
        Keys_schematic[i] = list(map(list, zip(*Keys_schematic[i]))) 
        Keys.append([line.count("#") - 1 for line in Keys_schematic[i]])
        
    fits = len(Keys) * len(Locks)
    for lock, key in product(Locks, Keys):
        for a,b in zip(lock, key):
            if a + b > len(key):
                fits -= 1
                break
            else:
                continue

    print(fits)