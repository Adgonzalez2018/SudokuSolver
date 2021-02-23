board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, position):
    # row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != 1:
            return False
    # col
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != 1:
            return False
    # square
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):  # finds empty space
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col
    return None

def edit(board):
    x = 0
    y = 0
    while (y <= 8 and x <=8):
        input_a = int(input("Enter a number 1-9 (0 if no number): "))
        board[x][y] = input_a
        y += 1
        if y == 9 and x != 8:
            x += 1
            y = 0
        elif y == 9 and x == 8:
            break
    return print(print_board(board))


userInput = input("Welcome, would you like to change the board?\n")
if userInput == 'yes':
    edit(board)
    print_board(board)
    print("")
    solve(board)
    print("Solved Solution")
    print("__________________________\n")
    print_board(board)
    exit()

elif userInput == 'no':
    print_board(board)
    print("")
    solve(board)
    print("Solved Solution")
    print("__________________________\n")
    print_board(board)
    exit()
