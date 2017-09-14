import random


class Field:
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
            row = [0] * self.width
            self.grid.append(row)

    def _add_mines_to_grid(self):
        mines = self.mines
        while mines > 0:
            mine_x = random.randrange(self.width)
            mine_y = random.randrange(self.height)
            if self.grid[mine_y][mine_x] != "x":
                self.grid[mine_y][mine_x] = "x"
                self._update_hints(mine_x, mine_y)
            else:
                continue
            mines -= 1

    def _update_hints(self, mine_x, mine_y):
        min_x = mine_x - 1 if mine_x > 0 else 0
        max_x = mine_x + 1 if mine_x < self.width - 1 else self.width - 1
        min_y = mine_y - 1 if mine_y > 0 else 0
        max_y = mine_y + 1 if mine_y < self.height - 1 else self.height - 1

        for i in range(min_y, max_y + 1):
            for j in range(min_x, max_x + 1):
                if (i != mine_y or j != mine_x) and self.grid[i][j] != "x":
                    self.grid[i][j] += 1

    def has_mine_at_position(self, i, j):
        return self.grid[i][j] == "x"
        
    def __getitem__(self, index):
        i, j = index
        return self.grid[i][j]
    
    def __setitem__(self, index, value):
        i, j = index
        self.grid[i][j] = value
        
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
    field = Field(HEIGHT, WIDTH, nbrMines)
    print(field)
