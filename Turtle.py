# Creating PONG game in Python using Turtle
import turtle


# Create screen
Screen = turtle.Screen()
Screen.title("PONG GAME")
Screen.bgcolor("white")
Screen.setup(width=1000, height=600)


# Left paddle
Left_Pad = turtle.Turtle()
Left_Pad.speed(0)
Left_Pad.shape("square")
Left_Pad.color("black")
Left_Pad.shapesize(stretch_wid=6, stretch_len=2)
Left_Pad.penup()
Left_Pad.goto(-400, 0)


# Right paddle
Right_Pad = turtle.Turtle()
Right_Pad.speed(0)
Right_Pad.shape("square")
Right_Pad.color("black")
Right_Pad.shapesize(stretch_wid=6, stretch_len=2)
Right_Pad.penup()
Right_Pad.goto(400, 0)


# Ball 
Hit_Ball = turtle.Turtle()
Hit_Ball.speed(40)
Hit_Ball.shape("circle")
Hit_Ball.color("blue")
Hit_Ball.penup()
Hit_Ball.goto(0, 0)
Hit_Ball.dx = 5
Hit_Ball.dy = -5


# Initializing the score
Left_Player = 0
Right_Player = 0


# Displaying the score
Sketch = turtle.Turtle()
Sketch.speed(0)
Sketch.color("blue")
Sketch.penup()
Sketch.hideturtle()
Sketch.goto(0, 260)
Sketch.write("Left_player : 0 Right_player: 0",
			align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically
def paddleaup():
	y = Left_Pad.ycor()
	y += 20
	Left_Pad.sety(y)


def paddleadown():
	y = Left_Pad.ycor()
	y -= 20
	Left_Pad.sety(y)


def paddlebup():
	y = Right_Pad.ycor()
	y += 20
	Right_Pad.sety(y)


def paddlebdown():
	y = Right_Pad.ycor()
	y -= 20
	Right_Pad.sety(y)


# Keyboard bindings
Screen.listen()
Screen.onkeypress(paddleaup, "e")
Screen.onkeypress(paddleadown, "x")
Screen.onkeypress(paddlebup, "Up")
Screen.onkeypress(paddlebdown, "Down")


while True:
	Screen.update()

	Hit_Ball.setx(Hit_Ball.xcor()+Hit_Ball.dx)
	Hit_Ball.sety(Hit_Ball.ycor()+Hit_Ball.dy)

	# Checking borders
	if Hit_Ball.ycor() > 280:
		Hit_Ball.sety(280)
		Hit_Ball.dy *= -1

	if Hit_Ball.ycor() < -280:
		Hit_Ball.sety(-280)
		Hit_Ball.dy *= -1

	if Hit_Ball.xcor() > 500:
		Hit_Ball.goto(0, 0)
		Hit_Ball.dy *= -1
		Left_Player += 1
		Sketch.clear()
		Sketch.write("Left_player : {} Right_player: {}".format(
					Left_Player, Right_Player), align="center",
					font=("Courier", 24, "normal"))

	if Hit_Ball.xcor() < -500:
		Hit_Ball.goto(0, 0)
		Hit_Ball.dy *= -1
		Right_Player += 1
		Sketch.clear()
		Sketch.write("Left_player : {} Right_player: {}".format(
								Left_Player, Right_Player), align="center",
								font=("Courier", 24, "normal"))

	# Paddle ball collision
	if (Hit_Ball.xcor() > 360 and
						Hit_Ball.xcor() < 370) and
						(Hit_Ball.ycor() < Right_Pad.ycor()+40 and
						Hit_Ball.ycor() > Right_Pad.ycor()-40):
		Hit_Ball.setx(360)
		Hit_Ball.dx*=-1
		
	if (Hit_Ball.xcor()<-360 and
					Hit_Ball.xcor()>-370) and
					(Hit_Ball.ycor()<Left_Pad.ycor()+40 and
						Hit_Ball.ycor()>Left_Pad.ycor()-40):
		Hit_Ball.setx(-360)
		Hit_Ball.dx*=-1
