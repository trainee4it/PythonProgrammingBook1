# orintiung thge game board
#Take player input
#Check for in or Tie
#switch player


board = ["-", "-","-",
        "-", "-","-",
        "-", "-","-",]

current_player = "X"
winner = None
game_running = True

#Printing the game board

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")

#Take player input

def player_input(board):
    inp = int(input("enter a number 1-9"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print(f" {inp} this is taken")


#Check for win or tie
