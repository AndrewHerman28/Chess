from Piece import Piece
import BuildBoard


class Rook(Piece):
    def __init__(self, x, y, team, character, canvas, cell_size):
        super().__init__(x, y, team, character, canvas, cell_size)
        self.has_moved = False

    """
    Rooks Valid Moves Are
    As far left, right, up down until:
        Hit edge, or another piece
    Castle:
        Can castle as long as king and rook has not moved
    """

    def canMoveTo(self, from_x, from_y, to_x, to_y, chess_board):
        print(f"From: {from_x}, {from_y} To: {to_x}, {to_y}")
        isValidMove = False
        if chess_board[to_y][to_x] is None:
            # Side ways movement
            if from_x is not to_x and from_y == to_y:
                isValidMove = True

            # Up and Down movement
            if from_y is not to_y and from_x == to_x:
                isValidMove = True

        return isValidMove
