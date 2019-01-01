#!/usr/bin/env python3

#------------------------------------------------------------------------------

import turtle
import time
import random

#------------------------------------------------------------------------------

# Time delay by 1/10 of a second
delay = 0.1

# Score
score  = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game by Patrick")
window.bgcolor("green")
window.setup(width = 600, height = 600)
window.tracer(0) # Turns off the screen updates

# Create the snake head
snake_head = turtle.Turtle()
snake_head.speed(0) # 0 = fastest animation speed
snake_head.shape("square")
snake_head.color("black")
snake_head.penup() # Doesn't draw anything
snake_head.goto(0,0) # Start in the centre of the screen
snake_head.direction = "right" # When it starts, it sits in the middle

# Snake food
snake_food = turtle.Turtle()
snake_food.speed(0) # 0 = fastest animation speed
snake_food.shape("circle")
snake_food.color("red")
snake_food.penup() # Doesn't draw anything
snake_food.goto(0,100)

# List
segments = []

# Pen 
pen = turtle.Turtle()
pen.speed(0) # Animation speed
pen.shape("square")
pen.color("white")
pen.penup() # Don't want the pen to draw lines
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 24, "normal"))

# Functions 
def go_up():
    if snake_head.direction != "down": # Avoid snake_head colliding with itself
        snake_head.direction = "up"
    
def go_down():
    if snake_head.direction != "up": 
        snake_head.direction = "down"
    
def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left": 
        snake_head.direction = "right"    

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20) # if statement is true, then the snake_head will move up in y-direction 20 each time

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
        
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
        
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

def keyboard_functions():
    # Connect a keyboard action with a function
    window.listen()
    window.onkeypress(go_up, "Up")
    window.onkeypress(go_down, "Down")
    window.onkeypress(go_left, "Left")
    window.onkeypress(go_right, "Right")
    
def clear_score():
    pen.clear() # Clear original writing off the screen
    pen.write(" Score: {}  High Score : {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
    
# Main game loop
while True:
    window.update()
    keyboard_functions()
    
    # Check for a collision with the border
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000) # Places each collected segment outside of the box
        
        # Clear the segments list
        segments.clear() # Because once the loop above is executed and game is reset, the snake_food returns to the centre of the segment
                
        # Clear the score
        score = 0

        # Reset the delay
        delay = 0.1        
        
        clear_score()
        
    # Check for a collision with the food
    if snake_head.distance(snake_food) < 20:
        # Measures the distance between 2 turtles
        # 20 because each turtle is 20px tall and 20px wide
        # Centre of 1px to the outer edge is 10
        # 10 + 10 = 20, so we can say that when the distance between the 2 turtles is <20, they have collided
        # Move the food to a random spot on the screen
        x = random.randint(-290, 290) # Borders are -300, 300 but choose 290 so that turtles don't go off the screen
        y = random.randint(-290, 290)
        snake_food.goto(x, y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) 
        
        # Shorten the delay
        delay -= 0.001
        
        # Increase the score
        score += 10
        
        if score > high_score:
            high_score = score
        
        clear_score()
        
    # Move the end segments first in reverse order
    for i in range(len(segments) -1, 0, -1):
        # Goes from 9 (-1) down to 1 (0)
        # If I want segment 9 to move where segment 8 is, etc.
        # This function loops through all of them
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    
    # Move segment 0 (first one after the head) to where the snake_head is
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)
        
    move()
    
    # Check for head collisions with the body segments
    # Need to check for this after we move
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"
            
            # Clear the segments list
            segments.clear() # Because once the loop above is executed and game is reset, the snake_food returns to the centre of the segment
                
            # Clear the score
            score = 0
            
            # Reset the delay
            delay = 0.1
            
            clear_score()
            
    time.sleep(delay)        
    
#------------------------------------------------------------------------------

window.mainloop()