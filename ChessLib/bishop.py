from .chess_unit import ChessUnit


class Bishop(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)
    
    def map_view(self):
        return 'B'