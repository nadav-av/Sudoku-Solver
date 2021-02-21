soduko_board = [

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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return (-1, -1)


def check(r, c, val, board):
    # check for row
    for i in range(0, 9):
        if val == board[i][c] and i != r:
            return False

    # check for col
    for j in range(0, 9):
        if val == board[r][j] and j != c:
            return False

    # check for square
    x = (r // 3) * 3
    y = (c // 3) * 3

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if i != r and j != c and board[i][j] == val:
                return False

    return True


def solve(board):
    r, c = find_blank(board)
    if r == -1 and c == -1:
        return True

    else:
        for i in range(1, 10):
            if check(r, c, i, board):
                board[r][c] = i

                if solve(board):
                    return True

                else:
                    board[r][c] = 0

    return False


print_board(soduko_board)
print("\n")
solve(soduko_board)
print_board(soduko_board)


