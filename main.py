from time import sleep
from os import system, name
from time import sleep
import random
  
# define our clear screen function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# function that display board
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# function that get player's marker option
def get_player_marker_choice():
    user_input=''
    while True:
        user_input=input('Player 1: Do you want to be X or O? ').upper()
        if not (user_input=='X'or user_input=='O'):
            print('\n*** Please choose only X or O ***')
        else: break
    return ('X', 'O') if user_input=='X' else ('O','X')

# place marker from player's move
def place_marker(board, marker, position):
    board[position] = marker

# check win condition for end game
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# randomly choose which player go first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# check valid empty position on board
def space_check(board, position):
    return board[position] == ' '

# check if the board is full for a draw
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# ask user next move on the board
def get_next_move(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# method that ask given phrase and return yes/no answer
def get_polar_question(phrase):
    user_input=''
    while True:
        user_input=input(phrase).lower()
        if not (user_input=='y'or user_input=='n'):
            print('\n*** Choose Y or N only ***')
        else: break
    return True if user_input=='y' else False

def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = get_player_marker_choice()
        turn = choose_first()
        print(turn + ' will go first.')

        game_on = get_polar_question('Are you ready to play? Enter Yes or No.')

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                display_board(theBoard)
                position = get_next_move(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(theBoard)
                position = get_next_move(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
                        
        if not get_polar_question('Do you want to play again? Enter Yes or No: '):
            break

if __name__ == "__main__":
    main()