#!/usr/bin/env python3

#------------------------------------------------------------------------------

import turtle
import random
import time
import os
import sys

#------------------------------------------------------------------------------

# Delay
delay = 0.01

# Game score
score = 0
lives = 10

# Main Window
window = turtle.Screen()
window.title("Falling Skies by Patrick")
window.bgpic("background.gif")
window.setup(width = 800, height = 600)
window.tracer(0) # Turns off any screen updates

window.register_shape("falling_enemies.gif")
window.register_shape("falling_people.gif")
window.register_shape("player.gif")

# Add the player
player = turtle.Turtle()
player.speed(0) # Draw at the fastest speed
player.shape("player.gif")
player.color("white")
player.penup() # Avoid drawing a line when player moves
player.goto(0, -250) # Start player at the bottom of screen
player.direction = "stop" # Want player to not move when game starts

# Create a list of falling_people
falling_people_list = []

# Add the falling_people
for i in range(10):
    falling_people = turtle.Turtle()
    falling_people.speed(0) # Draw at the fastest speed
    falling_people.shape("falling_people.gif")
    falling_people.color("blue")
    falling_people.penup() # Avoid drawing a line when player moves
    falling_people.goto(-100, 250) # Start player at the bottom of screen
    falling_people.speed = random.randint(1, 6) # Speed become a random number between 1 and 4 
    falling_people_list.append(falling_people)

# Create a list of falling_enemies
falling_enemies_list = []

# Add the falling_enemies
for i in range(10):
    falling_enemies = turtle.Turtle()
    falling_enemies.speed(0) # Draw at the fastest speed
    falling_enemies.shape("falling_enemies.gif")
    falling_enemies.color("red")
    falling_enemies.penup() # Avoid drawing a line when player moves
    falling_enemies.goto(100, 250) # Start player at the bottom of screen
    falling_enemies.speed = random.randint(1, 6) # Speed become a random number between 1 and 4 
    falling_enemies_list.append(falling_enemies)

# Write the scoreboard in box
pen = turtle.Turtle()
pen.hideturtle() # Hide turtle on screen but we can still use it
pen.speed(0) # Draw at the fastest speed
pen.color("white")
pen.penup() # Avoid drawing a line when player moves
pen.goto(0, 260)
pen.write("Score: {}  Lives: {}".format(score, lives), align = "center", font = ("Courier", 24, "normal"))

# Functions
def go_left():
    player.direction = "left"
    
def go_right():
    player.direction = "right"  

def keyboard_actions():

    # Keyboard actions
    window.listen()
    window.onkeypress(go_left, "Left")
    window.onkeypress(go_right, "Right")
    
def clear_score():
    pen.clear() # Before updating the scoreboard, clear it            
    pen.write("Score: {}  Lives: {}".format(score, lives), align = "center", font = ("Courier", 24, "normal"))    

def reset_game():
    sys.exit()      

while True:
    # Update screen
    window.update()
    
    keyboard_actions()
    
    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
        
    # Move the player
    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)
        
    #------------------------------------------------------------------------------
        
    for falling_people in falling_people_list: # For every falling_person in the list

        # Moving the falling person
        y = falling_people.ycor()
        y -= falling_people.speed
        falling_people.sety(y) # The new y coordinate
        
        # Once the falling_person passes the box edge
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400) # Start off the screen
            falling_people.goto(x, y)
        
        # Check for a collision of falling_enemies with the player
        if falling_people.distance(player) < 40: # 20 because the turtle pixels are around 20px big
            os.system("afplay Score.mp3&")
            x = random.randint(-380, 380)
            y = random.randint(300, 400) # Start off the screen       
            falling_people.goto(x, y)
            score += 10
            clear_score()
            
        if lives < 0:
            reset_game()
    
    #------------------------------------------------------------------------------
    
    for falling_enemies in falling_enemies_list: # For every falling_person in the list
        
        # Moving the falling enemies
        y = falling_enemies.ycor()
        y -= falling_enemies.speed
        falling_enemies.sety(y) # The new y coordinate
        
        # Once the falling_enemies passes the box edge
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400) # Start off the screen
            falling_enemies.goto(x, y)
        
        # Check for a collision of falling_enemies with the player
        if falling_enemies.distance(player) < 40: # 20 because the turtle pixels are around 20px big
            os.system("afplay Lives.mp3&")
            x = random.randint(-380, 380)
            y = random.randint(300, 400) # Start off the screen       
            falling_enemies.goto(x, y)  
            score -= 10
            lives -= 1
            clear_score()
            
        if lives < 0:
            reset_game()

    time.sleep(delay)
    
#------------------------------------------------------------------------------

window.mainloop()
