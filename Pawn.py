from Piece import Piece
import BuildBoard


class Pawn(Piece):
    def __init__(self, x, y, team, character, canvas, cell_size):
        super().__init__(x, y, team, character, canvas, cell_size)
        self.has_moved = False

    # If piece pos can move to new cell x,y then move
    # Only check if valid move
    def canMoveTo(self, from_x, from_y, to_x, to_y, chess_board):
        print(f"From: {from_x}, {from_y} To: {to_x}, {to_y}")
        isValidMove = False
        if chess_board[to_y][to_x] is None:
            if self.has_moved:
                if from_y - to_y == 1:
                    isValidMove = True
            else:
                if from_y - to_y in [1, 2]:
                    self.has_moved = True
                    isValidMove = True

        return isValidMove

