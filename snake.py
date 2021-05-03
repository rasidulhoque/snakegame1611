import turtle
import random
import time

#snake bodies
bodies=[]

#turtle screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)

#snake
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

def moveup():
    if head.direction!="down":
        head.diretion="up"
def movedown():
    if head.direction!="up":
        head.diretion="down"
def moveleft():
    if head.direction!="right":
        head.diretion="left"
def moveright():
    if head.direction!="left":
        head.diretion="right"
def movestop():
    head.direction="stop"

#movement
def move():
    if head.direction=="up":
       y=head.ycor()
       head.sety(y+20)
    if head.direction=="down":
       y=head.ycor()
       head.sety(y-20)
    if head.direction=="left":
       y=head.xcor()
       head.sety(x-20)  
    if head.direction=="right":
       y=head.xcor()
       head.sety(x+20)

#event handling
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")

#while true:
s.update()
if head.xcor()>290:
        head.setx(-290)
if head.xcor()>-290:
        head.setx(290)
if head.ycor()>290:
        head.sety(-290)
if head.ycor()>-290:
        head.sety(290)
        
#check collition with the food
if head.distance(food)<20:
    x=random.randint(-290,290)
    y=random.randint(-290,290)
    food.goto(x,y)
    
#increase length of the snake body
body=turtle.Turtle()
body.speed(0)
body.penup()
body.shape("square")
body.color("red")
body.fillcolor("black")
bodies.append(body)
delay=0.01

#movement of the snake body
for index in range(len(bodies) -1,0,-1):
    x=bodies[index-1].xcor()
    y=bodies[index-1].ycor()
    bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
        move()
    
#collition with the snake
for body in bodies:
    if body.distance(head)<20:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

#hide bodies
for body in bodies:
    body.ht()
    bodies.clear()
    delay=0.1
    time.sleep(delay)
    s.mainloop





































    
        













        












       
    
    












    
    
