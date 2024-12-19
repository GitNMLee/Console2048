import random
""" GLOBAL """
num_of_rows = 4
num_of_cols = 4

""" HELPER FUNCTIONS """
def swap(r1,c1,r2,c2,board):
    # Given two coordinates on the 2D board, swap them
    temp = board[r1][c1]
    board[r1][c1] = board[r2][c2]
    board[r2][c2] = temp
    return board

def merge(r1,c1,r2,c2,board):
    # Given two coordinates on the 2D board, merge them. The second coordinate is erased.
    board[r1][c1] += board[r2][c2]
    board[r2][c2] = 0
    return board

def print_board(board):
    for row in board:
        print("-----------------")
        print("|", end="")
        for col in row:
            print(" ", end="")
            if col == 0:
               print(" ", end=" |")
            else:
               print(col, end=" |")
        print("")
    print("-----------------")

def read_input():
    move = input("Make a move! Move Left (A), Right (D), Up (W), or Down (S). Press (Q) to quit.\n")
    return move

def get_random_empty_cells(x, board):
    # Find x empty cells at random. Returned as a list of tuples containing coordinates [(row, col),...]
    empty_coord_list = []
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            if (board[row][col] == 0):
                empty_coord_list.append((row,col))
    
    return_list = []
    for _ in range(x):
        if (len(empty_coord_list) == 0):
            return return_list
        rand_num = random.randint(0, len(empty_coord_list)-1) # -1 because randint is inclusive
        return_list.append(empty_coord_list[rand_num])
        del empty_coord_list[rand_num]

    return return_list

""" SHIFTS """
def shift_left(board):
    # Shift all cells to the left side of the board
    for row in range(num_of_rows):
        for col in range(num_of_cols-1):
            if (board[row][col] == 0):
                # If cell is empty
                search_col = col + 1
                while (search_col != num_of_cols):
                    # Search for non-empty cells to swap
                    if (board[row][search_col] != 0):
                        board = swap(row,col,row,search_col,board)
                        break
                    search_col += 1
    # Return modified board
    return board

def shift_right(board):
    # Shift all cells to the right side of the board
    for row in range(num_of_rows):
        for col in range(num_of_cols-1, 0, -1):
            if (board[row][col] == 0):
                # If cell is empty
                search_col = col - 1
                while (search_col != -1):
                    # Search for non-empty cells to swap
                    if (board[row][search_col] != 0):
                        board = swap(row,col,row,search_col,board)
                        break
                    search_col -= 1
    # Return modified board
    return board

def shift_up(board):
    # Shift all cells to the top side of the board
    for col in range(num_of_cols):
        for row in range(num_of_rows-1):
            if (board[row][col] == 0):
                # If cell is empty
                search_row = row + 1
                while (search_row != num_of_rows):
                    # Search for non-empty cells to swap
                    if (board[search_row][col] != 0):
                        board = swap(row,col,search_row,col,board)
                        break
                    search_row += 1
    # Return modified board
    return board

def shift_down(board):
    # Shift all cells to the bottom side of the board
    for col in range(num_of_cols):
        for row in range(num_of_rows-1, 0, -1):
            if (board[row][col] == 0):
                # If cell is empty
                search_row = row - 1
                while (search_row != -1):
                    # Search for non-empty cells to swap
                    if (board[search_row][col] != 0):
                        board = swap(row,col,search_row,col,board)
                        break
                    search_row -= 1
    # Return modified board
    return board

""" MERGES """
def merge_left(board):
    # Merge all cells to the left side of the board
    for row in range(num_of_rows):
        for col in range(num_of_cols-1):
            if (board[row][col] != 0):
                # Cell is non-empty
                search_col = col + 1
                while (search_col != num_of_cols and (board[row][search_col] == 0 or board[row][search_col] == board[row][col])): # If we found a cell of a higher number, ignore the rest of matches, this cell is blocking.
                    if (board[row][search_col] == board[row][col]):
                        merge(row, col, row, search_col, board)
                        break
                    search_col += 1
    # Return modified board
    return board

def merge_right(board):
    # Merge all cells to the right side of the board
    for row in range(num_of_rows):
        for col in range(num_of_cols-1, 0, -1):
            if (board[row][col] != 0):
                # Cell is non-empty
                search_col = col - 1
                while (search_col != -1 and (board[row][search_col] == 0 or board[row][search_col] == board[row][col])): # If we found a cell of a higher number, ignore the rest of matches, this cell is blocking.
                    # Search for matching cells to merge
                    if (board[row][search_col] == board[row][col]):
                        merge(row, col, row, search_col, board)
                        break
                    search_col -= 1
    # Return modified board
    return board

def merge_up(board):
    # Merge all cells to the top side of the board
    for col in range(num_of_cols):
        for row in range(num_of_rows-1):
            if (board[row][col] != 0):
                # Cell is non-empty
                search_row = row + 1
                while (search_row != num_of_rows and (board[search_row][col] == 0 or board[search_row][col] == board[row][col])): # If we found a cell of a higher number, ignore the rest of matches, this cell is blocking.
                    # Search for matching cells to merge
                    if (board[search_row][col] == board[row][col]):
                        merge(row, col, search_row, col, board)
                        break
                    search_row += 1
    # Return modified board
    return board

def merge_down(board):
    # Merge all cells to the bottom side of the board
    for col in range(num_of_cols):
        for row in range(num_of_rows-1, 0, -1):
            if (board[row][col] != 0):
                # Cell is non-empty
                search_row = row - 1
                        # If we found a cell of a higher number, ignore the rest of matches, this cell is blocking.
                while (search_row != -1 and (board[search_row][col] == 0 or board[search_row][col] == board[row][col])):
                    # Search for matching cells to merge
                    if (board[search_row][col] == board[row][col]):
                        merge(row, col, search_row, col, board)
                        break
                    search_row -= 1
    # Return modified board
    return board


def main():
    board = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    cont = True

    # Pick two random cells to place 2 in
    coord_list = get_random_empty_cells(2, board)

    for coords in coord_list:
        row = coords[0]
        col = coords[1]
        board[row][col] = 2

    while (cont):
        print_board(board)
        move = read_input().lower()
        if (move == "a"):
            # Left
            print("Left")
            board = merge_left(board)
            board = shift_left(board)

        elif (move == "d"):
            # Right
            print("Right")
            board = merge_right(board)
            board = shift_right(board)
        elif (move == "w"):
            # Up
            print("Up")
            board = merge_up(board)
            board = shift_up(board)
        elif (move == "s"):
            # Down
            print("Down")
            board = merge_down(board)
            board = shift_down(board)
        elif (move == "q"):
            # Quit!
            print("Quit")
            cont = False
        else:
            print("Bro, not an option")

        # Get a new random 2 cell
        coord_list = get_random_empty_cells(1, board)
        row = coord_list[0][0]
        col = coord_list[0][1]
        board[row][col] = 2

main()