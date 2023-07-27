import random
 
#game_running = True
#user_piece = "X"

possible_numbers = (1,2,3,4,5,6,7,8,9)

 
def show_instructions():
    print("Welcome to Tic Tact Toe")
    print("-----------------------")
 

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
 
def hail_the_winner(the_victor):
    if the_victor != 'Tie':
        print(f"Congratulations player {the_victor}")
    else:
        print("No one is the victor, it is a draw ")
   
 

def switch_players(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'


def modify_board(game,user_number,user_piece):
    game[user_number - 1] = user_piece

def human_move(game,user_piece):
    user_number = int(input("Pick a number between 1 and 9 : "))

    while legal_move(game,user_number) == False:
        print( "This is not a legal move there is an X or Y there already try again ")
        user_number = int(input("Pick a number between 1 and 9 : "))
    modify_board(game,user_number,user_piece)

def ai_move(game,user_piece):
    
    if game[4] not in ['X','O']:
       game[4] = user_piece
       
    else:
        for i in range(9):
            if game[i] != 'X' and game[i] != 'O':
            
                game[i] = user_piece
                break

def ai_move1(game, user_piece):
    for i in range(9):
        if game[i] not in ['X', 'O']:
            game[i] = user_piece
            break

def ai_move_evil (game,user_piece):
    
    if game[4] not in ['X','O']:
       game[4] = user_piece
       
    else:
        for i in range(9):
            if game[i] != 'X' and game[i] != 'O':
                game[i] = user_piece
                break

def main():
    user_piece = 'X'
    game_board = [1,2,3,4,5,6,7,8,9]
    while not check_won2(game_board):
        print_gameboard(game_board)
        human_move(game_board,user_piece)
    
        if not check_won2(game_board):
            user_piece = switch_players(user_piece)
            ai_move(game_board,user_piece)
            user_piece = switch_players(user_piece)

    the_victor = check_won2(game_board)
    hail_the_winner(the_victor)
    print_gameboard(game_board)


main()

