# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
secret_number = 0
num_guess = 0
guesses_used = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = 0
     
 
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, num_guess
    secret_number = random.randrange(0,100)
    num_guess = 7
    print "secret number is", secret_number
    print "Number of remaining guesses is", num_guess
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, num_guess
    secret_number = random.randrange(0,1000)
    num_guess = 10
    print "Number of remaining guesses is", num_guess
    

def input_guess(guess): 
    global secret_number, num_guess, guesses_used 
    guesses_used += 1
    if(guesses_used < num_guess):
        input = int(guess)
        print "Guess was", input
        print "Number of remaining guesses is", num_guess - guesses_used
        if input > secret_number:
            print "lower!"
        elif input < secret_number:
            print "higher!"
        elif input == secret_number:
            print "correct!"
            guesses_used = 0
            new_game() 
    else:
        print "You ran out of guesses. The number was", secret_number
 
        
    
# create frame
frame = simplegui.create_frame('Guess_Game', 200, 200)
frame.add_button('Range 0 to 100', range100)
frame.add_button('Range 0 to 1000', range1000) 
guessvalue = frame.add_input('Guess Value', input_guess, 100) 
                           

# register event handlers for control elements and start frame

frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

