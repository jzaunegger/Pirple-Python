# Import dependencies
import sys, random

# Create an empty gameboard
def initBoard():
    board = []
    for i in range(6):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

# Draw the current game board
def drawBoard(board):
    horiz_line = "|---------------------------|"
    index_line = "| 0   1   2   3   4   5   6 |"
    print(horiz_line)

    for row in board:
        boardline = '| '
        for col in row:
            boardline += col + ' | '
        print(boardline)
        print(horiz_line)

    print(index_line)
    print(horiz_line)
    print(" ")

# Get the status of a current column
def getColumn(gameboard, column_index):
    values = []
    
    for row_index in range(len(gameboard)):
        for col_index in range(len(gameboard[row_index])):
            
            current_value = gameboard[row_index][column_index]
            if col_index == column_index:
                if current_value == ' ':
                    values.append( [True, row_index, col_index] )
                else:
                    values.append( [False, row_index, col_index] )
    return(values)

# Check if the column has a valid move
def checkColumn(column):
    for space in range(len(column)):
        if column[space][0] == True:
            return True

    return False

# Place a peice in the board
def placePeice(gameboard, column, symbol):
    for space in range( len(column)-1, -1, -1):
        if column[space][0] == True:
            gameboard[column[space][1]][column[space][2]] = symbol
            break
    return gameboard

# Have the computer randomly choose a space
def computerRandomMove(gameboard, symbol):
    valid_moves = []
    for i in range(6):
        current_col = getColumn(gameboard, i)
        if checkColumn(current_col):
            valid_moves.append(current_col)

    placePeice(gameboard, random.choice(valid_moves), symbol)

def containsTrue(vals):
    hasTrue = False
    for val in vals:
        if val == True:
            hasTrue = True

    return hasTrue

# Check if there is a winner
def checkWinner(gameboard, symbol):


    '''     0  1  2  3  4  5  6
        0   _  _  _  _  _  _  _      
        1   _  _  _  _  _  _  _      
        2   _  _  _  _  _  _  _      
        3   _  _  _  _  _  _  _      
        4   _  _  _  _  _  _  _      
        5   _  _  _  _  _  _  _      

    '''

    winning_spaces = {
        "diag-lr": [
            [(2, 0), (3, 1), (4, 2), (5, 3)],
            [(1, 0), (2, 1), (3, 2), (4, 3)],
            [(2, 1), (3, 2), (4, 3), (5, 4)],
            [(0, 0), (1, 1), (2, 2), (3, 3)],
            [(1, 1), (2, 2), (3, 3), (4, 4)],
            [(2, 2), (3, 3), (4, 4), (5, 5)],
            [(0, 1), (1, 2), (2, 3), (3, 4)],
            [(1, 2), (2, 3), (3, 4), (4, 5)],
            [(2, 3), (3, 4), (4, 5), (5, 6)],
            [(0, 2), (1, 3), (2, 4), (3, 5)],
            [(1, 3), (2, 4), (3, 5), (4, 6)],
            [(0, 3), (1, 4), (2, 5), (3, 6)]
        ],

        "diag-rl": [
            [(2, 6), (3, 5), (4, 4), (5, 3)],
            [(1, 6), (2, 5), (3, 4), (4, 3)],
            [(2, 5), (3, 4), (4, 3), (5, 2)],
            [(0, 6), (1, 5), (2, 4), (3, 3)],
            [(1, 5), (2, 4), (3, 3), (4, 2)],
            [(2, 4), (3, 3), (4, 2), (5, 1)],
            [(0, 5), (1, 4), (2, 3), (3, 2)],
            [(1, 4), (2, 3), (3, 2), (4, 1)],
            [(2, 3), (3, 2), (4, 1), (5, 0)],
            [(0, 4), (1, 3), (2, 2), (3, 1)],
            [(1, 3), (2, 2), (3, 1), (4, 0)],
            [(0, 3), (1, 2), (2, 1), (3, 0)],
        ],

        "horizontal-wins": [
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(0, 1), (0, 2), (0, 3), (0, 4)],
            [(0, 2), (0, 3), (0, 4), (0, 5)],
            [(0, 3), (0, 4), (0, 5), (0, 6)],

            [(1, 0), (1, 1), (1, 2), (1, 3)],
            [(1, 1), (1, 2), (1, 3), (1, 4)],
            [(1, 2), (1, 3), (1, 4), (1, 5)],
            [(1, 3), (1, 4), (1, 5), (1, 6)],

            [(2, 0), (2, 1), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 3), (2, 4)],
            [(2, 2), (2, 3), (2, 4), (2, 5)],
            [(2, 3), (2, 4), (2, 5), (2, 6)],

            [(3, 0), (3, 1), (3, 2), (3, 3)],
            [(3, 1), (3, 2), (3, 3), (3, 4)],
            [(3, 2), (3, 3), (3, 4), (3, 5)],
            [(3, 3), (3, 4), (3, 5), (3, 6)],

            [(4, 0), (4, 1), (4, 2), (4, 3)],
            [(4, 1), (4, 2), (4, 3), (4, 4)],
            [(4, 2), (4, 3), (4, 4), (4, 5)],
            [(4, 3), (4, 4), (4, 5), (4, 6)],
        
            [(5, 0), (5, 1), (5, 2), (5, 3)],
            [(5, 1), (5, 2), (5, 3), (5, 4)],
            [(5, 2), (5, 3), (5, 4), (5, 5)],
            [(5, 3), (5, 4), (5, 5), (5, 6)],
        ],

        "vertical-wins": [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(1, 0), (2, 0), (3, 0), (4, 0)],
            [(2, 0), (3, 0), (4, 0), (5, 0)],

            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(1, 1), (2, 1), (3, 1), (4, 1)],
            [(2, 1), (3, 1), (4, 1), (5, 1)],

            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(1, 2), (2, 2), (3, 2), (4, 2)],
            [(2, 2), (3, 2), (4, 2), (5, 2)],

            [(0, 3), (1, 3), (2, 3), (3, 3)],
            [(1, 3), (2, 3), (3, 3), (4, 3)],
            [(2, 3), (3, 3), (4, 3), (5, 3)],

            [(0, 4), (1, 4), (2, 4), (3, 4)],
            [(1, 4), (2, 4), (3, 4), (4, 4)],
            [(2, 4), (3, 4), (4, 4), (5, 4)],

            [(0, 5), (1, 5), (2, 5), (3, 5)],
            [(1, 5), (2, 5), (3, 5), (4, 5)],
            [(2, 5), (3, 5), (4, 5), (5, 5)],

            [(0, 6), (1, 6), (2, 6), (3, 6)],
            [(1, 6), (2, 6), (3, 6), (4, 6)],
            [(2, 6), (3, 6), (4, 6), (5, 6)]
        ]
    }
    
    won_found = False

    # Check for wins in horizontal spaces
    horizontal_spaces = winning_spaces['horizontal-wins']

    for space in horizontal_spaces:
        vals = []
        for entry in space:
            entry_val = gameboard[entry[0]][entry[1]]
            if entry_val == symbol:
                vals.append(True)
            else:
                vals.append(False)

        if vals[0] == True and vals[1] == True and vals[2] == True and vals[3] == True:
            win_found = True
            print("---------------------------------------------------------------------")
            print("Horizontal Win found for", symbol)
            print("---------------------------------------------------------------------")
            sys.exit()

    # Check for wins in vertical spaces
    vertical_spaces = winning_spaces['vertical-wins']
    for space in vertical_spaces:
        vals = []
        for entry in space:
            entry_val = gameboard[entry[0]][entry[1]]
            if entry_val == symbol:
                vals.append(True)
            else:
                vals.append(False)
        
        if vals[0] == True and vals[1] == True and vals[2] == True and vals[3] == True:
            win_found = True
            print("---------------------------------------------------------------------")
            print("Vertical Win found for", symbol)
            print("---------------------------------------------------------------------")
            sys.exit()

    # Check Diagonal Left-Right
    diag_spaces_lr = winning_spaces['diag-lr']
    for space in diag_spaces_lr:
        vals = []
        for entry in space:
            entry_val = gameboard[entry[0]][entry[1]]
            if entry_val == symbol:
                vals.append(True)
            else:
                vals.append(False)
        
        if vals[0] == True and vals[1] == True and vals[2] == True and vals[3] == True:
            win_found = True
            print("---------------------------------------------------------------------")
            print("Diagonal Win found for", symbol)
            print("---------------------------------------------------------------------")
            sys.exit()

    # Check Diagonal Left-Right
    diag_spaces_rl = winning_spaces['diag-rl']
    for space in diag_spaces_rl:
        vals = []
        for entry in space:
            entry_val = gameboard[entry[0]][entry[1]]
            if entry_val == symbol:
                vals.append(True)
            else:
                vals.append(False)
        
        if vals[0] == True and vals[1] == True and vals[2] == True and vals[3] == True:
            win_found = True
            print("---------------------------------------------------------------------")
            print("Diagonal Win found for", symbol)
            print("---------------------------------------------------------------------")
            sys.exit()



       
