import time
import turtle

#Adding pic to play with it
screen=turtle.Screen()
screen.bgcolor("black")
screen.addshape('Spongebob.gif')
screen.bgcolor("black")

#Note
TEXX=turtle.Turtle()
TEXX.hideturtle()
TEXX.color("white")
TEXX.write("Please open full screen!!",False,"center",["Tahoma",20,"bold"])
time.sleep(5)
TEXX.clear()


#the turtle who i will play with
Spongebob=turtle.Turtle()
Spongebob.penup()


Spongebob.shape('Spongebob.gif')

#The danger Dot
Dot=turtle.Turtle()
Dot.hideturtle()
Dot.penup()
Dot.goto(100,120)
Dot.dot(20,"red")
Dot.pendown()
if Spongebob.xcor()==100 or Spongebob.ycor()==130:
    Dot.clear()

#the text Danger
Tex=turtle.Turtle()
Tex.hideturtle()
Tex.penup()
Tex.goto(100,130)
Tex.color("white")
Tex.write("Don't click here!!! Danger",False,"center",["Tahoma",10,"bold"])
Tex.pendown()

#Text that the turtle will say to me
Text=turtle.Turtle()
Text.hideturtle()
Text.penup()
Text.speed(0)
Text.goto(0,80)
for i in range(1):
    Text.color("white")
    Text.write("Hello Friend",False,"center",["Tahoma",10,"bold"])
    time.sleep(3)
    Text.clear()
Text.pendown()
Text.penup()
Text.goto(0,50)
for i in range(1):
    Text.color("white")
    Text.write("you can only click in any thing else the red point",False,"center",["Tahoma",10,"bold"])
    time.sleep(3)
    Text.clear()
Text.pendown()


screen2=turtle.Screen()
sponge2=turtle.Turtle()
sponge2.hideturtle()
def clicked(x,y):
    Spongebob.goto(x,y)
    if x==100 or y==120:
        Spongebob.hideturtle()
        screen.clearscreen()
        screen.bgcolor("black")
        screen.addshape("Scare.gif")
        sponge2.shape("Scare.gif")
        sponge2.showturtle()
        time.sleep(4)
        screen.clearscreen()
        screen.bgcolor("black")
        text=turtle.Turtle()
        text.hideturtle()
        text.speed(0)
        text.penup()
        text.goto(0,250)
        text.color("dark grey")
        text.write("Thanks for making me die >:(",False,"center",["Tahoma",15,"bold"])
        text.pendown()
        time.sleep(3)
    if x==100 or y==120:
        screen.bgcolor("black")
        text1=turtle.Turtle()
        text1.color("red")
        text1.write("Hope you're happy now",False,"center",["Engravers MT",40,"bold"])
        text1.hideturtle()
        time.sleep(3)

for i in range(10):
    screen.onscreenclick(clicked)

turtle.mainloop()