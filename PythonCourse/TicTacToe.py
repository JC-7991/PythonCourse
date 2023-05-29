import random

def display_board(board):

    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    
    else:
        return ('O', 'X')
    
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:


def replay():
    pass

if __name__ == "__main__":

    test_board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
    place_marker(test_board, '$', 8)
    display_board(test_board)
    print(win_check(test_board, 'X'))