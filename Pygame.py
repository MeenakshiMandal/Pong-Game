# Creating PONG game in Python using Pygame

import random
import pygame, sys
from pygame.locals import *

# Colours 
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

# Global Dimensions
Width = 600
Height = 400       
Ball_Radius = 20
Pad_Width = 8
Pad_Height = 80
Half_Pad_Width = Pad_Width // 2
Half_Pad_Height = Pad_Height // 2
Ball_Pos = [0,0]
Ball_Vel = [0,0]
Paddle1_Vel = 0
Paddle2_Vel = 0
L_Score = 0
R_Score = 0

# Canvas 
Window = pygame.display.set_mode((Width, Height), 0, 32)
pygame.display.set_caption("Welcome")

# Function that returns position vector and velocity vector of ball
# If Right equals True, then Right; otherwise Left
def Ball_init(Right):
    global Ball_Pos, Ball_Vel # Vectors stored as lists
    Ball_Pos = [Width//2,Height//2]
    Horizontal = random.randrange(2,4)
    Vertical = random.randrange(1,3)
    
    if Right == False:
        Horizontal = - Horizontal
        
    Ball_Vel = [Horizontal,-Vertical]

# event Handle
def init():
    global Paddle1_Pos, Paddle2_Pos, Paddle1_Vel, Paddle2_Vel,L_Score,R_Score  # Float Variables
    global Score1, Score2  # Integer Variables
    Paddle1_Pos = [Half_Pad_Width - 1,Height//2]
    Paddle2_Pos = [Width +1 - Half_Pad_Width,Height//2]
    L_Score = 0
    R_Score = 0
    if random.randrange(0,2) == 0:
        Ball_init(True)
    else:
        Ball_init(False)

# Drawing on Canvas
def Draw(Canvas):
    global Paddle1_Pos, Paddle2_Pos, Ball_Pos, Ball_Vel, L_Score, R_Score
           
    Canvas.fill(Blue)
    pygame.draw.line(Canvas, White, [Width // 2, 0],[Width // 2, Height], 1)
    pygame.draw.line(Canvas, White, [Pad_Width, 0],[Pad_Width, Height], 1)
    pygame.draw.line(Canvas, White, [Width - Pad_Width, 0],[Width - Pad_Width, Height], 1)
    pygame.draw.circle(Canvas, White, [Width // 2, Height // 2], 70, 1)

    # Paddle's Vertical Position
    if Paddle1_Pos[1] > Half_Pad_Height and Paddle1_Pos[1] < Height - Half_Pad_Height:
        Paddle1_Pos[1] += Paddle1_Vel
    elif Paddle1_Pos[1] == Half_Pad_Height  and Paddle1_Vel > 0:
        Paddle1_Pos[1] += Paddle1_Vel
    elif Paddle1_Pos[1] == Height - Half_Pad_Height  and Paddle1_Vel < 0:
        Paddle1_Pos[1] += Paddle1_Vel
    
    if Paddle2_Pos[1] > Half_Pad_Height  and Paddle2_Pos[1] < Height - Half_Pad_Height :
        Paddle2_Pos[1] += Paddle2_Vel
    elif Paddle2_Pos[1] == Half_Pad_Height  and Paddle2_Vel > 0:
        Paddle2_Pos[1] += Paddle2_Vel
    elif Paddle2_Pos[1] == Height - Half_Pad_Height  and Paddle2_Vel < 0:
        Paddle2_Pos[1] += Paddle2_Vel

    # Update Ball Position
    Ball_Pos[0] += int( Ball_Vel[0])
    Ball_Pos[1] += int( Ball_Vel[1])

    # Drawing Ball and Paddles
    pygame.draw.circle( Canvas, Red, Ball_Pos, 20, 0)
    pygame.draw.polygon( Canvas, Green, [[Paddle1_Pos[0] - Half_Pad_Width, Paddle1_Pos[1] - Half_Pad_Height], [Paddle1_Pos[0] - Half_Pad_Width, Paddle1_Pos[1] + Half_Pad_Height], [Paddle1_Pos[0] + Half_Pad_Width, Paddle1_Pos[1] + Half_Pad_Height], [Paddle1_Pos[0] + Half_Pad_Width, Paddle1_Pos[1] - Half_Pad_Height]], 0)
    pygame.draw.polygon( Canvas, Green, [[Paddle2_Pos[0] - Half_Pad_Width, Paddle2_Pos[1] - Half_Pad_Height], [Paddle2_Pos[0] - Half_Pad_Width, Paddle2_Pos[1] + Half_Pad_Height], [Paddle2_Pos[0] + Half_Pad_Width, Paddle2_Pos[1] + Half_Pad_Height], [Paddle2_Pos[0] + Half_Pad_Width, Paddle2_Pos[1] - Half_Pad_Height]], 0)

    # Ball Collision on Top and Bottom Walls
    if int(Ball_Pos[1]) <= Ball_Radius:
         Ball_Vel[1] = -  Ball_Vel[1]
    if int(Ball_Pos[1]) >= Height + 1 - Ball_Radius:
         Ball_Vel[1] = - Ball_Vel[1]

    # Ball Collision on Gutters and Paddles
    if int(Ball_Pos[0]) <= Ball_Radius + Pad_Width and int(Ball_Pos[1]) in range(Paddle1_Pos[1] - Half_Pad_Height,Paddle1_Pos[1] + Half_Pad_Height,1):
        Ball_Vel[0] = -Ball_Vel[0]
        Ball_Vel[0] *= 1.1
        Ball_Vel[1] *= 1.1
    elif int(Ball_Pos[0]) <= Ball_Radius + Pad_Width:
        R_Score += 1
        Ball_init(True)
        
    if int(Ball_Pos[0]) >= Width + 1 - Ball_Radius - Pad_Width and int(Ball_Pos[1]) in range(Paddle2_Pos[1] - Half_Pad_Height,Paddle2_Pos[1] + Half_Pad_Height,1):
        Ball_Vel[0] = -Ball_Vel[0]
        Ball_Vel[0] *= 1.1
        Ball_Vel[1] *= 1.1
    elif int(Ball_Pos[0]) >= Width + 1 - Ball_Radius - Pad_Width:
        L_Score += 1
        Ball_init(False)

    # Update of Score
    Myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    Label1 = Myfont1.render("Score "+str(L_Score), 1, (255,255,0))
    Canvas.blit(Label1, (50,20))

    Myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    Label2 = Myfont2.render("Score "+str(R_Score), 1, (255,255,0))
    Canvas.blit(Label2, (470, 20))  


# Keydown
def keydown(event):
    global Paddle1_Vel, Paddle2_Vel
    
    if event.key == K_UP:
        Paddle2_Vel = -8
    elif event.key == K_DOWN:
        Paddle2_Vel = 8
    elif event.key == K_w:
        Paddle1_Vel = -8
    elif event.key == K_s:
        Paddle1_Vel = 8

# Keyup
def keyup(event):
    global Paddle1_Vel, Paddle2_Vel
    
    if event.key in (K_w, K_s):
        Paddle1_Vel = 0
    elif event.key in (K_UP, K_DOWN):
        Paddle2_Vel = 0

init()


# Game Loop
while True:

    Draw(Window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            Keydown(event)
        elif event.type == KEYUP:
            Keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)
