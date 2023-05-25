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

def win_check(mark, board):
    (board[7] == mark and board[8] == mark and board[9] == mark)

if __name__ == "__main__":
    test_board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    place_marker(test_board, '$', 8)
    display_board(test_board)