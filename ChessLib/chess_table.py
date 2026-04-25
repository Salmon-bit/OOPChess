from __future__ import annotations
from .rook import Rook
from .bishop import Bishop
from .knight import Knight
from .king import King
from .queen import Queen
from .pawn import Pawn
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chess_unit import ChessUnit


class ChessTable:
    """This class provides an interface to create and manipulate chess board.\n
    Methods:
     * __init__: Creates a new chess board. Doesn`t need any arguments
     * get_unit: Returns a unit from the board. Must have one argument - position
     * set_unit: Sets a unit to the board. Must have two arguments - position and unit. Unit must be None or SubClass from ChessUnit
     * move_unit: Moves a unit from one position to another. Must have two arguments - start position and end position
     * __str__: Provides the visual representation of the board.
    """
    def __init__(self):
        self.map = []

        for row in range(8):
            self.map.append([])
            for col in range(8):
                match col:
                    case 0 | 7:
                        if row == 0:
                            self.map[row].append(Rook((row, col), 'black'))
                        elif row == 7:
                            self.map[row].append(Rook((row, col), 'white'))
                        elif row == 1:
                            self.map[row].append(Pawn((row, col), 'black'))
                        elif row == 6:
                            self.map[row].append(Pawn((row, col), 'white'))
                        else:
                            self.map[row].append(None)
                    case 1 | 6:
                        if row == 0:
                            self.map[row].append(Knight((row, col), 'black'))
                        elif row == 7:
                            self.map[row].append(Knight((row, col), 'white'))
                        elif row == 1:
                            self.map[row].append(Pawn((row, col), 'black'))
                        elif row == 6:
                            self.map[row].append(Pawn((row, col), 'white'))
                        else:
                            self.map[row].append(None)
                    case 2 | 5:
                        if row == 0:
                            self.map[row].append(Bishop((row, col), 'black'))
                        elif row == 7:
                            self.map[row].append(Bishop((row, col), 'white'))
                        elif row == 1:
                            self.map[row].append(Pawn((row, col), 'black'))
                        elif row == 6:
                            self.map[row].append(Pawn((row, col), 'white'))
                        else:
                            self.map[row].append(None)
                    case 3:
                        if row == 0:
                            self.map[row].append(Queen((row, col), 'black'))
                        elif row == 7:
                            self.map[row].append(Queen((row, col), 'white'))
                        elif row == 1:
                            self.map[row].append(Pawn((row, col), 'black'))
                        elif row == 6:
                            self.map[row].append(Pawn((row, col), 'white'))
                        else:
                            self.map[row].append(None)
                    case 4:
                        if row == 0:
                            self.map[row].append(King((row, col), 'black'))
                        elif row == 7:
                            self.map[row].append(King((row, col), 'white'))
                        elif row == 1:
                            self.map[row].append(Pawn((row, col), 'black'))
                        elif row == 6:
                            self.map[row].append(Pawn((row, col), 'white'))
                        else:
                            self.map[row].append(None)

    def __str__(self):
        """Provides the visual representation of the board."""
        output = "+---+" + "---+" * 8 + "\n|"
        for row in range(8):
            output += " " + str(8 - row) + " |"
            for unit in self.map[row]:
                if unit:
                    output += " " + unit.map_view() + " |"
                else:
                    output += " ∙ |"
            output += "\n|"
        output = output[:-1]
        output += "+---+" + "---+" * 8 + "\n"
        output += "| x | a | b | c | d | e | f | g | h |\n"
        output += "+---+" + "---+" * 8
        return output

    def get_unit(self, position: tuple) -> ChessUnit:
        """Returns a unit from the board. Must have one argument - position"""
        return self.map[position[0]][position[1]]

    def set_unit(self, position: tuple, piece: ChessUnit | None) -> None:
        """Sets a unit to the board. Must have two arguments - position and unit. Unit must be None or SubClass from ChessUnit"""
        if self.get_unit(position) is not None:
            if piece is not None:
                raise ValueError("The Destination place must be empty!")

        self.map[position[0]][position[1]] = piece

    def get_list(self) -> list[list[ChessUnit | None]]:
        """Returns the board as a list"""
        return self.map

    def move_unit(self, position: tuple[int, int], destination: tuple[int, int]) -> None:
        """Moves a unit from one position to another. Must have two arguments - position and destination"""
        if (self.get_unit(position) is not None) and\
           (self.get_unit(destination) is None) and\
           (self.get_unit(position).check_available(destination, self)):

            move_unit = self.get_unit(position)
            move_unit.goto(destination, self)
            self.map[destination[0]][destination[1]] = move_unit
            self.map[position[0]][position[1]] = None
        else:
            raise ValueError("Invalid move! Destination point must be None and position must be ChessUnit subclass.")

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    table = ChessTable()
    print(table)
