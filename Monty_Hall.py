# The Monty Hall Problem - Frequency Analysis - www.101computing.net/the-monty-hall-problem
import random
import os
import sys
import time

win_count = [0,0] #first counter for staying and second for switching
change_count = [0,0] #first counter for staying and second for switching
N = 100000

for trials in range(0,N):

    #Let's initialise our 3 doors
    doors = ["goat", "goat", "car"]

    # Randomly position the two goats and the car behind the three doors
    random.shuffle(doors)

    # Randomly pick a door and display the selected door number
    pick_door1 = random.randint(0,2)

    #while True:
     # input_int = int(input("Pick a door (integer from 0 to 2):\n"))
      #if input_int > len(doors):
       # print('Invalid number picked \n')
        #continue
      #else:
          #break

    #print('You picked door ', input_int)
    #print('\n')
    not_picked = [0,1,2]
    not_picked.pop(pick_door1)

    count_car = 0
    car_idx = 0

    for i in range(0, len(not_picked)):
        if doors[not_picked[i]] == "car":
            count_car += 1
            car_idx = i
            break
        else:
            continue

    pick_door2 = 0

    # Get the computer to identify the two doors which have not been selected
    #   If only one of these two doors contains a goat, display the door number to reveal the goat
    #   If both doors contain a goat, pick one of the two doors randomly and display its number to reveal the goat
    if count_car == 0:
        pick_door2 = random.randint(0,1)
    else:
        pick_door2 = 1 - car_idx


    not_picked.pop(pick_door2)

    # Get the computer to randomly decide whether it will keep the selected door or switch to the other closed door
    decide_door = random.randint(0,1) #0: Stay with door (pick_door1)
                                      #1: Move doors 
    change_count[decide_door] += 1
    
    # Check if the car was behind the selected door
    final_door = 0

    if decide_door == 0:
        final_door = doors[pick_door1]      
    else:
        final_door = doors[not_picked[0]]

    if final_door == "car":
        win_count[decide_door] += 1
    
    if trials > 10:
        print("Trials = ", trials, "\n")
        print("Percentage win when switching = ", "%.2f"%(win_count[1]*100/(change_count[1])), "%\n")
        print("Percentage win when staying = ", "%.2f"%(win_count[0]*100/(change_count[0])), "%\n")

    if trials < N - 1:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")





# If your code is working fine you should reach statistics to confirm that:
#     When switching doors your are twice as likely to win the car
#     When not switching doors your are twice as likely to get the goat!



