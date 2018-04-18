import random

board = [
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'],
    ['0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0']
]

count = 0

#print the board
def print_board(p):
    str = ''
    for i in range(8):
        for j in range(8):
            str += p[i][j] + ' '
        str += '\n'
    print(str)

#print intial state
print_board(board)

#print the first queen
board[random.randint(0,7)][0] = '1'
print_board(board)


def test_row(row,col):
    for i in range(col):
        if board[row][i]  == '1':
            return False

def test_col(col):
    for i in range(8):
        if board[i][col] == '1':
            return False

def test_down_dialog(row,col):
    for i,j in zip(range(row, 8, 1), range(col, -1, -1)):
        #if board[row+i][col-j] == '1':
        if board[i][j] == '1':
            return False

def test_up_dialog(row,col):
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        #range(1,row),range(1,col):
        #if board[row-i][col-j] == '1':
        if board[i][j] == '1':
            return False

def test(row,col):
    t = test_row(row,col) and test_col(col) and test_down_dialog(row,col) and test_up_dialog(row,col)
    if t:
        return False
    else:
        return True

def solve(col):


    for i in range(8):
        print(i)
        if col >= 8:
            return True
        if test(i,col):
            board[i][col] = ' 1'

            if solve(col + 1) == True:
                print_board(board)
                return True

            board[i][col] = ' 0'
            #print_board(board)

    return False

def result():
    if solve(1) == False:
        print "Solution does not exist"
        return False

    print_board(board)
    return True


result()