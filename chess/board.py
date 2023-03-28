from .const import COLOR_WHITE, COLOR_BLACK
from .piece import Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    """
    Class representing a chess board.
    """

    def __init__(self, state=None):
        """
        Initialize a board.

        :param state: The state of the board
        :type state: list[list]
        """
        self.state = (
            [
                [
                    Rook(position=(0, 0), color=COLOR_BLACK),
                    Knight(position=(0, 1), color=COLOR_BLACK),
                    Bishop(position=(0, 2), color=COLOR_BLACK),
                    Queen(position=(0, 3), color=COLOR_BLACK),
                    King(position=(0, 4), color=COLOR_BLACK),
                    Bishop(position=(0, 5), color=COLOR_BLACK),
                    Knight(position=(0, 6), color=COLOR_BLACK),
                    Rook(position=(0, 7), color=COLOR_BLACK),
                ],
                [Pawn(position=(1, col), color=COLOR_BLACK) for col in range(8)],
                [None] * 8,
                [None] * 8,
                [None] * 8,
                [None] * 8,
                [Pawn(position=(6, col), color=COLOR_WHITE) for col in range(8)],
                [
                    Rook(position=(7, 0), color=COLOR_WHITE),
                    Knight(position=(7, 1), color=COLOR_WHITE),
                    Bishop(position=(7, 2), color=COLOR_WHITE),
                    Queen(position=(7, 3), color=COLOR_WHITE),
                    King(position=(7, 4), color=COLOR_WHITE),
                    Bishop(position=(7, 5), color=COLOR_WHITE),
                    Knight(position=(7, 6), color=COLOR_WHITE),
                    Rook(position=(7, 7), color=COLOR_WHITE),
                ],
            ]
            if state is None
            else state
        )

    def update(self, piece_position, target_position):
        """
        Updates the board state with a piece move from piece_position to target_position.

        :param piece_position: The position of the piece to be moved.
        :type piece_position: tuple[int, int]
        :param target_position: The position where the piece should be moved to.
        :type target_position: tuple[int, int]
        """
        raise NotImplementedError

    def get_pieces(self, color):
        """
        Get a list of all pieces on board of the given color.

        :param color: The color of the player whose possible moves are to be found.
        :type color: str
        :return: A list pieces.
        :rtype: list[chess.piece.Piece]
        """
        return list(
            filter(lambda piece: piece is not None and piece.color == color),
            [piece for row in self.state for piece in row],
        )

    def get_possible_moves(self, color):
        """
        Get a list of all possible moves for the given color on the current board state.

        :param color: The color of the player whose possible moves are to be found.
        :type color: str
        :return: A list of tuples representing all possible moves for the given color.
        :rtype: list[tuple[int, int]]
        """
        return [
            piece.get_possible_moves()
            for piece in self.get_pieces(color)
            if piece.get_possible_moves is not None
        ]

    def get_state(self, color, position):
        """
        Get the state of a given position on the board from given color perspective.

        :param color: The color of the player requesting the state.
        :type color: str
        :param position: The position on the board to get the state of.
        :type position: tuple[int, int]
        :return: True if there is no piece of given color at the position and False otherwise
        :rtype: bool
        """
        row, col = position
        if getattr(self.state[row][col], "color") == color:
            return False
        return True

    def get_king_position(self, color):
        """
        Get the position of the king for the given color.

        :param color: The color of the king to find.
        :type color: str
        :return: A tuple representing the position of the king.
        :rtype: tuple[int, int] or None
        """
        for row in self.state:
            for piece in row:
                if isinstance(piece, King) and piece.color == color:
                    return piece.position
        return None

    def is_check(self, color):
        """
        Check if the given color is currently in check.

        :param color: The color of the player to check for check.
        :type color: str
        :return: True if the player is in check, False otherwise.
        """
        enemy_moves = self.get_possible_moves(
            color=COLOR_BLACK if color == COLOR_WHITE else COLOR_WHITE
        )
        king_position = self.get_king_position(color=color)
        if king_position in enemy_moves:
            return True
        return False

    def is_checkmate(self, color):
        """
        Check if the given color is currently in checkmate.

        :param color: The color of the player to check for checkmate.
        :type color: str
        :return: True if the player is in checkmate, False otherwise.
        :rtype: bool
        """
        if self.is_check(color=color) and len(self.get_possible_moves(color)) == 0:
            return True
        return False

    def is_stalemate(self, color):
        """
        Check if the given color is currently in stalemate.

        :param color: The color of the player to check for stalemate.
        :type color: str
        :return: True if the player is in stalemate, False otherwise.
        :rtype: bool
        """
        raise NotImplementedError
