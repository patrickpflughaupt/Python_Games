#!/usr/bin/env python3
### --------------------------------------------- ###
### ----- Copyright 2019 Patrick Pflughaupt ----- ###
### --------------------------------------------- ###
#
### ------------------------------ DESCRIPTION OF THIS SCRIPT ---------------------------------- ###
### Tic tac goe game played by the human against a computer (opponent)                           ###
### The computer is an AI model                                                                  ###
### Contains files that records score, datetime, frequency of choosing grid points               ###
### This file contains the game itself and the autoamted processes for data analysis             ###
### -------------------------------------------------------------------------------------------- ###
#

# Import lib
import time
import random
import os
import os.path
import subprocess
import csv
from time import gmtime, strftime

### ---------------------------- ###
### ----- Global Variables ----- ###
### ---------------------------- ###

player = "X"
computer = "O"
EMPTY = " "
score = 0

# Create an array of numbers for board matrix
board = [EMPTY for i in range(1,11)]
board[0] = ''

# Defining colours to add to the warning message based on the strength level below
CRED = '\033[91m'
CGREEN  = '\33[32m'
CEND = '\033[0m' # Ending the colour code

# Start of game for PLAYER
start_zero_p = '0,0,0,0,0,0,0,0,0,0'
list_p = list(start_zero_p)

# Start of game for COMPUTER
start_zero_c = '0,0,0,0,0,0,0,0,0,0'
list_c = list(start_zero_c)

### ----------------------------- ###
### ----- Utility Functions ----- ###
### ----------------------------- ###

# Check if tictactoe score database exists to avoid overriding file
if os.path.exists('tictactoe_score_database.csv'):
    print("file exists")
else:
    # Create csv file to save initial data
    config = f'''#!/usr/bin/
# Database of tictactoe scores
# Player Score YYYY-MM-DD Hours-Minutes | Computer Score YYYY-MM-DD Hours-Minutes

Player,{score},{strftime("%Y-%m-%d %H:%M", gmtime())},Computer,{score},{strftime("%Y-%m-%d %H:%M", gmtime())} \n'''
    f = open('tictactoe_score_database.csv', 'w')
    f.writelines(config)
    f.close()

# Check if database of grid point frequency exists to avoid overriding file (PLAYER)
if os.path.exists('tictactoe_gridpoint_database_player.csv'):
    print("file exists")
else:
    # Create csv file to save initial data
    insert_txt = f'''#!/usr/bin/
# Database of grid point frequencies per game
# Header: Index [1..9]
# Each row: Game
# 0,1,2,3,4,5,6,7,8,9 (PLAYER)

{strftime("%Y-%m-%d %H:%M", gmtime())},{start_zero_p}\n'''
    g = open('tictactoe_gridpoint_database_player.csv', 'w')
    g.writelines(insert_txt)
    g.close()

# Check if database of grid point frequency exists to avoid overriding file (COMPUTER)
if os.path.exists('tictactoe_gridpoint_database_computer.csv'):
    print("file exists")
else:
    # Create csv file to save initial data
    insert_txt_c = f'''#!/usr/bin/
# Database of grid point frequencies per game
# Header: Index [1..9]
# Each row: Game
# 0,1,2,3,4,5,6,7,8,9 (COMPUTER)

{strftime("%Y-%m-%d %H:%M", gmtime())},{start_zero_c}\n'''
    h = open('tictactoe_gridpoint_database_computer.csv', 'w')
    h.writelines(insert_txt_c)
    h.close()

