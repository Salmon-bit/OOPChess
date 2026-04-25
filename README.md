# OOPChess

A Python chess library built with object-oriented programming principles. Provides a board representation, piece classes, and movement logic as a reusable package.

## Project Structure

```
OOPChess/
├── main.py              # Entry point / usage example
├── setup.py             # Package setup
├── setup.cfg
└── ChessLib/
    ├── __init__.py      # Public package exports
    ├── chess_unit.py    # Base class for all pieces
    ├── chess_table.py   # Chess board logic
    ├── rock.py          # Rook piece
    ├── bishop.py        # Bishop piece
    ├── knight.py        # Knight piece
    ├── king.py          # King piece
    ├── queen.py         # Queen piece
    └── pawn.py          # Pawn piece
```

## Requirements

- Python 3.10+ (uses `match`/`case` syntax)

No external dependencies.

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/Salmon-bit/OOPChess
cd OOPChess
pip install -e .
```

Or just use `ChessLib` directly by placing it next to your script.

## Quick Start

```python
from ChessLib.chess_table import ChessTable

# Create a new board with pieces in starting positions
board = ChessTable()
print(board)

# Get a piece at a position (row, col) — 0-indexed, top-left is (0, 0)
piece = board.get_unit((7, 1))  # White Knight
print(piece)  # White Knight at b-1.

# Move a piece
board.move_unit((7, 1), (5, 2))
print(board)
```

### Board output example

```
+---+---+---+---+---+---+---+---+---+
| 8 | R | K | B | Q | + | B | K | R |
| 7 | P | P | P | P | P | P | P | P |
| 6 | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ |
| 5 | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ |
| 4 | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ |
| 3 | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ | ∙ |
| 2 | P | P | P | P | P | P | P | P |
| 1 | R | K | B | Q | + | B | K | R |
+---+---+---+---+---+---+---+---+---+
| x | a | b | c | d | e | f | g | h |
+---+---+---+---+---+---+---+---+---+
```

Piece symbols: `R` = Rook, `K` = Knight, `B` = Bishop, `Q` = Queen, `+` = King, `P` = Pawn

## API Reference

### `ChessTable`

The main board class.

| Method                             | Description                                                    |
| ---------------------------------- | -------------------------------------------------------------- |
| `__init__()`                       | Creates a new board with pieces in standard starting positions |
| `get_unit(position)`               | Returns the piece at `(row, col)`, or `None` if empty          |
| `set_unit(position, piece)`        | Places a piece (or `None`) at a position                       |
| `move_unit(position, destination)` | Moves a piece from one square to another                       |
| `get_list()`                       | Returns the full board as a `list[list]`                       |

### `ChessUnit` (base class for all pieces)

All piece classes (`Rock`, `Bishop`, `Knight`, `King`, `Queen`, `Pawn`) inherit from `ChessUnit`.

| Method                       | Description                                             |
| ---------------------------- | ------------------------------------------------------- |
| `__init__(pos, side)`        | `pos` is `(row, col)`, `side` is `'white'` or `'black'` |
| `get_pos()`                  | Returns current position as `(row, col)`                |
| `convert_pos()`              | Converts position to chess notation, e.g. `('b', 1)`    |
| `check_available(dest, map)` | Returns `True` if the destination square is empty       |
| `goto(dest, map)`            | Moves the piece to `dest` if available                  |
| `map_view()`                 | Returns the single-character board symbol for the piece |

### Coordinate system

Positions use `(row, col)` tuples, 0-indexed from the top-left:

- `(0, 0)` = top-left = `a8` (black's back rank)
- `(7, 7)` = bottom-right = `h1` (white's back rank)

## Extending with a new piece

Subclass `ChessUnit` and implement `map_view()`:

```python
from .chess_unit import ChessUnit

class MyPiece(ChessUnit):
    def __init__(self, pos, side):
        super().__init__(pos, side)

    def map_view(self) -> str:
        return 'M'  # Symbol shown on the board
```

Then add it to `chess_table.py` imports and `__init__.py` exports.
