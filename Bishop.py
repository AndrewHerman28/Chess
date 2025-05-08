from Piece import Piece


class Bishop(Piece):
    def __init__(self, x, y, team, character, canvas, cell_size):
        super().__init__(x, y, team, character, canvas, cell_size)

    def canMoveTo(self, from_x, from_y, to_x, to_y, chess_board):
        print(f"From: {from_x}, {from_y} To: {to_x}, {to_y}")
        isValidMove = False
        if chess_board[to_y][to_x] is None:
            if abs(to_x - from_x) == abs(to_y - from_y):
                isValidMove = True

        return isValidMove
