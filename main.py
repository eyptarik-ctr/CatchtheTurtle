import turtle
from turtle import*
from random import*
#Root
root = Screen()
root.bgcolor("black")
root.title("Catch the turtle")
root.listen()

#Setings
FONT = ("Arial" ,25 ,"normal")
dificult = 10



#X , Y
x_coordinates = [-30 ,-20 ,-10 ,0 ,10 ,20 ,30]
y_coordinates = [-30 ,-20 ,-10 ,0 ,10 ,20 ,30]
turtleList = []
score = 0
#Turtle
def scoreTurtle():
    global timeTurtle
    timeTurtle = Turtle()
    timeTurtle.penup()
    timeTurtle.setpos(0, 340)
    timeTurtle.color("dark blue")
    timeTurtle.hideturtle()
    timeTurtle.write(arg=f"Score: {score}", align="center", font=FONT)


def TurtleMaker(a ,b):
    T = Turtle()
    def turtleClick(a,b):
        global score
        timeTurtle.clear()
        score += 1
        timeTurtle.write(arg=f"Score: {score}", align="center", font=FONT)


    T.onclick(turtleClick)
    T.penup()
    T.color("blue")
    T.shape("turtle")
    T.turtlesize(3)
    T.goto(a,b)
    turtleList.append(T)

def TurtleGenerate():
    for x in x_coordinates:
        for y in y_coordinates:
            TurtleMaker(x*dificult , y*dificult)

def TurtleHider():
    for h in turtleList:
        h.hideturtle()

def TurtleShower():

    choice(turtleList).showturtle()
    root.ontimer(TurtleShower , 1500)
    root.ontimer(TurtleHider,1500)
def timerr(remainingTime):
    global timeTurtle
    timeTurtle = Turtle()
    timeTurtle.penup()
    timeTurtle.setpos(0, 300)
    timeTurtle.color("dark blue")
    timeTurtle.clear()
    timeTurtle.hideturtle()

    if remainingTime > 0 :
        timeTurtle.clear()
        timeTurtle.write(arg=f"time : {remainingTime}", align="center", font=FONT)
        root.ontimer(lambda: timerr(remainingTime -1), 1000)
    else :
        timeTurtle.clear()
        timeTurtle.write(arg="game over", align="center", font=FONT)

turtle.tracer(0)
scoreTurtle()
TurtleGenerate()
TurtleHider()
TurtleShower()
timerr(10)
turtle.tracer(1)



root.mainloop()