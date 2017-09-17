import random

from tile import Tile


class Minefield:
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.grid = None

        self._init_grid()
        self._add_mines_to_grid()

    def _init_grid(self):
        self.grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Tile())
            self.grid.append(row)

    def _add_mines_to_grid(self):
        mines = self.mines
        while mines > 0:
            mine_x = random.randrange(self.width)
            mine_y = random.randrange(self.height)
            if not self.grid[mine_y][mine_x].is_mine:
                self.grid[mine_y][mine_x].is_mine = True
                self._update_hints(mine_x, mine_y)
            else:
                continue
            mines -= 1

    def _update_hints(self, mine_x, mine_y):
        min_x = max(0, mine_x - 1)
        max_x = min(self.width - 1, mine_x + 1)
        min_y = max(0, mine_y - 1)
        max_y = min(self.height - 1, mine_y + 1)

        for i in range(min_y, max_y + 1):
            for j in range(min_x, max_x + 1):
                if i != mine_y or j != mine_x:
                    if not self.grid[i][j].is_mine:
                        self.grid[i][j].adjacent_mines += 1

    def has_mine_at_position(self, i, j):
        return self.grid[i][j].is_mine
        
    def __getitem__(self, index):
        i, j = index
        return self.grid[i][j]
    
    def __str__(self):
        string = ""
        for i in range(self.height):
            for j in range(self.width - 1):
                string += str(self.grid[i][j]) + " "
            string += str(self.grid[i][-1]) + "\n"
        return string


if __name__ == "__main__":
    WIDTH = 9
    HEIGHT = 9
    nbrMines = 10 
    field = Minefield(HEIGHT, WIDTH, nbrMines)
    print(field)
