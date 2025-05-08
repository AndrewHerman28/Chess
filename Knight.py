from Piece import Piece
import BuildBoard


class Knight(Piece):
    def __init__(self, x, y, team, character, canvas, cell_size):
        super().__init__(x, y, team, character, canvas, cell_size)

    # IF DIFFERENCE of x value of 1, then difference of y must be 2
    # IF DIFFERENCE of y value of 1, then difference of x must be 2
    def canMoveTo(self, from_x, from_y, to_x, to_y, chess_board):
        print(f"From: {from_x}, {from_y} To: {to_x}, {to_y}")
        isValidMove = False
        if chess_board[to_y][to_x] is None:
            x_diff = abs(to_x - from_x)
            y_diff = abs(to_y - from_y)

            if x_diff == 1 and y_diff == 2 or x_diff == 2 and y_diff == 1:
                isValidMove = True

        return isValidMove
