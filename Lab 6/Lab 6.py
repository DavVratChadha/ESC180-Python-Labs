'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    print("")
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

#Problem 1 (a)
def coordinates(square_num):
    global coord
    coord = []
    if square_num < 1 or square_num > 9:
        print("\nInvalid Input\n")
        return "ERROR"
    else:
        row = ((square_num - 1) // 3) #0 to 8; 0 to 2 ->0 | 3 to 5 ->1...
        column = (square_num - 1) - 3 * row #becasue 3 elements in a row
        coord.append(row)
        coord.append(column)
        return coord

#Problem 1 (b)
def put_in_board(board, mark, square_num):
    output = coordinates(square_num)
    if output == "ERROR":
        return
    else:
        board[coord[0]][coord[1]] = mark
        return

#Problem 1 (c)
def PvP_game():
    print("")
    mark_list = ["X", "O"]
    coord_list = []
    counter = 0
    board = make_empty_board()
    print_board_and_legend(board)
    turn_num = 0
    while True:
        if turn_num > 8: #To end the game on 9 moves
            print("\nIt's a Tie. Game Ended") #because if someone wins, the computer would check at the end of this loop, before coming here
            return
        turn_num += 1

        #asking user input
        square_num = int(input("\nPlease enter the square number for " + mark_list[counter] + ":"))
        if square_num in coord_list:
            print("Invalid Input.")
            return
        else:
            coord_list.append(square_num)

        mark = mark_list[counter]
        put_in_board(board, mark, square_num)
        print_board_and_legend(board)

        #Determining the winner
        flag = is_win(board, mark)
        if flag: #True
            print("\nPlayer {} with {} has won the game".format(counter + 1, mark))
            return

        counter = (counter + 1) % 2 #to keep counter = 0 or 1 for
                                    #mark_list

#Problem 2 (a)
def get_free_squares(board):
#    global empty_coord_list
    empty_coord_list = []
    for i in range(len(board)): #each row
        for j in range(len(board[0])): #each corresponding column
            if board[i][j] == " ":
                empty_coord_list.append([i,j])
    return empty_coord_list

#Problem 2 (b)
def make_random_move(board, mark):
    empty_coord_list = get_free_squares(board)
    n = len(empty_coord_list)
    #No more free turns left
    if n == 0:
        print("Game Ended")
        return
    comp_choice = empty_coord_list[int(n * random.random())] #(0 to 1)* n
    board[comp_choice[0]][comp_choice[1]] = mark
    print_board_and_legend(board)
    return

#Problem 2 (c)
def PvC_game():
    print("")
    coord_list = []
    board = make_empty_board()
    print_board_and_legend(board)
    turn_num = 0
    while True:
        #asking user input
        square_num = int(input("\nPlease enter the square number for X:"))

        #To avoid user from cheating by taking a square that has already been taken
        allowed_moves = get_free_squares(board)
        player_move = coordinates(square_num)
        if player_move not in allowed_moves:
            print("Invalid Input")
            return

        #Player turn
        print("\nPlayer played:")
        put_in_board(board, "X", square_num)
        print_board_and_legend(board)
        turn_num += 1 #player turn counted

        #Check if player won
        flag = is_win(board, "X")
        if flag: #True
            print("\nPlayer has won the game")
            return

        if turn_num > 8: #To end the game on 9 moves
            print("\nIt's a tie. Game Ended")
            return

        #Computer turn
        print("\nComputer Played:")
#        make_random_move(board, "O")
#        comp_decider_level_1(board) #for Problem 4 (a)
        comp_decider_level_2(board) #for Problem 4 (b)
        turn_num += 1 #computer turn counted

        #Check if computer won
        flag = is_win(board, "O")
        if flag: #True
            print("\nComputer has won the game")
            return


#Problem 3 (a)
def is_row_all_marks(board, row_i, mark):
    if board[row_i][0] == mark and board[row_i][1] == mark and board[row_i][2] == mark:
            return True
    else:
        return False

#Problem 3 (b)
def is_col_all_marks(board, col_i, mark):
    if board[0][col_i] == mark and board[1][col_i] == mark and board[2][col_i] == mark:
            return True
    else:
        return False

#Problem 3 (c)
def is_diag_all_marks(board, mark): #Checks for both diagnals
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    elif board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    else:
        return False

def is_win(board, mark):
    for i in range(3): #3 rows, 3 columns in game
        row_res = is_row_all_marks(board, i, mark)
        if row_res == True:
            return True

        col_res = is_col_all_marks(board, i, mark)
        if col_res == True:
            return True
    diag_res = is_diag_all_marks(board, mark)
    if diag_res == True:
        return True
    #else
    return False

#Problem 3 (d)
#Done in line 135 (PvC_game) and 80 (PvP_game)

#Problem 4 (a)
def comp_decider_level_1(board):
    free_squares = get_free_squares(board)
    n = len(free_squares)

    if n == 0: #No more free turns left
        print("Game Ended")
        return

    for num in range(n):
        new_board = board_duplicator(board)
        temp_choice = free_squares[num]
        new_board[temp_choice[0]][temp_choice[1]] = "O"

        #Check if computer won
        flag = is_win(new_board, "O")
        if flag: #True
            comp_choice = temp_choice
            board[comp_choice[0]][comp_choice[1]] = "O"
            print_board_and_legend(board)
            return

    #else (no moves give direct victory to computer)
    comp_choice = free_squares[int(n * random.random())] #(0 to 1)* n
    board[comp_choice[0]][comp_choice[1]] = "O"
    print_board_and_legend(board)
    return

def board_duplicator(board):
    similar_new_board = []
    for row in board: #creating a deep copy
        similar_new_board.append(row.copy())
    return similar_new_board


#Problem 4 (b)
def comp_decider_level_2(board):
    comp_free_squares = get_free_squares(board) #for computer
    mod_comp_free_squares = []
    n = len(comp_free_squares)

    if n == 0: #No more free turns left
        print("Game Ended")
        return

    for num in range(n):
        new_board = board_duplicator(board)
        temp_comp_choice = comp_free_squares[num]
        new_board[temp_comp_choice[0]][temp_comp_choice[1]] = "O"

        #Check if computer won
        flag = is_win(new_board, "O")
        if flag: #True
            comp_choice = temp_choice
            board[comp_choice[0]][comp_choice[1]] = "O"
            print_board_and_legend(board)
            return

        #same to 4 (a) till this line

        #if computer does not win, we predict player's move and try so that player does not win
        player_free_squares = get_free_squares(new_board) #for player
        m = len(player_free_squares)
        if m > 0:
            for num2 in range(m):
                new_board2 = board_duplicator(new_board)
                temp_player_choice = player_free_squares[num2]
                new_board2[temp_player_choice[0]][temp_player_choice[1]] = "X"

                #Check if player wins
                flag2 = is_win(new_board2, "X")
                if flag2 == False: #False I.e. good move by comp
                    if temp_comp_choice not in mod_comp_free_squares:
                        mod_comp_free_squares.append(temp_comp_choice)
                        #for computer to avoid bad moves, we modify
                        #the list of possible moves for computer
                       # comp_free_squares.remove(temp_comp_choice)

    #if (computer does not win on a single move)
    #selecting random point from new modified list
    if len(mod_comp_free_squares) > 0:

        comp_choice = mod_comp_free_squares[int(len(mod_comp_free_squares) * random.random())]
        board[comp_choice[0]][comp_choice[1]] = "O"
        print_board_and_legend(board)
        return

    else: #Computer loses by every possible move
        free__squares = get_free_squares(board)
        comp_choice = free_squares[int(len(free_squares) * random.random())]
        board[comp_choice[0]][comp_choice[1]] = "O"
        # print_board_and_legend(board)
        return


"""
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    print_board_and_legend(board)
    #Problem 1 (a)
    coordinates(6)
    board[coord[0]][coord[1]] = "X"
    print_board_and_legend(board)

    coordinates(12)

    #Problem 1 (b)
    put_in_board(board, "X", 9)
    print_board_and_legend(board)

    put_in_board(board, "X", 10)
    print_board_and_legend(board)

    #Problem 1 (c)
    #PvP_game()

    #Problem 2 (b)
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    print_board_and_legend(board)
    make_random_move(board, "X")

    #Problem 2 (c)
    #PvC_game()

    #Problem 3 (a)
    board = [["X", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    print(is_row_all_marks(board,0,"X")) #True
    print(is_row_all_marks(board,1,"X")) #False

    #Problem 3 (b)
    board = [["X", "O", "X"],
             [" ", "O", " "],
             [" ", "O", " "]]
    print(is_col_all_marks(board,1,"O")) #True
    print(is_col_all_marks(board,2,"X")) #False

    #Problem 3 (c)
    board = [["O", "X", "O"],
             [" ", "O", " "],
             ["O", "O", "X"]]
    print(is_diag_all_marks(board,"O")) #True
    print(is_diag_all_marks(board,"X")) #False

    print(is_win(board, "X")) #False
    print(is_win(board, "O")) #True

    board = [["X", "X", "X"],
             [" ", "O", " "],
             [" ", "O", " "]]
    print(is_win(board, "X")) #True
    print(is_win(board, "O")) #False

"""