from abc import ABC, abstractmethod

from .const import BOARD_SIZE, COLOR_WHITE
from .exception import InvalidMoveException


class HasMovedMixin:
    """
    Mixin class for adding has_move functionality.
    """

    @property
    def has_moved(self):
        return getattr(self, "_has_moved", False)

    @has_moved.setter
    def has_moved(self, value: bool):
        self._has_moved = value


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
                f"Move of {self} from {self.position} to {target_position} is invalid!"
            )

    @abstractmethod
    def can_move(self, target_position: tuple[int, int]) -> bool:
        """
        Check if the move is allowed, does not consider the board rules or other pieces.

        :param target_position: The target position to move the piece to.
        :return: True if move is valid and False otherwise
        """


class Pawn(HasMovedMixin, Piece):
    """
    Class representing a Pawn piece.
    """

    def __str__(self):
        return "Pawn"

    def move(self, target_position: tuple[int, int]):
        super().move(target_position)
        if not self.has_moved:
            self.has_moved = True

    def can_move(self, target_position: tuple[int, int]) -> bool:
        dx = self.position[1] - target_position[1]
        dy = (
            self.position[0] - target_position[0]
            if self.color == COLOR_WHITE
            else target_position[0] - self.position[0]
        )
        if (dy == 1 and dx == 0) or (dy == 2 and dx == 0 and not self.has_moved):
            return True
        return False


class King(HasMovedMixin, Piece):
    """
    Class representing a King piece.
    """

    def __str__(self) -> str:
        return "King"

    def move(self, target_position: tuple[int, int]):
        super().move(target_position)
        if not self.has_moved:
            self.has_moved = True

    def can_move(self, target_position: tuple[int, int]) -> bool:
        dx = abs(self.position[1] - target_position[1])
        dy = abs(self.position[0] - target_position[0])
        if dx == 1 and dy in (0, 1) or dy == 1 and dx in (0, 1):
            return True
        return False


class Queen(Piece):
    """
    Class representing a Queen piece.
    """

    def __str__(self) -> str:
        return "Queen"

    def can_move(self, target_position: tuple[int, int]) -> bool:
        dx = abs(self.position[1] - target_position[1])
        dy = abs(self.position[0] - target_position[0])
        if dx == dy != 0 or dx == 0 != dy or dx != 0 == dy:
            return True
        return False


class Rook(HasMovedMixin, Piece):
    """
    Class representing a Rook piece.
    """

    def __str__(self) -> str:
        return "Rook"

    def move(self, target_position: tuple[int, int]):
        super().move(target_position)
        if not self.has_moved:
            self.has_moved = True

    def can_move(self, target_position: tuple[int, int]) -> bool:
        dx = abs(self.position[1] - target_position[1])
        dy = abs(self.position[0] - target_position[0])
        if dx == 0 != dy or dx != 0 == dy:
            return True
        return False


class Knight(Piece):
    """
    Class representing a Knight piece.
    """

    def __str__(self) -> str:
        return "Knight"

    def can_move(self, target_position: tuple[int, int]) -> bool:
        dx = abs(self.position[1] - target_position[1])
        dy = abs(self.position[0] - target_position[0])
        if dx == 1 and dy == 2:
            return True
        return False


class Bishop(Piece):
    """
    Class representing a Bishop piece.
    """

    def __str__(self) -> str:
        return "Bishop"

    def can_move(self, target_position: tuple[int, int]) -> bool:
        dx = abs(self.position[1] - target_position[1])
        dy = abs(self.position[0] - target_position[0])
        if dx == dy != 0:
            return True
        return False