def extract_high_score():
    out = subprocess.Popen(['bash', 'max_csv.sh'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    stdout,stderr = out.communicate()
    return (out,stdout,stderr)

### ----------------------------- ###
### ----- Helping Functions ----- ###
### ----------------------------- ###

def intro_head():
    '''
    Welcome to the game
    '''
    print(f'''{CRED}
        Welcome to Tic Tac Toe. \n
        
        Please enter a number between 1 - 9 to play the game.
        The number will corresponde to the board position as illustrated:
        
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        
        Designed by Patrick Pflughaupt [._.] {CEND}
        ''')

def board_game():
    '''
    Display tictactoe board game
    '''
    print("\n\t", board[1], "|", board[2], "|", board[3])
    print("\t", "---------")
    print("\t", board[4], "|", board[5], "|", board[6])
    print("\t", "---------")
    print("\t", board[7], "|", board[8], "|", board[9], "\n")

def win_combo(board,player):
    '''
    Combinations needed to win the game
    '''
    if (board[1]==player and board[2]==player and board[3]==player or \
        board[4]==player and board[5]==player and board[6]==player or \
        board[7]==player and board[8]==player and board[9]==player or \
        board[1]==player and board[5]==player and board[9]==player or \
        board[3]==player and board[5]==player and board[7]==player or \
        board[1]==player and board[4]==player and board[7]==player or \
        board[2]==player and board[5]==player and board[8]==player or \
        board[3]==player and board[6]==player and board[9]==player):
        return True
    else:
        return False

def computer_moves(board, player):
    '''
    Function for computer moves
    '''
    # Statistically, best moves start with any of the four corners
    best_move = [1,3,7,9]
    if board[1] != EMPTY or board[3] != EMPTY or board[7] != EMPTY or board[9] != EMPTY:
        return random.choice(best_move)

    # If computer can win, take the move
    for i in range(1,len(board)):
        if board[i] == EMPTY: # Check if the space in the board is empty
            board[i] = player
            if win_combo(board, player): # Check if player's next move is a winner and if next move the computer can win
                return i # Return value, such that the computer wins
        else:
            board[i] = EMPTY # If not a winner, then make this a space again

    while True:
        move = random.randint(1,9)
        # If the move is blank, go ahead and return, otherwise try again
        if board[move] == EMPTY:
            return move
        else:
            new_move = random.randint(1,9)
            return new_move

def tie_game():
    '''
    Function returns True if all spaces in the board are filled
    '''
    if EMPTY not in board:
        return True
    else:
        return False

def grid_point_db_player():
    '''
    Database of grid point frequencies per game
    Function for Player
    '''
    # Start of game
    start_zero_p = '0,0,0,0,0,0,0,0,0,0'
    list_p = list(start_zero_p)

    # Index that the player and computer occupy
    f = [i for i, elem in enumerate(board) if player in elem]

    # Replacing 0 with a 1 for that index for PLAYER
    for i in f:
        if i == 1:
            list_p[2] = '1'
        elif i == 2:
            list_p[4] = '1'
        elif i == 3:
            list_p[6] = '1'
        elif i == 4:
            list_p[8] = '1'
        elif i == 5:
            list_p[10] = '1'
        elif i == 6:
            list_p[12] = '1'
        elif i == 7:
            list_p[14] = '1'
        elif i == 8:
            list_p[16] = '1'
        else:
            list_p[18] = '1'

    start_zero_p = ''.join(list_p)
    return start_zero_p

def grid_point_db_computer():
    '''
    Database of grid point frequencies per game
    Function for Computer
    '''
    # Start of game
    start_zero_c = '0,0,0,0,0,0,0,0,0,0'
    list_c = list(start_zero_c)

    # Index that the player and computer occupy
    g = [i for i, elem in enumerate(board) if computer in elem]

    # Replacing 0 with a 1 for that index for COMPUTER
    for i in g:
        if i == 1:
            list_c[2] = '1'
        elif i == 2:
            list_c[4] = '1'
        elif i == 3:
            list_c[6] = '1'
        elif i == 4:
            list_c[8] = '1'
        elif i == 5:
            list_c[10] = '1'
        elif i == 6:
            list_c[12] = '1'
        elif i == 7:
            list_c[14] = '1'
        elif i == 8:
            list_c[16] = '1'
        else:
            list_c[18] = '1'

    start_zero_c = ''.join(list_c)
    return start_zero_c

def smart_reallocation():
    '''
    Smart reallocation of empty spaces across the board
    '''
    occupied_space = []
    for i,elem in enumerate(board):
        if player in elem or computer in elem:
            occupied_space.append(i)

    yes = []
    for i in range(1,10):
        if i not in occupied_space:
            yes.append(i)

    final_list = random.choice(yes)
    return final_list

def clear():
    '''
    Clear the screen
    Use it after every move is executed
    '''
    os.system("clear")

def play_again():
    '''
    Ask player to play again if game complete
    '''
    question = input(f"Do you want to play again? ({CGREEN}yes{CEND}/{CRED}no{CEND}) ")
    if question.lower().startswith('y'):
        clear()
        subprocess.call("python3 tictactoe.py", shell=True)
    if question.lower().startswith('n'):
        print("Thank you for playing tic tac toe with me! See you soon. ")
        time.sleep(2)
        exit()

def main():
    '''
    Main game function
    '''
    # Print score board
    out,stdout,stderr = extract_high_score()
    extract_high_score()
    global score
    print(f'''
{CGREEN} Player:   {score} {CEND} {CGREEN} Player's   High Score: {stdout.split()[0]}{CEND}
{CRED} Computer: {score} {CEND} {CRED} Computer's High Score: {stdout.split()[1]}{CEND}
        ''')
    
    # Player Input (X)
    choice = input("Please choose an empty space for X. (1-9) ")
    choice = int(choice)
    
    # Check if board space is empty
    if board[choice] == EMPTY:
        board[choice] = player
        score += 5 # Each successful entry earns 5 points
    else:
        print("Sorry, that space is not empty!")
        time.sleep(1)

    # If player wins
    if win_combo(board, player):
        clear()
        intro_head()
        board_game()
        print(f"{CGREEN} Player wins! Congratulations. {CEND}")
        if board.count(EMPTY) == 4:
            score += 100
            print('You took the least steps to win!')
        elif board.count(EMPTY) == 2:
            score += 50
            print('You could take less steps to win. Goal for next time!')
        else:
            score += 20
            print('You took the most number of steps to win.')

    # If computer wins
    computer_choice = computer_moves(board, computer)

    # Check to see if the space is empty first
    if board[computer_choice] == EMPTY:
        board[computer_choice] = computer
    else:
        sm = smart_reallocation()
        board[sm] = computer

    # If Computer wins
    if win_combo(board, computer):
        clear()
        intro_head()
        board_game()
        print(f"{CRED} Computer wins! Congratulations. {CEND}")
        if board.count(EMPTY) == 4:
            score += 100
            print('You took the least steps to win!')
        elif board.count(EMPTY) == 2:
            score += 50
            print('You could take less steps to win. Goal for next time!')
        else:
            score += 20
            print('You took the most number of steps to win.')

    # If game results in a tie
    if tie_game() == True:
        intro_head()
        board_game()
        print(f"{CRED} Oh no, looks like it's a Tie! {CEND}")
        score += 0
        subprocess.call(f'''
echo 'Player,{score},{strftime("%Y-%m-%d %H:%M", gmtime())},Computer,{score},{strftime("%Y-%m-%d %H:%M", gmtime())}' >> tictactoe_score_database.csv''', shell=True)
        play_again()

### ------------------------ ###
### ----- Running Game ----- ###
### ------------------------ ###

while True:
    clear()
    intro_head()
    board_game()
    main()

    if win_combo(board, player) == True or win_combo(board, computer) == True:
        subprocess.call(f'''
echo 'Player,{score},{strftime("%Y-%m-%d %H:%M", gmtime())},Computer,{score},{strftime("%Y-%m-%d %H:%M", gmtime())}' >> tictactoe_score_database.csv;
echo '{strftime("%Y-%m-%d %H:%M", gmtime())},{grid_point_db_player()}' >> tictactoe_gridpoint_database_computer.csv''', shell=True)
        play_again()
