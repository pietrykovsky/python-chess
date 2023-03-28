# not sure whether this is necessary, it might be removed


class Move:
    """Class representing a move."""

    def __init__(self, start_pos, end_pos, piece=None, captured_piece=None):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.piece = piece
        self.captured_piece = captured_piece
