import turtle


#screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("royalblue")
screen.setup(width=1600, height=900)
screen.tracer(0)

#L_Pod
L_Pod = turtle.Turtle()
L_Pod.shape("square")
L_Pod.shapesize(stretch_wid=10, stretch_len=1)
L_Pod.penup()
L_Pod.speed(0)
L_Pod.color("orange")
L_Pod.goto(-1600 / 2 + 50, 0)

def L_go_up():
    L_Pod.sety(L_Pod.ycor() + 100)

screen.listen()
screen.onkeypress(L_go_up, "w")

def L_go_down():
    L_Pod.sety(L_Pod.ycor() - 100)

screen.listen()
screen.onkeypress(L_go_down, "s")

#R_Pod
R_Pod = turtle.Turtle()
R_Pod.shape("square")
R_Pod.shapesize(stretch_wid=10, stretch_len=1)
R_Pod.penup()
R_Pod.speed(0)
R_Pod.color("magenta")
R_Pod.goto(1600 / 2 - 50, 0)

def R_go_up():
    R_Pod.sety(R_Pod.ycor() + 100)

screen.listen()
screen.onkeypress(R_go_up, "Up")

def R_go_down():
    R_Pod.sety(R_Pod.ycor() - 100)

screen.listen()
screen.onkeypress(R_go_down, "Down")



#Ball
Ball = turtle.Turtle()
Ball.speed(1)
Ball.shape("circle")
Ball.color("yellowgreen")
Ball.shapesize(1)
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 1
Ball.dy = 1



while True:
    screen.update()
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    
    
    if Ball.ycor() < 900 / 2 :
        Ball.dy *= -1
    
    if Ball.ycor() > -900/ 2 :
        Ball.dy *= -1
    
    if Ball.xcor() < 800:
        Ball.dx *= -1
    
    if Ball.xcor() > -800:
        Ball.dx *= -1

    if Ball.xcor() <= -1600 / 2 + 50 \
    and Ball.ycor() < L_Pod.ycor() + 100 \
        and Ball.ycor() > - 100:
        Ball.dx *= -1.1
        

    if Ball.xcor() >= 1600 / 2 - 50 \
    and Ball.ycor() < R_Pod.ycor() + 100 \
        and Ball.ycor() > - 100:
        Ball.dx *= -1.1
       



    






    






