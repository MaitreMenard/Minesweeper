class Tile:

    def __init__(self):
        self.adjacent_mines = 0
        self.is_mine = False
        self.flagged = False
        self.revealed = False

    def __str__(self):
        if self.is_mine:
            return "x"
        else:
            return str(self.adjacent_mines)
