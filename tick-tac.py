import sys
import random

def display_board(board):

    #clear_output()
    print(f"  {board[6]} | {board[7]}  | {board[8]} ")
    print(f"  {board[3]} | {board[4]}  | {board[5]} ")
    print(f"  {board[0]} | {board[1]}  | {board[2]} ")
    

def user_choice(): 

    marker = ""
    
    while marker != 'X' and marker !='O':
        marker = input('Player 1, choose X or O: ').upper()
    
    player1 = marker
    player2 = ' '
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print("Player1", player1)
    print("Player2", player2)
    
    return (player1, player2)


def place_marker(board,marker,position):
    board[position -1] = marker


def win_check(board,marker):
    return ((board[0] == board[1] == board[2] == marker) or 
    (board[3] == board[4] == board[5] == marker) or
    (board[0] == board[3] == board[6] == marker) or
    (board[1] == board[4] == board[7] == marker) or 
    (board[2] == board[5] == board[8] == marker) or        
    (board[0] == board[4] == board[8] == marker) or
    (board[2] == board[4] == board[6] == marker))


def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position - 1].isdigit()


def full_board_check(board):
    for i in range(0,10):
        if space_check(board, i):
            return False
    return True 


def player_choice(board):
    position = input('Choose a position 1-9: ')
    while len(position) > 1 or not position.isdigit() or int(position) not in range(1,10) or not space_check(board,int(position)):
        print("Please enter a valid input")
        position = input('Choose a position 1-9: ')
    return position 


def replay():

    user_responce = input('Would you like to play again? Enter y or n: ').lower()

    while user_responce != 'y' and user_responce != 'n':
        print('Please enter a valid input')
        user_responce = input('Would you like to play again? Enter y or n: ').lower()

    return user_responce == 'y'


while True:

    the_board = [str(i) for i in range(1,10)]
    player1_marker, player2_marker = user_choice()

    turn = choose_first()
    print(turn + ' will be starting \n')

    play_game = input('Ready to play? y or n: ').lower()
    
    while play_game != 'y' and play_game != 'n':       
        print('Please enter a valid input' + play_game)
        play_game = input('Ready to play? y or n: ').lower()
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    
    while game_on:
        print("run")
        display_board(the_board)
        if turn == 'Player 1':

            
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,int(position))

            if win_check(the_board, player1_marker):
                print('Player 1 won!')
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print('This is a tie game')
                break 
            turn = 'Player 2'
        else:
            position = player_choice(the_board)
            place_marker(the_board,player2_marker, int(position))

            if win_check(the_board, player2_marker):
                print('Player 2 won!')
                game_on = False
            elif full_board_check(the_board):
                print('This is a tie game')
                display_board(the_board)
                break
            turn = 'Player 1'

    if not replay():
        sys.exit()    




    


    







        
































