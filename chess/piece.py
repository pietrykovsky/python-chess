from copy import deepcopy


class Piece:
    """Base class for pieces."""

    def __init__(self, position, color):
        """
        Initializes a new instance of a Piece.

        :param position: The position of the piece on the board
        :type position: tuple[int, int]
        :param color: The color of the piece
        :type color: str
        """
        self.position = position
        self.color = color

    def get_possible_moves(self, board):
        """
        Get possible moves for the piece on the board.

        :param board: The board
        :type board: chess.piece.Board
        """
        raise NotImplementedError

    def is_valid_move(self, target_position, board):
        # not sure whether this should be here or in the board class, might be moved in the future
        board_after_move = deepcopy(board)
        board_after_move.update(
            piece_position=self.position, target_position=target_position
        )
        if (
            board_after_move.is_check(color=self.color)
            and board.get_state(color=self.color, position=target_position) is not None
        ):
            return True
        return False


class Pawn(Piece):
    pass


class King(Piece):
    pass


class Queen(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass
