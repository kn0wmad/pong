# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
time = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    if LEFT == False:
        direction = RIGHT
        ball_vel = [20, -20]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        return ball_vel, direction, ball_pos
    
    else:
        direction = LEFT
        ball_vel = [-20, -20]
        ball_pos[0] += ball_vel[0]
        return ball_vel, direction, ball_pos
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def gameTime():
    global time
    time += 1
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    spawn_ball(RIGHT)
    ball_pos[0] = ball_pos[0] + time + ball_vel[0]
    ball_pos[1] = ball_pos[1] + time + ball_vel[1]
    # draw ballb
    c.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 5, "Green")
    # update paddle's vertical position, keep paddle on the screen
    print (ball_pos)
    # draw paddles
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(100, gameTime)


# start frame
new_game()
frame.start()
timer.start()

