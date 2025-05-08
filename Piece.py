from PIL import Image, ImageTk
import BuildBoard


class Piece:
    def __init__(self, x, y, team, character, canvas, cell_size):
        self.x = x
        self.y = y
        self.team = team
        self.character = character
        self.canvas = canvas
        self.cell_size = cell_size
        self.photo = None
        self.image = None
        self.id = None

        piece_map = {
            'P': 'pawn',
            'N': 'knight',
            'B': 'bishop',
            'R': 'rook',
            'Q': 'queen',
            'K': 'king'
        }
        piece_name = piece_map[character[1].upper()]

        if piece_name:
            try:
                if team == 'white':
                    self.image = Image.open(f'Images/{piece_name}White.png')
                elif team == 'black':
                    self.image = Image.open(f'Images/{piece_name}Black.png')
                else:
                    self.image = None
            except FileNotFoundError as e:
                print(f"No Image Found: {e}")

    def display(self):
        # Resize Image to fit the cell size
        if self.image is not None:
            try:
                self.image = self.image.resize((self.cell_size, self.cell_size), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(self.image)

                # Create image on canvas
                self.id = self.canvas.create_image(self.x * self.cell_size + self.cell_size // 2,
                                                   self.y * self.cell_size + self.cell_size // 2,
                                                   image=self.photo,
                                                   anchor='center')
            except Exception as e:
                print(f"Error: {e}")

    def move(self, row, col, x, y, canvas, cell_size, chess_board):
        # Move image to cell
        canvas.coords(self.id, x + (cell_size // 2), y + cell_size // 2)

        # Update chess board
        chess_board[row][col] = self

        # Update pieces x y coords
        chess_board[self.y][self.x] = None
        self.x, self.y = col, row
