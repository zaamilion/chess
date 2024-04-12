from figures import Rook, Knight, Bishop, Queen, King, Pawn
from consts import WHITE, BLACK
from global_commands import opponent, correct_coords


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        self.shah_white = False
        self.shah_black = False
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]
 
    def current_player_color(self):
        return self.color
 
    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()
 
    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None
 
    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''
 
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True
    
    def is_shah(self, color): # по цвету короля
        c = 0
        for row_king in range(8):
            for col_king in range(8):
                c += 1
                print(f'Ищу короля81 {c}')
                if type(self.field[row_king][col_king]) == King:
                    if self.field[row_king][col_king].color != color:
                        continue
                    print(f'85Нашел короля {row_king, col_king}')
                    for row_figure in range(8):
                        for col_figure in range(8):
                            piece = self.field[row_figure][col_figure]
                            print(f'89Нашел фигуру {row_figure, col_figure, type(piece), piece.color if piece is not None else None}')
                            if piece == None or piece.color == color:
                                print('91она не та')
                                continue
                            print('93проверяю хавает чи не')
                            if piece.can_attack(self, row_figure, col_figure, row_king, col_king):
                                print('хавает95')
                                return True
                    return False
        return False