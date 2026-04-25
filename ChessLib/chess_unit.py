from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chess_table import ChessTable


class ChessUnit:
    def __init__(self, pos: tuple[int, int], side: str):
        self.pos = list(pos)
        self.side = side.lower()

        if side not in ['white', 'black']:
            raise ValueError(f'Unknown Side "{side}"')

        if self.pos[0] > 7 or self.pos[1] > 7 or self.pos[0] < 0 or self.pos[1] < 0:
            raise ValueError(f'Position must be in 8x8 field.')

    def get_pos(self) -> tuple[int, int]:
        return tuple(self.pos)

    def convert_pos(self, pos=None) -> tuple[str, int]:
        if pos is None:
            pos = tuple(self.pos)
        
        y = 8 - pos[0]
        x = pos[1] + 97

        return chr(x), y

    def check_available(self, dest: tuple[int, int], map: ChessTable) -> bool:
        if dest[0] > 7 or dest[1] > 7 or dest[0] < 0 or dest[1] < 0:
            raise ValueError(f'Position must be in 8x8 field.')
        
        if map.get_unit(dest) is None:
            return True
        else:
            return False

    def goto(self, dest: tuple[int, int], map: ChessTable) -> None:
        """Moves unit on the board
        :param dest tuple[int, int] - Destination point for the unit.
        :param map table.ChessTable - ChessTable object. Unit won`t change this object
        """
        if self.check_available(dest, map):
            self.pos = dest

    def __str__(self) -> str:
        return f"{self.side.title()} {self.__class__.__name__} at {self.convert_pos()[0]}-{self.convert_pos()[1]}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.pos}, '{self.side}')"


if __name__ == "__main__":
    unit = ChessUnit((5, 4), 'black')
    print(unit)
