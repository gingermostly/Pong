#Simple Pong app built in Python

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop window from updating to improve speed and performance

#Score

score_a = 0
score_b = 0

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
ball.penup() #prevents line from being drawn on screen
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

#Pen 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #hide turtle so we are only displaying text
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function for moving paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #create event listener
wn.onkeypress(paddle_a_up, "w") #call paddle_a_up function to increase y coordinate by 20px when lowercase w key is pressed
wn.onkeypress(paddle_a_down, "s")#call paddle_a_down function to decrease y coordinate by 20px when lowercase s key is pressed
wn.onkeypress(paddle_b_up, "Up") #call paddle_b_up function when up arrow key is pressed
wn.onkeypress(paddle_b_down, "Down") #call paddle_b_down function when down arrow key is pressed

#Main game loop

while True:
    wn.update() #update screen each time loop runs

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 #reset y coord and change direction when ball hits top border of screen
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_a += 1 #increase player A score when ball goes off right side of screen
        pen.clear() #clear previous score info before printing new score
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_b += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
