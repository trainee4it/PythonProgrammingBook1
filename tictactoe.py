import random
 
print("Welcome to Tic Tact Toe")
print("-----------------------")
 
game_running = True
user_piece = "X"
user_number = None
possible_numbers = (1,2,3,4,5,6,7,8,9)
game_board = [1,2,3,4,5,6,7,8,9]
 

def print_gameboard(game):
    for x in range(3):
        print("+---+---+---+")
        for y in range(3):
            print("|",game[x*3+y], end = " ")
        print("|")
    print("+---+---+---+")
 
def legal_move(game,user_number):
    if game[user_number - 1] not in ('X','O'):
        return True
    else:
        return False
 

def get_user_move(game):
    user_number = int(input("Pick a number between 1 and 9 : "))
    while not legal_move(game, user_number):
        print("This is not a legal move. There is an X or O there already. Try again.")
        user_number = int(input("Pick a number between 1 and 9 : "))
    return user_number
 
def check_won(game):
    # check rows
    for i in range(3):
        if game[i*3] == game[i*3+1] == game[i*3+2] and game[i*3] in ('X', 'O'):
            return True
    # check columns
    for i in range(3):
        if game[i] == game[i+3] == game[i+6] and game[i] in ('X', 'O'):
            return True
    # check diagonals
    if game[0] == game[4] == game[8] and game[0] in ('X', 'O'):
        return True
    if game[2] == game[4] == game[6] and game[2] in ('X', 'O'):
        return True
    # no winner
    return False
 
def computer_move(game,user_piece):
    for i in range(9):
        if legal_move(user_number):
            game[i] = user_piece


def check_won2(game):
    # check rows
    for i in range(3):
        if game[i*3] == game[i*3+1] == game[i*3+2] and game[i*3] in ('X', 'O'):
            return game[i*3]
    # check columns
    for i in range(3):
        if game[i] == game[i+3] == game[i+6] and game[i] in ('X', 'O'):
            return game[i]
    # check diagonals
    if game[0] == game[4] == game[8] and game[0] in ('X', 'O'):
        return game[0]
    if game[2] == game[4] == game[6] and game[2] in ('X', 'O'):
        return game[2]
    # check tie
    if all(x in ('X', 'O') for x in game):
        return 'Tie'
    # no winner or tie
    return False
 
def hail_the_winner(user_piece,the_victor):
    if the_victor != 'Tie':
        print(f"Congratulations player {user_piece}")
    else:
        print("No one is the victor, it is a draw ")
   
 

def switch_players(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'


def modify_board(game):
    game[user_number - 1] = user_piece



while not check_won2(game_board):
    print_gameboard(game_board)
   
    user_number = int(input("Pick a number between 1 and 9 : "))

    while legal_move(game_board,user_number) == False:
        print( "This is not a legal move there is an X or Y there already try again ")
        user_number = int(input("Pick a number between 1 and 9 : "))
    modify_board(game_board)
    if not check_won2(game_board):
       user_piece = switch_players(user_piece)
 
the_victor = check_won2(game_board)
hail_the_winner(user_piece = user_piece, the_victor=the_victor)
print_gameboard(game_board)