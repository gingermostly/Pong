#Simple Pong app built in Python

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop window from updating to improve speed and performance

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #set animation speed to maximum
paddle_a.shape("square") #give paddle shape using built-in square shape
paddle_a.color("white")
paddle_a.penup() #prevent line from being drawn
paddle_a.goto(-350, 0) #vertically center paddle in middle of screen
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #stretch paddle width to 100px (5 times 20px default)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0) 
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Main game loop

while True:
    wn.update() #update screen each time loop runs
