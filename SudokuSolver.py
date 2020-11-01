import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

board = [
    [0,4,0,3,5,7,8,1,2],
    [3,8,0,2,9,0,0,0,0],
    [1,2,0,6,0,4,7,0,3],
    [4,6,9,0,0,0,0,0,7],
    [0,3,1,0,6,0,2,4,9],
    [0,5,2,4,3,0,1,8,0],
    [0,0,8,9,7,0,0,2,5],
    [0,9,4,5,0,6,3,7,0],
    [5,0,0,0,0,0,0,0,0]
]


def solve(bo):
    # Base Case of recursion
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    #attempting to insert num
    time.sleep(.2)
    print_board(board)
    print("---------------------")

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0 

    return False

def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 Square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, Col
    return None

solve(board)
print_board(board)

#TODO Design and implement GUI