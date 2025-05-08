import tkinter as tk
from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King
import BuildBoard

# Create main window
screen_size = 800
cell_size = screen_size // 8

window = tk.Tk()
window.title("Chess Board")
canvas = tk.Canvas(window, width=screen_size, height=screen_size)
canvas.pack()

BuildBoard.make_color_grid(canvas, cell_size)

chess_board = []

board_layout = [
    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
    ['BP︎'] * 8,
    ['.'] * 8,
    ['.'] * 8,
    ['.'] * 8,
    ['.'] * 8,
    ['WP'] * 8,
    ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
]

chess_board = [
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
]

piece_dict = {
    'BR': Rook,
    'BN': Knight,
    'BB': Bishop,
    'BQ': Queen,
    'BK': King,
    'BP': Pawn,
    'WR': Rook,
    'WN': Knight,
    'WB': Bishop,
    'WQ': Queen,
    'WK': King,
    'WP': Pawn,
    '.': lambda x, y, team, character, canvas, cell_size: None  # Handle empty cells
}

BuildBoard.create_chess_board(board_layout, chess_board, piece_dict, canvas, cell_size)

prev_cell = None
prev_piece = None
tempArr = []


def on_cell_click(event):
    global prev_cell
    # Find cell user clicked on
    col = event.x // cell_size
    row = event.y // cell_size
    x1, y1 = col * cell_size, row * cell_size
    x2, y2 = x1 + cell_size, y1 + cell_size

    # Highlight selected cell
    new_cell = canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=3)

    # User selected piece
    picked_piece = chess_board[row][col]
    tempArr.append(picked_piece)

    # If two cells are selected
    if len(tempArr) == 2:
        # If piece exist
        if tempArr[0]:
            # If valid move
            if tempArr[0].canMoveTo(tempArr[0].x, tempArr[0].y, col, row, chess_board):
                # Move piece
                tempArr[0].move(row, col, x1, y1, piece_dict, canvas, cell_size, chess_board, tempArr[0])
                chess_board[row][col] = None

        tempArr.pop(0)
        tempArr.pop(0)

    # Remove previously selected cell-
    if prev_cell:
        canvas.delete(prev_cell)  # Unhighlight old cell
        prev_cell = new_cell
    else:
        prev_cell = new_cell


# Bind mouse click to canvas
canvas.bind("<Button-1>", on_cell_click)

window.mainloop()
