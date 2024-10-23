
import turtle, random
import numpy as np

race_steps = 10
race_steps_tracks = 100
race_track_cor = [[0,0],[race_steps_tracks,0]]


def create_race_track():
    min_y = -50
    max_y = 50
    dist = 1200
    
    prev = 0

    inc = 1
    dist -= race_steps_tracks

    while dist > 0:
        if race_track_cor[inc][1] < max_y and race_track_cor[inc][1] > min_y:

            rand = random.randint(0,2) #0: Move forward
                                       #1: Move down
                                       #2: Move up
            
            inc += 1
            
   
            if rand == 1 and prev != 2:
                race_track_cor.append([race_track_cor[inc-1][0], max(race_track_cor[inc-1][1] - race_steps_tracks, min_y)])
                prev = 1
            elif rand == 2 and prev != 1:
                race_track_cor.append([race_track_cor[inc-1][0], min(race_track_cor[inc-1][1] + race_steps_tracks, max_y)])
                prev = 2
            else:
                race_track_cor.append([race_steps_tracks + race_track_cor[inc-1][0],race_track_cor[inc-1][1]])
                dist -= race_steps_tracks
                prev = 0

        elif race_track_cor[inc][1] == min_y:

            rand = random.randint(0,1) #0: Move forward
                                       #1: Move up
            
            inc += 1

            if rand == 1 and prev != 1:
                race_track_cor.append([race_track_cor[inc-1][0], race_track_cor[inc-1][1] + race_steps_tracks])
                prev = 2
            else:
                race_track_cor.append([race_steps_tracks + race_track_cor[inc-1][0],race_track_cor[inc-1][1]])
                dist -= race_steps_tracks
                prev = 0
        
        else:
            rand = random.randint(0,1) #0: Move forward
                                       #1: Move down
            inc += 1                           
                 
            if rand == 1 and prev != 2:
                race_track_cor.append([race_track_cor[inc-1][0], race_track_cor[inc-1][1] - race_steps_tracks])   
                prev = 1
            else:
                race_track_cor.append([race_steps_tracks + race_track_cor[inc-1][0],race_track_cor[inc-1][1]])
                dist -= race_steps_tracks
                prev = 0



