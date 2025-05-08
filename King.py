from Piece import Piece
import BuildBoard


class King(Piece):
    def __init__(self, x, y, team, character, canvas, cell_size):
        super().__init__(x, y, team, character, canvas, cell_size)
        self.has_moved = False

    def canMoveTo(self, from_x, from_y, to_x, to_y, chess_board):
        print(f"From: {from_x}, {from_y} To: {to_x}, {to_y}")
        isValidMove = False

        if chess_board[to_y][to_x] is None:
            x_diff = abs(to_x - from_x)
            y_diff = abs(to_y - from_y)
            if x_diff <= 1 and y_diff <= 1:
                isValidMove = True

        return isValidMove
