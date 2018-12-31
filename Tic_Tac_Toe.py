#!/usr/bin/env python3

#------------------------------------------------------------------------------

import os
import time
import random

#------------------------------------------------------------------------------

# Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Print the header
def print_header():
	print("""
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    1 | 2 | 3
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      4 | 5 | 6
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     7 | 8 | 9
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\
                                                            
 To play Tic-Tac-Toe, you need to get three in a row...
 Your choices are defined, they must be from 1 to 9...

""")

# Define the print_board function 
def print_board():  
	print("   |   |   ")
	print(" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
	print("   |   |   ")
	print("---|---|---")
	print("   |   |   ")
	print(" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
	print("   |   |   ")
	print("---|---|---")
	print("   |   |   ")		
	print(" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
	print("   |   |   ")
	
while True:
    os.system("clear")
    print_header()
    print_board()
    
    # Player Input (X)
    choice = input("Please choose an empty space for X. ")
    choice = int(choice)
    
    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)
        
    # Check for X win
    if(board[1] == "X" and board[2] == "X" and board[3] == "X") or \
        (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
        (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
        (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
        (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
        (board[3] == "X" and board[5] == "X" and board[7] == "X"):
            os.system("clear")
            print_header()
            print_board()
            print("X wins! Congratulations.")
            break

    # Check for a tie (is the board full?)
    is_board_full = True
    for i in range(1, 10):
        if board[i] == " ":
            is_board_full = False
            break
 
    # If board is full, then do this
    if is_board_full == True:
        print("Tie!")
        break

    # Player Input (O)    
    os.system("clear")
    print_header()
    print_board()
    
    choice = input("Please choose an empty space for O. ")
    choice = int(choice)
    
    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)
        
    # Check for X win
    if(board[1] == "O" and board[2] == "O" and board[3] == "O") or \
        (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
        (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
        (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
        (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
        (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
        (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
        (board[3] == "O" and board[5] == "O" and board[7] == "O"):
            os.system("clear")
            print_header()
            print_board()
            print("O wins! Congratulations.")
            break   
        
    # Check for a tie (is the board full?)
    is_board_full = True
    for i in range(1, 10):
        if board[i] == " ":
            is_board_full = False
            break  
    
    # If board is full, then do this
    if is_board_full == True:
        print("Tie!")
        break