while True:
    myPen = turtle.Turtle()
    turtle.Screen().bgcolor("#3fa652")
    myPen.shape("arrow")
    myPen.pensize(2)
    myPen.speed(10)
    myPen.color("white")
    myPen.write("Turtle Race!", align='center',  font=("Arial", 20, "normal"))

    create_race_track()


    #Let's draw the start line
    myPen.penup()
    myPen.goto(-600, 500)
    myPen.pendown()
    myPen.goto(-600, -500)


    #Let's draw the finish line
    myPen.penup()
    myPen.goto(600, 500)
    myPen.pendown()
    myPen.goto(600, -500)


    #Add turtles
    #Red
    RedTurtle = turtle.Turtle()
    RedTurtle.shape('turtle')
    RedTurtle.color('red')
    RedTurtle.pensize(4)
    RedTurtle.penup()
    RedTurtle.goto(-600, 450)
    RedTurtle.pendown()


    #Blue
    BlueTurtle = turtle.Turtle()
    BlueTurtle.shape('turtle')
    BlueTurtle.color('Blue')
    BlueTurtle.pensize(4)
    BlueTurtle.penup()
    BlueTurtle.goto(-600, 150)
    BlueTurtle.pendown()


    #Orange
    OrangeTurtle = turtle.Turtle()
    OrangeTurtle.shape('turtle')
    OrangeTurtle.color('Orange')
    OrangeTurtle.pensize(4)
    OrangeTurtle.penup()
    OrangeTurtle.goto(-600, -150)
    OrangeTurtle.pendown()


    #Black
    BlackTurtle = turtle.Turtle()
    BlackTurtle.shape('turtle')
    BlackTurtle.color('black')
    BlackTurtle.pensize(4)
    BlackTurtle.penup()
    BlackTurtle.goto(-600, -450)
    BlackTurtle.pendown()


    for i in range(1,len(race_track_cor)):
        myPen.penup()
        myPen.goto(RedTurtle.xcor() + race_track_cor[i-1][0], RedTurtle.ycor() + race_track_cor[i-1][1])
        myPen.pendown()
        myPen.goto(RedTurtle.xcor() + race_track_cor[i][0], RedTurtle.ycor() + race_track_cor[i][1])


    for i in range(1,len(race_track_cor)):
        myPen.penup()
        myPen.goto(BlueTurtle.xcor() + race_track_cor[i-1][0], BlueTurtle.ycor() + race_track_cor[i-1][1])
        myPen.pendown()
        myPen.goto(BlueTurtle.xcor() + race_track_cor[i][0], BlueTurtle.ycor() + race_track_cor[i][1])

            
    for i in range(1,len(race_track_cor)):
       myPen.penup()
       myPen.goto(OrangeTurtle.xcor() + race_track_cor[i-1][0], OrangeTurtle.ycor() + race_track_cor[i-1][1])
       myPen.pendown()
       myPen.goto(OrangeTurtle.xcor() + race_track_cor[i][0], OrangeTurtle.ycor() + race_track_cor[i][1])

         
    for i in range(1,len(race_track_cor)):
        myPen.penup()
        myPen.goto(BlackTurtle.xcor() + race_track_cor[i-1][0], BlackTurtle.ycor() + race_track_cor[i-1][1])
        myPen.pendown()
        myPen.goto(BlackTurtle.xcor() + race_track_cor[i][0], BlackTurtle.ycor() + race_track_cor[i][1])



    #Start race
    inc_Red = 1
    inc_Blue = 1
    inc_Orange = 1
    inc_Black = 1

    while True:
        
        randRed = random.randint(1,race_steps)
        randBlue = random.randint(1,race_steps)
        randOrange = random.randint(1,race_steps)
        randBlack = random.randint(1,race_steps)
        
        if RedTurtle.xcor()>=600:
            print("Red Turtle wins!")
            break
        elif BlueTurtle.xcor()>=600:
            print("Blue Turtle wins!")
            break
        elif OrangeTurtle.xcor()>=600:
            print("Orange Turtle wins!")
            break
        elif BlackTurtle.xcor()>=600:
            print("Black Turtle wins!")
            break


        #RED TURTLE
        while randRed > 0:
            abs_y_Red = race_track_cor[inc_Red][1] - RedTurtle.ycor() + 450
            abs_x_Red = race_track_cor[inc_Red][0] - RedTurtle.xcor() - 600

            if abs_x_Red > 0:
                RedTurtle.setheading(0)
                RedTurtle.forward(min(randRed, abs_x_Red))
                randRed -= min(randRed, abs_x_Red)

            if randRed == 0:
                continue

            if abs_y_Red > 0:
                if abs_y_Red != 0:
                    RedTurtle.setheading(90)
                RedTurtle.forward(min(randRed, abs_y_Red))
                randRed -= min(randRed, abs_y_Red)
            
            if randRed == 0:
                continue

            if abs_y_Red < 0:
                if abs_y_Red != 0:
                    RedTurtle.setheading(-90)
                RedTurtle.forward(min(randRed, abs(abs_y_Red)))
                randRed -= min(randRed, abs(abs_y_Red))

            if randRed == 0:
                continue

            if randRed > 0:
                inc_Red += 1
                if inc_Red >= len(race_track_cor):
                    break
        
        if inc_Red < len(race_track_cor):
            if RedTurtle.xcor() == race_track_cor[inc_Red][0] and RedTurtle.ycor() == race_track_cor[inc_Red][1]:
                inc_Red +=1
                

        #BlUE TURTLE
        while randBlue > 0:
            abs_y_Blue = race_track_cor[inc_Blue][1] - BlueTurtle.ycor() + 150
            abs_x_Blue = race_track_cor[inc_Blue][0] - BlueTurtle.xcor() - 600

            if abs_x_Blue > 0:
                BlueTurtle.setheading(0)
                BlueTurtle.forward(min(randBlue, abs_x_Blue))
                randBlue -= min(randBlue, abs_x_Blue)

            if randBlue == 0:
                continue

            if abs_y_Blue > 0:
                if abs_y_Blue != 0:
                    BlueTurtle.setheading(90)
                BlueTurtle.forward(min(randBlue, abs_y_Blue))
                randBlue -= min(randBlue, abs_y_Blue)
            
            if randBlue == 0:
                continue

            if abs_y_Blue < 0:
                if abs_y_Blue != 0:
                    BlueTurtle.setheading(-90)
                BlueTurtle.forward(min(randBlue, abs(abs_y_Blue)))
                randBlue -= min(randBlue, abs(abs_y_Blue))

            if randBlue == 0:
                continue

            if randBlue > 0:
                inc_Blue += 1
                if inc_Blue >= len(race_track_cor):
                    break

        if inc_Blue < len(race_track_cor):
            if BlueTurtle.xcor() == race_track_cor[inc_Blue][0] and BlueTurtle.ycor() == race_track_cor[inc_Blue][1]:
                inc_Blue +=1


        #ORANGE TURTLE
        while randOrange > 0:
            abs_y_Orange = race_track_cor[inc_Orange][1] - OrangeTurtle.ycor() - 150
            abs_x_Orange = race_track_cor[inc_Orange][0] - OrangeTurtle.xcor() - 600

            if abs_x_Orange > 0:
                OrangeTurtle.setheading(0)
                OrangeTurtle.forward(min(randOrange, abs_x_Orange))
                randOrange -= min(randOrange, abs_x_Orange)

            if randOrange == 0:
                continue

            if abs_y_Orange > 0:
                if abs_y_Orange != 0:
                    OrangeTurtle.setheading(90)
                OrangeTurtle.forward(min(randOrange, abs_y_Orange))
                randOrange -= min(randOrange, abs_y_Orange)
            
            if randOrange == 0:
                continue

            if abs_y_Orange < 0:
                if abs_y_Orange != 0:
                    OrangeTurtle.setheading(-90)
                OrangeTurtle.forward(min(randOrange, abs(abs_y_Orange)))
                randOrange -= min(randOrange, abs(abs_y_Orange))

            if randOrange == 0:
                continue

            if randOrange > 0:
                inc_Orange += 1
                if inc_Orange >= len(race_track_cor):
                    break

        if inc_Orange < len(race_track_cor):
            if OrangeTurtle.xcor() == race_track_cor[inc_Orange][0] and OrangeTurtle.ycor() == race_track_cor[inc_Orange][1]:
                inc_Orange +=1



        #BLACK TURTLE
        while randBlack > 0:
            abs_y_Black = race_track_cor[inc_Black][1] - BlackTurtle.ycor() - 450
            abs_x_Black = race_track_cor[inc_Black][0] - BlackTurtle.xcor() - 600

            if abs_x_Black > 0:
                BlackTurtle.setheading(0)
                BlackTurtle.forward(min(randBlack, abs_x_Black))
                randBlack -= min(randBlack, abs_x_Black)

            if randBlack == 0:
                continue

            if abs_y_Black > 0:
                if abs_y_Black != 0:
                    BlackTurtle.setheading(90)
                BlackTurtle.forward(min(randBlack, abs_y_Black))
                randBlack -= min(randBlack, abs_y_Black)
            
            if randBlack == 0:
                continue

            if abs_y_Black < 0:
                if abs_y_Black != 0:
                    BlackTurtle.setheading(-90)
                BlackTurtle.forward(min(randBlack, abs(abs_y_Black)))
                randBlack -= min(randBlack, abs(abs_y_Black))

            if randBlack == 0:
                continue

            if randBlack > 0:
                inc_Black += 1
                if inc_Black >= len(race_track_cor):
                    break

        if inc_Black < len(race_track_cor):
            if BlackTurtle.xcor() == race_track_cor[inc_Black][0] and BlackTurtle.ycor() == race_track_cor[inc_Black][1]:
                inc_Black +=1


    print("Would you like to play a new game (y/n)?")
    choice = input()
    if choice == "y":
        turtle.clearscreen()
        race_track_cor = [[0,0],[race_steps_tracks,0]]
        continue
    elif choice == "n":
        exit()