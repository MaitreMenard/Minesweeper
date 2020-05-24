from chronograph import Chronograph
from domain.difficulty import Difficulty
from infra.txt_statistics_dao import TxtStatisticsDao
from minefield import Minefield
from view.header import Header
from view.main_window import MainWindow
from view.menu import Menu
from view.options_window import OptionsWindow
from view.statistics_window import StatisticsWindow
from view.tile_button import ButtonState
from view.tile_grid import TileGrid


class Minesweeper:

    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.nbrMines = mines
        self.current_difficulty = Difficulty.EASY

        self.minesLeft = mines
        self.tiles_to_reveal = 0
        self.running = False
        self.win = False

        self.minefield = None
        self.chronograph = Chronograph(autostart=False)
        self.stats_dao = TxtStatisticsDao()
        self.stats = self.stats_dao.load()

        self.root = MainWindow()
        self.menu = Menu(self.root, self.new_game, self.on_statistics_window_opened, self.on_options_window_opened,
                         self.exit)
        self.header = Header(self.root, self.new_game)
        self.tile_grid = None

        self.new_game()
        self.root.mainloop()

    def new_game(self):
        self.running = True
        self.win = False
        self.stats.increment_games_started(self.current_difficulty)
        self.stats_dao.save(self.stats)
        self.minefield = Minefield(self.height, self.width, self.nbrMines)
        self.minesLeft = self.nbrMines
        self.header.set_mines_left(self.minesLeft)
        self.header.set_smiley_face()
        self.tiles_to_reveal = self.width * self.height

        if self.tile_grid is not None:
            self.tile_grid.destroy()
        self.tile_grid = TileGrid(self.root, self.minefield, self.on_tile_button_left_click,
                                  self.on_tile_button_right_click, self.on_label_left_click)

        self.header.set_time(0)
        self.chronograph.reset(autostop=True)
        self.root.after(1, self.update)

    def update(self):
        if self.running:
            time = int(self.chronograph.get())
            if not self.win:
                self.header.set_time(time)
                self.root.after(1, self.update)
            else:
                self.header.set_sunglasses_face()
                if time < self.stats.get_best_time(self.current_difficulty):
                    self.stats.set_best_time(self.current_difficulty, time)
                self.stats.increment_games_won(self.current_difficulty)
                self.stats_dao.save(self.stats)

    def on_statistics_window_opened(self):
        StatisticsWindow(self.root, self.stats)

    def on_options_window_opened(self):
        OptionsWindow(self.root)

    def on_tile_button_left_click(self, row, column):
        self.chronograph.resume()

        self.minefield[row, column].revealed = True

        if self.minefield.has_mine_at_position(row, column):
            print("BOOM !!!!")
            self.chronograph.pause()
            self.running = False
            self.header.set_dead_face()
        elif self.minefield[row, column].adjacent_mines == 0:
            self.for_each_surrounding_tiles(row, column, self.reveal_tile)
        self.tiles_to_reveal -= 1
        if self.tiles_to_reveal == self.nbrMines:
            self.chronograph.pause()
            self.win = True

    def for_each_surrounding_tiles(self, row, column, function):
        min_row = max(0, row - 1)
        max_row = min(self.height - 1, row + 1)
        min_column = max(0, column - 1)
        max_column = min(self.width - 1, column + 1)

        for i in range(min_row, max_row + 1):
            for j in range(min_column, max_column + 1):
                if i != row or j != column:
                    function(i, j)

    def reveal_tile(self, row, column):
        if not self.is_revealed(row, column):
            self.tile_grid.reveal_tile(row, column)

    def on_tile_button_right_click(self, row, column, button_state):
        if button_state == ButtonState.FLAGGED:
            self.minefield[row, column].flagged = True
            if self.minesLeft > 0:
                self.minesLeft -= 1
        elif button_state == ButtonState.QUESTION_MARK:
            self.minefield[row, column].flagged = False
            self.minesLeft += 1
        self.header.set_mines_left(self.minesLeft)

    def on_label_left_click(self, row, column):
        flags = 0

        min_row = max(0, row - 1)
        max_row = min(self.height - 1, row + 1)
        min_column = max(0, column - 1)
        max_column = min(self.width - 1, column + 1)

        for i in range(min_row, max_row + 1):
            for j in range(min_column, max_column + 1):
                if i != row or j != column:
                    if not self.is_revealed(i, j) and self.is_flagged(i, j):
                        flags += 1

        if flags == self.minefield[row, column].adjacent_mines:
            for i in range(min_row, max_row + 1):
                for j in range(min_column, max_column + 1):
                    if i != row or j != column:
                        if not self.is_revealed(i, j) and not self.is_flagged(i, j):
                            self.tile_grid.reveal_tile(i, j)

    def exit(self):
        self.root.quit()

    def is_revealed(self, i, j):
        return self.minefield[i, j].revealed

    def is_flagged(self, i, j):
        return self.minefield[i, j].flagged