# Print a hint to the player
def printHint(gameboard):
    print("---------------------------------------------------------------------")
    print("             Hint: Columns with available spaces in them.            ")
    print("---------------------------------------------------------------------")
    for i in range(6):
        current_col = getColumn(gameboard, i)
        if checkColumn(current_col):
            #print("---------------------------------------------------------------------")
            print("Column", i, ": Has an available space in it.")
    print("---------------------------------------------------------------------")

# Print the rules of the Game
def printRules():
    print("---------------------------------------------------------------------")
    print("                         Rules of Connect 4                          ")
    print("---------------------------------------------------------------------")
    print("The goal of connect 4 is to  place 4 of your peices in a line. This")
    print("line may be horizontal, vertical, or diagonal. Each player Is trying ")
    print("to connect thier peices. To place your peice enter in the number of")
    print("column you would like to place your peice in.")

# Main game script
def main():    
    gameboard = initBoard()
    game_running = True

    while(game_running):
        drawBoard(gameboard)
        print("---------------------------------------------------------------------")
        print("Please enter the column number you would like to place your peice in.")
        print("Or type 'hint', if you need a hint or 'rules' to review the rules of")
        print("the game.")
        print("---------------------------------------------------------------------")
        input_value = input("Player Move: ")

        # Check for valid columns
        if input_value == 'hint':
            #print("You can place your peice in the following columns: ")
            printHint(gameboard)

        # Check if player needs to read the rules
        elif input_value == 'rules':
            printRules()

        # Check if player wants to quit
        elif input_value == 'quit' or input_value == 'exit':
            print("You have choosen to quit the game.")
            game_running == False
            sys.exit()

        # Check if input is a valid column index
        elif int(input_value) <= 6 and int(input_value) >=0:
            print("Checking column", int(input_value))
            choosen_col = getColumn(gameboard, int(input_value))

            # If column is valid, place the peice
            if checkColumn(choosen_col):
                gameboard = placePeice(gameboard, choosen_col, 'X')
                checkWinner(gameboard, 'X')

                computerRandomMove(gameboard, 'O')
                checkWinner(gameboard, 'O')
            
        # Log error
        else:
            print("The value entered was not recgonized, please enter a valid move.")

# Run the main script
main()