# Ping Pong Play App
#### import needed modules ####
import turtle

#### Game Window Preparation ####
wind = turtle.Screen()
wind.title('Ping Pong Game By Energy')
wind.bgcolor('black')
wind.setup(width = 800, height = 600)
wind.tracer(0)   # stop the window automatically updating 


#### Game Objects ####
# madrab_1
madrab_1 = turtle.Turtle()
madrab_1.speed(0)
madrab_1.shape("square")
madrab_1.color("blue")
madrab_1.shapesize(stretch_wid = 5, stretch_len = 1)
madrab_1.penup()
madrab_1.goto(-350, 0)

# madrab_2
madrab_2 = turtle.Turtle()
madrab_2.speed(0)
madrab_2.shape("square")
madrab_2.color("red")
madrab_2.shapesize(stretch_wid = 5, stretch_len = 1)
madrab_2.penup()
madrab_2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25


#### Score ####
score_1 = 0
score_2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 - Player 2: 0", align= "center", font=("Courier", 22, "normal"))


#### Game Functions ####
def madrab_1_up():
    y = madrab_1.ycor()
    y += 20
    madrab_1.sety(y)

def madrab_1_down():
    y = madrab_1.ycor()
    y -= 20
    madrab_1.sety(y)

def madrab_2_up():
    y = madrab_2.ycor()
    y += 20
    madrab_2.sety(y)

def madrab_2_down():
    y = madrab_2.ycor()
    y -= 20
    madrab_2.sety(y)


#### Keyboard Bindings ####
wind.listen()
# madrab_1
wind.onkeypress(madrab_1_up, "w")
wind.onkeypress(madrab_1_down, "s")
# madrab_2
wind.onkeypress(madrab_2_up, "Up")
wind.onkeypress(madrab_2_down, "Down")


#### Game Loop ####
while True:
    # update the game window
    wind.update()
    
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # check the border
    # up
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # down
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        score.clear()
        score.write("Player 1: {} - Player 2: {}".format(score_1, score_2), align= "center", font=("Courier", 22, "normal"))  
    # left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        score.clear()
        score.write("Player 1: {} - Player 2: {}".format(score_1, score_2), align= "center", font=("Courier", 22, "normal"))  
        
    # check madrab and ball hitting
    # madrab_1
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab_1.ycor() + 40 and ball.ycor() > madrab_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    # madrab_2
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab_2.ycor() + 40 and ball.ycor() > madrab_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1