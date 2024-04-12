from global_commands import opponent, correct_coords
from consts import WHITE, BLACK
import bord
class Rook:
 
    def __init__(self, color):
        self.color = color
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'R'
 
    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False
 
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False
 
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        if (self.color == WHITE and board.shah_white) or (self.color == BLACK and board.shah_black):
            board_model = Board()
            for idx in range(8):
                board_model.field[idx] = board.field[idx].copy()
            board_model.shah_white = True
            board_model.shah_black = True
            board_model.field[row1][col1] = board_model.field[row][col]
            board_model.field[row][col] = None 
            if board_model.is_shah(self.color):
                print('41по шаху')
                return False
 
        return True
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
 
 
class Pawn:
 
    def __init__(self, color):
        self.color = color
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'P'
 
    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False
 
        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
 
        # ход на 1 клетку
        if row + direction == row1 or (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            if (self.color == WHITE and board.shah_white) or (self.color == BLACK and board.shah_black):
                board_model = bord.Board()
                for idx in range(8):
                    board_model.field[idx] = board.field[idx].copy()
                board_model.shah_white = True
                board_model.shah_black = True
                board_model.field[row1][col1] = board_model.field[row][col]
                board_model.field[row][col] = None 
                if board_model.is_shah(self.color):
                    print('89по шаху')
                    return False
            return True
 
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))
 
 
class Knight:
    """Класс коня. Пока что заглушка, которая может ходить в любую клетку."""
 
    def __init__(self, color):
        self.color = color
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём
 
    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        piece1 = board.get_piece(row1, col1) # фигура на той клетке

        # если не пустая я своего цвета
        if not (piece1 is None) and piece1.get_color() == self.color:
            return False
        
        if ((row + 2, col + 1) != (row1, col1) and (row + 2, col - 1) != (row1, col1) and 
                (row + 1, col + 2) != (row1, col1) and (row1 + 1, col1 - 2) != (row1, col1) and
                (row - 2, col + 1) != (row1, col1) and (row1 - 2, col1 - 1) != (row1, col1) and
                (row - 1, col - 2) != (row1, col1) and (row1 - 1, col1 - 2) != (row1, col1)) is True:
            return False

        if (self.color == WHITE and board.shah_white) or (self.color == BLACK and board.shah_black):
            board_model = bord.Board()
            for idx in range(8):
                board_model.field[idx] = board.field[idx].copy()
            board_model.shah_white = True
            board_model.shah_black = True
            board_model.field[row1][col1] = board_model.field[row][col]
            board_model.field[row][col] = None 
            if board_model.is_shah(self.color):
                print('137по шаху')
                return False
        return True  # реализовано
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
 
 
class King:
    """Класс короля. Пока что заглушка, которая может ходить в любую клетку."""
 
    def __init__(self, color):
        self.color = color
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'K'
 
    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        piece1 = board.get_piece(row1, col1) # фигура на той клетке

        # если не пустая я своего цвета
        if not (piece1 is None) and piece1.get_color() == self.color:
            return False
        
        if ((row + 1, col) != (row1, col1) and (row + 1, col + 1) != (row1, col1) and
                (row + 1, col - 1) != (row1, col1) and (row, col + 1) != (row1, col1) and 
                (row - 1, col + 1) != (row1, col1) and (row - 1, col - 1) != (row1, col1) and
                (row - 1, col) != (row1, col1) and (row, col - 1) != (row1, col1)) is True:
            return False

        if (self.color == WHITE and board.shah_white) or (self.color == BLACK and board.shah_black):
            board_model = bord.Board()
            for idx in range(8):
                board_model.field[idx] = board.field[idx].copy()
            board_model.shah_white = True
            board_model.shah_black = True
            board_model.field[row1][col1] = board_model.field[row][col]
            board_model.field[row][col] = None 
            if board_model.is_shah(self.color):
                print('181по шаху')
                return False
        return True  # реализовано
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
 
 
class Queen:
    """Класс ферзя. Пока что заглушка, которая может ходить в любую клетку."""
 
    def __init__(self, color):
        self.color = color
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'Q'
 
    def can_move(self, board, row, col, row1, col1):
        prohod = False
        if not correct_coords(row1, col1):
            print('204вне доски')
            return False
        piece1 = board.get_piece(row1, col1) # фигура на той клетке

        # если не пустая я своего цвета
        if not (piece1 is None) and piece1.get_color() == self.color:
            print('210там свои')
            return False
        # по идее надо еще реализовать по диагонали
        # если идем прямо ← ↑ → ↓
        if row == row1 or col == col1:

            step = 1 if (row1 >= row) else -1

            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    print('220чет на пути')
                    return False
            
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    print('226чет на пути')
                    return False
                
            prohod = True
        
        elif row - col == row1 - col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                c = col - row + r
                if not (board.get_piece(r, c) is None):
                    print('236чет на пути')
                    return False
            prohod = True

        elif row + col == row1 + col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                c = row + col - r
                if not (board.get_piece(r, c) is None):
                    print('245чет на пути')
                    return False
            prohod = True
        if prohod is True:
            if abs(row1 - row) != abs(col1 - col):
                print('250не по диаге')
                return False
            
            if row < row1:
                step_row = 1
            else:
                step_row = -1
            if col < col1:
                step_col = 1
            else:
                step_col = -1

            for kf in range(1, abs(row1 - row)):
                print('263 ', row + (kf * step_row), col + (kf * step_col))
                if board.field[row + (kf * step_row)][col + (kf * step_col)] != None:
                    print(f'265На диаге корды {row + (kf * step_row), col + (kf * step_col)} лежит {board.field[row + (kf * step_row)][col + (kf * step_col)]}')
                    return False

            if (self.color == WHITE and board.shah_white) or (self.color == BLACK and board.shah_black):
                board_model = bord.Board()
                for idx in range(8):
                    board_model.field[idx] = board.field[idx].copy()
                board_model.shah_white = True
                board_model.shah_black = True
                board_model.field[row1][col1] = board_model.field[row][col]
                board_model.field[row][col] = None 
                if board_model.is_shah(self.color):
                    print('277по шаху')
                    return False
            
            return True
        return False
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
 
 
class Bishop:
    """Класс слона. Пока что заглушка, которая может ходить в любую клетку."""
 
    def __init__(self, color):
        self.color = color
 
    def get_color(self):
        return self.color
 
    def char(self):
        return 'B'
 
    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        
        piece1 = board.get_piece(row1, col1) # фигура на той клетке

        # если не пустая я своего цвета
        if not (piece1 is None) and piece1.get_color() == self.color:
            return False
        # по идее надо еще реализовать по диагонали
        if abs(row1 - row) != abs(col1 - col):
            return False
        for i in range(row + 1, row1):
            for j in range(col + 1, col1):
                if board.field[i][j] != None:
                    return False
        for i in range(row + 1, row1):
            for j in range(col - 1, col1, -1):
                if board.field[i][j] != None:
                    return False
        for i in range(row - 1, row1, -1):
            for j in range(col + 1, col1):
                if board.field[i][j] != None:
                    return False
        for i in range(row - 1, row1, -1):
            for j in range(col - 1, col1, -1):
                if board.field[i][j] != None:
                    return False            
        if (self.color == WHITE and board.shah_white) or (self.color == BLACK and board.shah_black):
            board_model = bord.Board()
            for idx in range(8):
                board_model.field[idx] = board.field[idx].copy()
            board_model.shah_white = True
            board_model.shah_black = True
            board_model.field[row1][col1] = board_model.field[row][col]
            board_model.field[row][col] = None 
            if board_model.is_shah(self.color):
                print('336по шаху')
                return False
 
    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)