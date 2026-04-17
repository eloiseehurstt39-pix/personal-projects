import time
import random


#INSTRUCTIONS
def show_instructions():
    print("\n - HOW TO PLAY CONNECT 4 - \n")

    print("HOW TO PLAY:")
    print("- Player X goes first.")
    print("- Choose a column number.")
    print("- Your piece will fall to the lowest available space.")
    print("- Other player's turn.\n")

    print("OBJECTIVE:")
    print("Be the first player to connect your pieces in a row.\n")

    print("EACH LEVEL INSTRUCTIONS:\n")

    print("LEVEL EASY:")
    print("- Connect 4 in a row to win.")
    print("- All directions count (horizontal, vertical, diagonal).")
    print("- Undo and Redo your last move by typing 'undo' or 'redo'.\n")
    print("- Go back to start of game.")

    print("LEVEL MEDIUM:")
    print("- Connect 4 in a row to win.")
    print("- You have 15 seconds per turn or your turn is skipped!")
    print("- After 30 seconds a random column gets blocked.\n")
    print("- Undo and Redo your last move by typing 'undo' or 'redo'.\n")
    print("- Each player gets ONE double drop : drop a second token on your turn!")  
    print("- Go back to start of game.")

    print("LEVEL HARD:")
    print("- Connect 5 in a row to win.")
    print("- Diagonal only!")
    print("- You have 15 seconds per turn or your turn is skipped!")
    print("- After 45 seconds the grid shrinks — columns 1 and 9 are blocked.\n")
    print("- Each player gets ONE double drop : drop a second token on your turn!")  
    print("- Go back to start of game.")

    print("LEVEL BONUS:")
    print("- Connect 4 in a row to win.")
    print("- Every 20 seconds all tokens on the board SWAP!")
    print("- X becomes O and O becomes X — watch out!\n")
    print("- Go back to start of game.")

    input("Press Enter to return to Main Menu...") # is able to start again because of the while loop restarts and goes to main

# function that prints the board (in a nice way)
def print_board(board):
    for row in board:
        print(" | ", end="")
        for cell in row:
            print(cell, end = " | ")
        print()

# function creates the empty board itself (list of lists)
def create_board(rows, cols):
    # creating an empty list depending on the amount of columns there will be
    board = []

    for i in range(rows):
        new_row = [] # this creates a new empty row

        for x in range(cols):# this creates a new column each time
            new_row.append(" ") # adds an empty space to the new row , append --> adds something new to a list
        board.append(new_row)

    return board


#function that checks if the player has won, longing at each possibility of 4 or 5 in a row on the board
def check_if_win(board, player, level): #will depend on the board (level)and the player

    rows = len(board) # how many rows the board has
    cols = len(board[0]) # how many columns the board has

    # HARD level - diagonals only, and 5 in a row
    if level == "3":

        # HARD level: diagonals only, 5 in a row
        for r in range(rows - 4): # We subtract 4 because we need room for 5 pieces.
            for c in range(cols -4):
                if (board[r][c] == player and # this starts checking from th top-left
                    board[r+1][c+1] == player and
                    board[r+2][c+2]== player and
                    board[r+3][c+3]== player and
                    board[r+4][c+4] == player):
                    return True # if 5 matching pieces in a row = WIN

        # diagonal /, r goes down, c goes left (so minus)
        for r in range(rows - 4):
            for c in range(4, cols):
                if (board[r][c]== player and
                    board[r+1][c-1] ==player and
                    board[r+2][c-2] == player and
                    board[r+3][c-3]== player and
                    board[r+4][c-4]== player):
                    return True
                
        return False

    else:
        #horizontal win row -> col 1 to 3 = 4 in a row
        for r in range(rows):
            for c in range(cols - 3 ): # 3 beacuse were using 4 colums total , meaning the last place the program will benlook will be column 3
                if (board[r][c] == player and
                    board[r][c+1] == player and
                    board[r][c+2] == player and
                    board[r][c+3] == player):
                    return True

        # vertical from board[r][c] to board[r+3][c]
        for r in range(rows - 3):
            for c in range(cols):
                if (board[r][c]== player and
                    board[r+1][c] == player and
                    board[r+2][c] == player and
                    board [r+3][c] == player):
                    return True


        #diagonal \
        for r in range(rows - 3):
            for c in range(cols -3):
                if (board[r][c] == player and
                    board[r+1][c+1] == player and
                    board[r+2][c+2]== player and
                    board[r+3][c+3]== player):
                    return True

        #other diagocnal /
        for r in range(rows - 3):
            for c in range(3, cols):
                if (board[r][c]== player and
                    board[r+1][c-1] ==player and
                    board[r+2][c-2] == player and
                    board[r+3][c-3]== player):
                    return True

    return False

