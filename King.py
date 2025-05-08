from Piece import Piece
import BuildBoard


class King(Piece):
    def __init__(self, x, y, team, character, canvas, cell_size):
        super().__init__(x, y, team, character, canvas, cell_size)

        # If piece pos can move to new cell x,y then move
        # Only check if valid move

    def canMoveTo(self, from_x, from_y, to_x, to_y, chess_board):
        return True


