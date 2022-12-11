# Creating the PONG game on Python using CodeSkulptor

import simplegui
import random

# Global Variables
Width = 600
Height = 400       
Ball_Radius = 20
Pad_Width = 8
Pad_Height = 80
Half_Pad_Width = Pad_Width / 2
Half_Pad_Height = Pad_Height / 2
Left = False
Right = True
ball_pos = 300,200
ball_vel = 2,-7
paddle1_pos= 200
paddle2_pos = 200
paddle1_vel =  0
paddle2_vel =  0
PadDLE_VEL = 7
score1 = 0
score2 = 0

# Initialize
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = 300,200
    direction_sign = 1
    if direction == Left:
        direction_sign = -1
    ball_vel = direction_sign * random.randrange(2, 7), -random.randrange(2, 7)

def ball_bounce():
    global ball_pos, ball_vel, Ball_Radius, Height, Width, paddle1_pos, paddle2_pos, Half_Pad_Height, score1, score2
    if ball_pos[1] - Ball_Radius < 0 or ball_pos[1] + Ball_Radius > Height:
        ball_vel = ball_vel[0], -ball_vel[1] 
        
    if ball_pos[0] - Ball_Radius < 0 + Pad_Width:
        if paddle1_pos - Half_Pad_Height < ball_pos[1] < paddle1_pos + Half_Pad_Height:
            ball_vel = round(-ball_vel[0] * 1.1), round(ball_vel[1] * 1.1)
        else:
            spawn_ball(Right)
            score2 = score2 + 1
            
    if ball_pos[0] + Ball_Radius > Width - Pad_Width:
        if paddle2_pos - Half_Pad_Height < ball_pos[1] < paddle2_pos + Half_Pad_Height:
            ball_vel = -ball_vel[0] * 1.1, ball_vel[1] * 1.1
        else:
            spawn_ball(Left)
            score1 = score1 + 1
   
# Event Handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(Left)
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_line([Width / 2, 0],[Width / 2, Height], 1, "Red")
    canvas.draw_line([Pad_Width, 0],[Pad_Width, Height], 1, "Red")
    canvas.draw_line([Width - Pad_Width, 0],[Width - Pad_Width, Height], 1, "White")
        
    # update ball
    ball_pos = ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1] 
    ball_bounce()
    
    # draw ball
    canvas.draw_circle(ball_pos, Ball_Radius, 10, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel
    if paddle1_pos - Half_Pad_Height < 0:
        paddle1_pos = 0 + Half_Pad_Height
        
    if paddle1_pos + Half_Pad_Height > Height:
        paddle1_pos = Height - Half_Pad_Height
    
    if paddle2_pos - Half_Pad_Height < 0:
        paddle2_pos = 0 + Half_Pad_Height
        
    if paddle2_pos + Half_Pad_Height > Height:
        paddle2_pos = Height - Half_Pad_Height
       
    # draw paddles
    canvas.draw_line((Half_Pad_Width, (paddle1_pos - Half_Pad_Height)), (Half_Pad_Width, (paddle1_pos + Half_Pad_Height)), Pad_Width, 'White')
    canvas.draw_line((Width - Half_Pad_Width, (paddle2_pos - Half_Pad_Height)), (Width - Half_Pad_Width, (paddle2_pos + Half_Pad_Height)), Pad_Width, 'White')    
    
    # draw scores
    canvas.draw_text(str(score1), (230, 50), 40, 'Red')
    canvas.draw_text(str(score2), (350, 50), 40, 'Red')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, PadDLE_VEL
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -PadDLE_VEL
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = PadDLE_VEL
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PadDLE_VEL
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = PadDLE_VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel, PadDLE_VEL
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# Create Frame
frame = simplegui.create_frame("Pong", Width, Height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', new_game)

# Start Frame
new_game()
frame.start()
