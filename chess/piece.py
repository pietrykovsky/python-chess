from abc import ABC, abstractmethod

from .const import BOARD_SIZE
from .exception import InvalidMoveException


class Piece(ABC):
    """Base class for pieces."""

    def __init__(self, position: tuple[int, int], color: str):
        """
        Initializes a new instance of a Piece.

        :param position: The position of the piece on the board
        :param color: The color of the piece
        """
        self._color = color
        self._position = position

    @property
    def position(self):
        """
        Get the current position of the piece.
        """
        return self._position

    @property
    def color(self):
        """
        Get the color of the piece.
        """
        return self._color

    def get_possible_positions(
        self, board_size: int = BOARD_SIZE
    ) -> list[tuple[int, int]] | None:
        """
        Get possible moves for the piece on the board. Does not consider the board rules.

        :param board_size: The size of the board
        :return: A list of tuples containing possible target positions
        or None if there are no possible.
        """
        positions = []
        for row in range(board_size):
            for col in range(board_size):
                position = row, col
                if self.can_move(target_position=position):
                    positions.append(position)
        return positions if len(positions) > 0 else None

    def move(self, target_position: tuple[int, int]):
        """
        Update the position of the piece.

        :param target_position: The target position to move the piece to.
        :raises InvalidMoveException:
        """
        if self.can_move(target_position):
            self._position = target_position
        else:
            raise InvalidMoveException(
                f"Move of {self} from {self._position} to {target_position} is invalid!"
            )

    @abstractmethod
    def can_move(self, target_position: tuple[int, int]):
        """
        Check if the move is allowed, does not consider the board rules or other pieces.

        :param target_position: The target position to move the piece to.
        :raises NotImplementedError:
        """
        raise NotImplementedError


class Pawn(Piece):
    """
    Class representing a Pawn piece.
    """


class King(Piece):
    """
    Class representing a King piece.
    """


class Queen(Piece):
    """
    Class representing a Queen piece.
    """


class Rook(Piece):
    """
    Class representing a Rook piece.
    """


class Knight(Piece):
    """
    Class representing a Knight piece.
    """


class Bishop(Piece):
    """
    Class representing a Bishop piece.
    """
