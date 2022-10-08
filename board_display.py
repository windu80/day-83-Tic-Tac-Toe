class Board:
    """Board class, in charge of displaying the current board of the tic-tac-toe game."""
    def __init__(self):
        """Init a Board object."""
        self.lines = {
            'line_abc': "     A   B   C ",
            'line0':    "0      |   |   ",
            'line1':    "1      |   |   ",
            'line2':    "2      |   |   ",
            'line_sep': "    -----------"
        }
        self.display = self.combine_lines()
        self.posA = 5
        self.posB = 9
        self.posC = 13
        self.pos_numbers = {
            0: self.posA, 1: self.posB, 2: self.posC,
        }

    def combine_lines(self) -> str:
        """Put the lines composing the board display together."""
        display = '\n' + self.lines['line_abc'] + \
                  '\n' + self.lines['line0'] + \
                  '\n' + self.lines['line_sep'] + \
                  '\n' + self.lines['line1'] + \
                  '\n' + self.lines['line_sep'] + \
                  '\n' + self.lines['line2']
        return display

    def update_display(self, list_pos: list) -> None:
        """Update the board according to the current game settings. Take a list of lists as input (normally the 'matrix'
        attribute from a Brain object)."""
        for i_row, row in enumerate(list_pos):
            line_no = f'line{i_row}'
            for i_col, col in enumerate(row):
                list_line = list(self.lines[line_no])
                list_line[self.pos_numbers[i_col]] = col
                self.lines[line_no] = "".join(list_line)
        self.display = self.combine_lines()
