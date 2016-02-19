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
ball_vel = [0,0]
paddle1_pos = HEIGHT/2 
paddle2_pos = HEIGHT/2
score1 = 0
score2 = 0
count = 0
paddle1_vel = 0
paddle2_vel = 0
pad_acc = 10
ball_pos = [WIDTH / 2, HEIGHT / 2]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 4) 
        ball_vel[1] = - random.randrange(1, 3)
    elif direction == LEFT: 
        ball_vel[0] = - random.randrange(2, 4) 
        ball_vel[1] = - random.randrange(1, 3)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, count, LEFT, RIGHT  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT/2 
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
      
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
       
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT ), (HALF_PAD_WIDTH, paddle1_pos + 80 - HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + 80 - HALF_PAD_HEIGHT), PAD_WIDTH, "white")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]       
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "White")
    
     
    # collide and reflection of the ball from the top and bottom of wall
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # determine whether paddle and ball collide   
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):	# if it hits left wall
        # If ball position is between vertical range of paddles
        if (paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
        # else it scores, respawns ball
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):	#if it hits right wall
        # If ball position is between vertical range of paddles
        if (paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
        # else it scores, respawns ball
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    
    # draw scores
    canvas.draw_text(str(score1), [150,30], 25, "white")  
    canvas.draw_text(str(score2), [450,30], 25, "white")
    
def keydown(key):
    global paddle1_vel, paddle2_vel 
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += pad_acc    
        
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= pad_acc
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= pad_acc
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game, 100)

# start frame
frame.start()
new_game()
