class Player:
    """
    Basic Player class, with shape attribute, and potentially a name if used later.
    """
    def __init__(self, name):
        self.shape = ''
        self.name = name


class Brain:
    """Main engine of the game, deal with various functions such as assigning shape O or X to player,
    checking the validity of a move, processing the move, checking if a win, etc."""
    def __init__(self):
        """Init a Brain object."""
        self.matrix = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.round = 0
        self.whose_turn = None
        self.positions = {
            'A0': {'row': 0, 'col': 0},
            'A1': {'row': 1, 'col': 0},
            'A2': {'row': 2, 'col': 0},
            'B0': {'row': 0, 'col': 1},
            'B1': {'row': 1, 'col': 1},
            'B2': {'row': 2, 'col': 1},
            'C0': {'row': 0, 'col': 2},
            'C1': {'row': 1, 'col': 2},
            'C2': {'row': 2, 'col': 2},
        }

    def ask_shape(self):
        """Ask the player the shape he wants to play with."""
        shapes = ['X', 'O']
        player_shape = input("Please choose your shape (X or O): ").upper()
        while player_shape not in shapes:
            player_shape = input("Entry incorrect. Please try again.\nChoose between X and O: ").upper()
        self.player1.shape = player_shape
        if shapes.index(player_shape) == 0:
            self.player2.shape = shapes[1]
        else:
            self.player2.shape = shapes[0]
        print("\nBy convention, the player with X starts first.")

    def make_move(self):
        """Ask user to enter a move, then process it."""
        if self.round % 2 == 0:
            symb = 'X'
        else:
            symb = 'O'
        if self.player1.shape == symb:
            self.whose_turn = self.player1
        else:
            self.whose_turn = self.player2
        move = input(f"\nPlayer {symb}, enter a position (e.g. A0):  ").upper()

        while (not self.valid_entry(move)) or (not self.legal_move(move)):
            if not self.valid_entry(move):
                move = input(
                    f"Entry incorrect. Please try again.\nPlayer {symb}, enter a position (e.g. A0):  ").upper()
            else:
                move = input(f"This position is already taken. Please try again.\n"
                             f"Player {symb}, enter a position (e.g. A0):  ").upper()

        row = self.positions[move]['row']
        col = self.positions[move]['col']
        self.matrix[row][col] = symb
        self.round += 1

    def valid_entry(self, move: str) -> bool:
        """Check if the move input is valid."""
        return move in self.positions.keys()

    def legal_move(self, move: str) -> bool:
        """Check if the move is legal, or already taken."""
        row = self.positions[move]['row']
        col = self.positions[move]['col']
        return self.matrix[row][col] == " "

    def is_win_horizontal(self) -> bool:
        """Check if horizontal win occurred"""
        symb = self.whose_turn.shape
        for row in self.matrix:
            hor_count = 0
            for col in row:
                if col == symb:
                    hor_count += 1
            if hor_count == 3:
                return True
        return False

    def is_win_vertical(self) -> bool:
        """Check if vertical win occurred"""
        symb = self.whose_turn.shape
        for col in [0, 1, 2]:
            ver_count = 0
            for row in [0, 1, 2]:
                if self.matrix[row][col] == symb:
                    ver_count += 1
            if ver_count == 3:
                return True
        return False

    def is_win_diagonal(self) -> bool:
        """Check if diagonal win occurred"""
        symb = self.whose_turn.shape
        if self.matrix[0][0] == symb and self.matrix[1][1] == symb and self.matrix[2][2] == symb:
            return True
        elif self.matrix[0][2] == symb and self.matrix[1][1] == symb and self.matrix[2][0] == symb:
            return True
        else:
            return False

    def is_win(self) -> bool:
        """Return True if either horizontal win, vertical win or diagonal win."""
        return self.is_win_horizontal() or self.is_win_vertical() or self.is_win_diagonal()

    def reset(self):
        """Re-initialize the game at the start."""
        # If I want to keep custom names in the future
        # name1 = self.player1.name
        # name2 = self.player2.name
        self.__init__()