# this function starts the game
# this will be what happends for each level
def start_game(level):
    #sets up the board size and will be explaining the rules again
    if level == "1":  # this is for the easy level
        rows = 6
        cols = 7
        print(" \n INSTRUCTION REMINDER :")
        print("- Connect 4 in a row to win.")
        print("- All directions count (horizontal, vertical, diagonal).")
        print("- Undo your last move by typing 'undo' , 'redo' or 'restart'.\n")

    elif level == "2": # for level medium
        rows = 6
        cols = 7
        print("\n INSTRUCTION REMINDER :")
        print("- Connect 4 in a row to win.")
        print("- You have 15 seconds per turn or your turn is skipped!")
        print("- Each player gets ONE double drop per game.") 
        print("- After 30 seconds a random column gets blocked.\n")

    elif level =="3":  # for level hard
        rows = 8
        cols = 9
        print(" \n INSTRUCTION REMINDER :")
        print("- Connect 5 in a row to win.")
        print("- Diagonal only!")
        print("- You have 15 seconds per turn or your turn is skipped!")
        print("- After 45 seconds the grid shrinks — columns 1 and 9 are blocked.\n")
        print("- Each player gets ONE double drop per game.") 


    elif level == "4":  # for the bonus level
        rows = 8
        cols = 9
        print(" \n INSTRUCTION REMINDER :")
        print("- Connect 4 in a row to win.")
        print("- Every 20 seconds all tokens on the board SWAP!")
        print("- X becomes O and O becomes X — watch out!\n")

    board = create_board(rows, cols) # the empty list

    current_player = "X" # will always starts with player X

    move_history = [] # empty list that will save all the moves made, for the undo function

    redo_history = []  # empty list that saves moves for the redo function

    game_start_time = time.time() # will calculate what time the game started (for hard, medium and bonus level)

    blocked_column = None # will keep what columun is blocked for level medium

    # this will track the two end columns of level hard to see if they have been blocked
    hard_blocked_cloumns = []
    grid_shrink = None

    # will track the time for bonus level
    last_swap_time = time.time()

    #advantage double tocken tracker
    x_double_used = False
    o_double_used = False


    # creating a loop for that game, every time the player choses a colum drop it to the lowest row
    while True:
        print_board(board) #show the board

        # MEDIUM --> block random column after a 30 seconds
        if level == "2" and blocked_column is None:
            if time.time() - game_start_time > 30:
                blocked_column = random.randint(0,cols -1 ) # will pick a random column between 0 and the last colmn(cols -1)
                print(f"Column {blocked_column + 1} is now blocked ")

                # will fill the whole column wil "|"
                for r in range(rows):
                    if board[r][blocked_column] == " ": # if has this
                        board[r][blocked_column] = "|" # then change to "|" (this)

        #HARD --> shring the grid after 45 seconds
        if level =="3" and grid_shrink is None:
            if time.time() - game_start_time > 45:
                hard_blocked_cloumns = [0, cols -1]
                grid_shrink =True
                print("The grid is shrinking! Column 1 and 9 are now blocked ")

                # will fill the columns will "-"
                for col in hard_blocked_cloumns:
                    for r in range(rows):
                            board[r][col] = "-"
        
        # BONUS --> Tokens swap every 20seconds
        if level == "4":
            if time.time() - last_swap_time > 40:
                print("TOKENS ARE SWAPPING!")
                for r in range(rows):
                    for c in range(cols):
                        if board[r][c] == "X":
                            board[r][c] = "O" # chnage from X to O
                        elif board[r][c] == "O":
                            board[r][c] = "X" # change from O to X
                last_swap_time = time.time()  # reset the timer so it swaps again in 20 seconds


        # start the timer
        turn_start = time.time()

        #player inputs 
        #the player gets the question to chose a colum depending on which level were on
        if level in ["1", "2"]:
            chosen_column = input(f"Player {current_player}, chooses column (1-{cols}) or type 'undo', 'redo' or 'restart' :")

            # if the player wants to undo
            if chosen_column.lower() == "undo":
                if move_history:
                    last_row, last_col, last_player = move_history.pop() # .pop() removes the last item from the list
                    redo_history.append((last_row, last_col, last_player))
                    board[last_row][last_col] = " " # this removes the token and make is a blanck space again
                    current_player = last_player # so that the same player can play again
                    print("LAST MOVE HAS BEEN UNDONE ")
                else:
                    print("NO MOVE TO UNDO")
                continue

            elif chosen_column.lower() == "redo":
                if redo_history:
                    redo_row, redo_col, redo_player = redo_history.pop()
                    board[redo_row][redo_col] = redo_player
                    # Put it back in move_history
                    move_history.append((redo_row, redo_col, redo_player))

                    # Switch player to the person who *didn't* just redo their turn
                    current_player = "O" if redo_player == "X" else "X"
                    print("REDO SUCCESSFUL")
                else :
                    print("NO MOVE TO REDO")
                continue


        # same but for the HARD and bonus level because it dose not have undo
        elif level in ["3", "4"]:
            chosen_column =input(f"Player {current_player} choose column (1-{cols}) or 'restart' :")
            # --- RESTART LOGIC ---
        if chosen_column.lower() == "restart":
            print("\n RESTARTING GAME")
            # 1. Create a brand new empty board
            board = create_board(rows, cols)

            # 2. Reset the history so you can't undo into the "old" game
            move_history.clear()
            redo_history.clear()

            # 3. Reset the player to X
            current_player = "X"

            # 4. Optional: Reset timers for Medium/Hard/Bonus levels
            game_start_time = time.time()
            last_swap_time = time.time()

            continue # Jumps back to the top to show the empty board


        # MEDIUM  --> check how long the player took
        turn_time = time.time() - turn_start

        # 10 sec per turn
        if level == "2" and time.time() - turn_start > 10:
            print("YOU HAVE RUN OUT OF TIME ! YOUR TURN HAS BEEN SKIPPED")

            # this will skip the player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            continue

        # HARD LEVEL --> 15 sec peur turn
        elif level =="3" and time.time() - turn_start > 15:
            print ("YOU HAVE RUN OUT OF TIME ! YOUR TURN HAS BEEN SKIPPED")

            # this will skip the player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            continue

      
        # double token
        if level in ["2", "3"]:
            if current_player == "X" and x_double_used == False:
                double_choice = input("Would you like to use your double drop? (yes/no): ")
                if double_choice.lower() == "yes":
                    double_drop = input(f"Choose your second column (1-{cols}): ")
                # if player type a word the game will not crash
                    try:
                        double_drop = int(double_drop) - 1
                    except ValueError:
                        print("UNVALID INPUT, DOUBLE DROP SKIPPED")
                    else:
                    # check if the colum is valid
                        if double_drop < 0 or double_drop >= cols:
                            print("UNVALID COLUMN, DOUBLE DROP SKIPPED")
                    #check if the column is not full
                        elif board[0][double_drop] != " ":
                            print("COLUMN FULL, DOUBLE DROP SKIPPED")
                    #drop the token
                        else:
                            for row in range(rows - 1, -1, -1):
                                if board[row][double_drop] == " ":
                                    board[row][double_drop] = current_player
                                    move_history.append((row, double_drop, current_player))
                                    break
                            x_double_used = True
                            print("DOUBLE DROP USED!")

            elif current_player == "O" and o_double_used == False:
                double_choice = input("Would you like to use your double drop (yes/no):")
                if double_choice.lower() == "yes":
                    double_drop = input("Choose your second column (1-{cols}) : ")
                    try:
                        double_drop = int(double_drop) - 1
                    except ValueError:
                        print("UNVALID")
                    else:
                        if double_drop < 0 or double_drop >= cols:
                            print("UNVALID COLUMN, DOUBLE DROP SKIPPED")
                        elif board[0][double_drop] != " ":
                            print("COLUMN FULL, DOUBLE DROP SKIPPED")
                        else:
                            for row in range(rows - 1, -1, -1):
                                if board[row][double_drop] == " ":
                                    board[row][double_drop] = current_player
                                    move_history.append((row, double_drop, current_player))
                                    break
                            o_double_used = True
                            print("DOUBLE DROP USED!")



        # if player types a word in when chosing a number = unvalid input
        try:
            chosen_column = int(chosen_column) - 1
        except ValueError:
            print("UNVALID INPUT")
            continue

        # if there is a number that is not 1 too 7 (6 = 7 because cause 0 1 2 3 4 5 6 7 )
        if chosen_column < 0 or chosen_column >= cols:
            print("UNVALID NUMBER - CHOOSE A NUMBER")
            continue

        #MEDIUM :  blocked column check
        if level == "2" and blocked_column == chosen_column:
            print("THIS COLUMN IS BLOCKED")
            continue

        # HARD : blocked columns
        if level =="3" and chosen_column in hard_blocked_cloumns:
            print("THE GRID HAS BEEN SHRINKED ")
            continue

        # check if column is full
        if board[0][chosen_column] != " ":
            print("Column is full, choose an other one")
            continue


        # Drop the piece into the lowest empty row
        # and replace blanck space with X or O
        #(rows - 1, -1, -1) = start (5) from last row , stop (0) , move backwards
        for row in range(rows -1 , -1, -1): # so it starts at the bottom and moves up
            if board[row][chosen_column] == " ":
                board[row][chosen_column] = current_player # this places the players pice
                move_history.append((row, chosen_column, current_player))# saves it for undo
                redo_history.clear() # saves it for redo
                break

        # check if win
        if check_if_win(board, current_player, level):
            print_board(board)
            print(f"Player {current_player} HAS WON CONGRATS")
            break


        # this will switch player, if current player is X then the next will be O otherwise the other way round
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        continue


# this function prints the main menu
def show_main_menu():
    print("=== MAIN MENU ===")
    print("1. Start game")
    print("2. Instructions ")
    print("3. Quit")

#this function prints the level menu
def level_menu():
    print("=== Level Menu ===")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Bonus")

#this keeps the main menu running to play again
def main():
    while True:
        show_main_menu()
        try:
            main_menu_choice = input("Choose an option (1-3):")
        except:
            print("Please enter a valid number")
            continue

        if main_menu_choice == "1":
            level_menu()
            level_choice = input("Choose a level: ")
            if level_choice in ["1", "2", "3", "4"]:
                start_game(level_choice) #will then go and chose the level selected
            else:
                print("Level has not been choosen")

        elif main_menu_choice == "2":
            show_instructions()

        elif main_menu_choice == "3":
            print("Goodbye")
            break

        else:
            print("UNVALID INPUT")



# Run program
main()




