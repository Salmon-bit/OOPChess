from .chess_unit import ChessUnit
from math import dist


class King(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)
    
    def map_view(self):
        return '+'
    
    def check_available(self, dest, map, flag=False):
        if (abs(self.pos[0] - dest[0]) <= 1 and abs(self.pos[1] - dest[1])) <= 1:
            if map.get_unit(dest) is None or flag:
                return True
            else:
                raise ValueError('Destination point must be None')
        else:
            raise ValueError('Invalid move for a King')
    
    def goto(self, dest, map):
        if self.side == 'white':
            if dist(dest, map.black_king_pos) <= 2:
                raise ValueError('Between two kings must be at least 2 free squares')
        else:
            if dist(dest, map.white_king_pos) <= 2:
                raise ValueError('Between two kings must be at least 2 free squares')
        
        map.set_king_pos(dest, self.side)

        super().goto(dest, map)
    
    def attack(self, dest, map):
        if (self.side == 'white' and map.get_unit(dest).side == 'black') or (self.side == 'black' and map.get_unit(dest).side == 'white'):
            if self.check_available(dest, map, flag=True):
                map.set_unit(dest, None)
                map.set_unit(self.pos, None)
                map.set_unit(dest, self)
        else:
            raise ValueError(f'Attacking unit must be other side, not {self.side}!')

        if self.side == 'white':
            map.white_king_pos = dest
        else:
            map.black_king_pos = dest
