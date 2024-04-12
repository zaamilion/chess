from consts import WHITE, BLACK

def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8

def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    if board.current_player_color() == WHITE:
        print('white')
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', board.cell(row, col), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='        ')
        for col in range(8):
            print(col, end='    ')
        print()
    else:
        print('black')
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(0, 8, 1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', board.cell(row, col), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='        ')
        for col in range(8):
            print(col, end='    ')
        print()


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE