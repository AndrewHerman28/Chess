# Colors
import unicodedata

WHITE_TILE = "#EEEED2"
WOOD_TILE = "#B58863"
SELECTED_TILE = "#A9A9A9"


def make_color_grid(canvas, cell_size):
    for i in range(8):
        for j in range(8):
            cell_color = WHITE_TILE if (i + j) % 2 == 0 else WOOD_TILE
            x1 = i * cell_size
            y1 = j * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=cell_color, outline='black')


def clean_character(char):
    return ''.join(c for c in char if not unicodedata.category(c).startswith('M'))


def define_cell(x, y, team, character, piece_dict, canvas, cell_size):
    character = clean_character(character)
    temp_piece = piece_dict[character](x, y, team, character, canvas, cell_size)
    if temp_piece:
        temp_piece.display()
    return temp_piece


def create_chess_board(board_layout, chess_board, piece_dict, canvas, cell_size):
    # Create real chess board based off template
    for y, row in enumerate(board_layout):
        for x, cell in enumerate(row):
            first_letter = cell[0].upper()
            if first_letter == 'W':
                team = 'white'
            elif first_letter == 'B':
                team = 'black'
            else:
                team = None
            piece = define_cell(x, y, team, cell, piece_dict, canvas, cell_size)
            if piece:
                chess_board[y][x] = piece
                piece.display()
