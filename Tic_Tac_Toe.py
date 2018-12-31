#!/usr/bin/env python3

#------------------------------------------------------------------------------

import os
import time
import random

#------------------------------------------------------------------------------

# Define the board that holds the data
# If the board is full (i.e. no spaces left), then the game is finished
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
    
def is_player_winner(board, player):    
    if(board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
            return True
    else:
        return False
	
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

def get_computer_move(board, player):
    
    # Check for a win across the board
    for i in range(1,10):
        if board[i] == " ": # Check if the space in the board is empty
            board[i] = player
            if is_player_winner(board, player): # Check if that the combination a winner
                return i # Return value, such that the computer wins
            else:
                board[i] = " " # If not a winner, then make this a space again
    
    # If the centre square is empty, choose that box
    if board[5] == " ":
        return 5
    else:
        return random.randint(1,9)

    while True:
        move = random.randint(1,9)
        # If the move is blank, go ahead and return, otherwise try again
        if board[move] == " ":
            return move
            break

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
    if is_player_winner(board, "X"):
            os.system("clear")
            print_header()
            print_board()
            print("X wins! Congratulations.")
            break

    # If board is full, then do this
    if is_board_full(board):
        print("Tie!")
        break

    # Player Input (O)
    choice = get_computer_move(board, "O")  
    
    os.system("clear")
    print_header()
    print_board()
    
    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)
        
    # Check for X win
    if is_player_winner(board, "O"):
            os.system("clear")
            print_header()
            print_board()
            print("O wins! Congratulations.")
            break   
        
    # If board is full, then do this
    if is_board_full(board):
        print("Tie!")
        break
