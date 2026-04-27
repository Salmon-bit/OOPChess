from .chess_unit import ChessUnit


class Knight(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)
    
    def map_view(self):
        return 'K'

    def check_available(self, dest, map, flag=False):
        if super().check_available(dest, map) or flag:
            if self.pos[0] + 1 == dest[0] and self.pos[1] + 2 == dest[1]:
                return True
            elif self.pos[0] - 1 == dest[0] and self.pos[1] + 2 == dest[1]:
                return True
            elif self.pos[0] + 1 == dest[0] and self.pos[1] - 2 == dest[1]:
                return True
            elif self.pos[0] - 1 == dest[0] and self.pos[1] - 2 == dest[1]:
                return True
            elif self.pos[0] - 2 == dest[0] and self.pos[1] + 1 == dest[1]:
                return True
            elif self.pos[0] - 2 == dest[0] and self.pos[1] - 1 == dest[1]:
                return True
            elif self.pos[0] + 2 == dest[0] and self.pos[1] + 1 == dest[1]:
                return True
            elif self.pos[0] + 2 == dest[0] and self.pos[1] - 1 == dest[1]:
                return True
            else:
                return False

    def goto(self, dest: tuple[int, int], map):
        if self.check_available(dest, map):
            self.pos = dest
        else:
            raise ValueError('Invalid move for a knight!')

    def attack(self, dest: tuple[int, int], map):
        if self.check_available(dest, map, flag=True) and map.get_unit(dest).side != self.side:
            map.set_unit(self.pos, None)
            self.pos = dest
            map.set_unit(dest, None)
            map.set_unit(dest, self)

        elif map.get_unit(dest).side == self.side:
            raise ValueError(f'Attacking unit must be other side, not {self.side}!')
