from __future__ import annotations
from .chess_unit import ChessUnit
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chess_table import ChessTable

class Pawn(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)

        self.moved = False

    def map_view(self):
        return 'P'

    def goto(self, dest: tuple[int, int], map: ChessTable):
        if self.moved:
            if self.side == 'white':
                if self.pos[0] - 1 == dest[0] and self.pos[1] == dest[1]:
                    if self.check_available(dest, map):
                        self.pos = dest
                    else:
                        raise ValueError('Destination point must be None')
                else:
                    raise ValueError('Invalid move for Pawn')
            else:
                if self.pos[0] + 1 == dest[0] and self.pos[1] == dest[1]:
                    if self.check_available(dest, map):
                        self.pos = dest
                    else:
                        raise ValueError('Destination point must be None')
                else:
                    raise ValueError('Invalid move for Pawn')
        else:
            if self.side == 'white':
                if (self.pos[0] - 1 == dest[0] and self.pos[1] == dest[1]) or (self.pos[0] - 2 == dest[0] and self.pos[1] == dest[1]):
                    if self.check_available(dest, map):
                        self.pos = dest
                    else:
                        raise ValueError('Destination point must be None')
                else:
                    raise ValueError('Invalid move for Pawn')
            else:
                if (self.pos[0] + 1 == dest[0] and self.pos[1] == dest[1]) or (self.pos[0] + 2 == dest[0] and self.pos[1] == dest[1]):
                    if self.check_available(dest, map):
                        self.pos = dest
                    else:
                        raise ValueError('Destination point must be None')
                else:
                    raise ValueError('Invalid move for Pawn')

        self.moved = True