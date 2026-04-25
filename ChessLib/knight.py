from .chess_unit import ChessUnit


class Knight(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)
    
    def map_view(self):
        return 'K'