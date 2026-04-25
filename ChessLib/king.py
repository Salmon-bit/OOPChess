from .chess_unit import ChessUnit


class King(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)
    
    def map_view(self):
        return '+'