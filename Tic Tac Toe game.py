from IPython.display import clear_output

def display_board(board):
    clear_output() 
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
    
def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, mark):    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
            (board[4] == mark and board[5] == mark and board[6] == mark) or 
            (board[1] == mark and board[2] == mark and board[3] == mark) or 
            (board[7] == mark and board[4] == mark and board[1] == mark) or 
            (board[8] == mark and board[5] == mark and board[2] == mark) or 
            (board[9] == mark and board[6] == mark and board[3] == mark) or 
            (board[7] == mark and board[5] == mark and board[3] == mark) or 
            (board[9] == mark and board[5] == mark and board[1] == mark))

# random module to randomly decide which player goes first
import random

def choose_first():
    flip = random.randint(0, 1)
    
    if flip == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '

# checks if the board is full and returns a boolean value
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# asks for a player's next position (as a number 1-9)
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
        
    return position

def replay():
    choice = input("Play again? Enter Yes or No: ").lower()
    return choice == 'yes'

# run the game
print('Welcome to Tic Tac Toe!')

while True:
    # set everything up (board, whos first, choose markers, X, O)
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    game_on = False9
                else:
                    turn = 'Player 1'

    if not replay():
        break
