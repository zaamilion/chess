from bord import Board
from global_commands import print_board
from consts import WHITE, BLACK


def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row_to> <row_to>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        
        else:
            print('Ход чёрных:')
        
        command = input()
        
        if command == 'exit':
            break
        
        try:
            move_type, row, col, row_to, col_to = command.split()
            row, col, row_to, col_to = int(row), int(col), int(row_to), int(col_to)
            if board.move_piece(row, col, row_to, col_to):
                print('Ход успешен')

            else:
                print('Координаты некорректы! Попробуйте другой ход!')
        except ValueError:
            print('Неверный ввод')
        board.shah_white =  board.is_shah(WHITE)
        board.shah_black =  board.is_shah(BLACK)
        print(board.shah_white)
        print(board.shah_black)
main()