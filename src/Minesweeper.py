from src.chronograph import Chronograph
from src.domain.difficulty import Difficulty, select_configuration
from src.domain.game_state import GameState
from src.infra.random_seed_generator import RandomSeedGenerator
from src.infra.txt_statistics_dao import TxtStatisticsDao
from src.minefield import Minefield
from src.view.button_factory import ButtonFactory
from src.view.header import Header
from src.view.main_window import MainWindow
from src.view.menu import Menu
from src.view.options_window import OptionsWindow
from src.view.statistics_window import StatisticsWindow
from src.view.tile_button import ButtonState
from src.view.tile_grid import TileGrid


class Minesweeper:
    SAVE_FILENAME = "src/data/stats.txt"

    def __init__(self, difficulty: Difficulty):
        self.width = 0
        self.height = 0
        self.current_difficulty = None

        self.running = False
        self.game_state = None

        self.seed_generator = RandomSeedGenerator()
        self.minefield = None
        self.chronograph = Chronograph(autostart=False)
        self.stats_dao = TxtStatisticsDao(self.SAVE_FILENAME)
        self.stats = self.stats_dao.load()

        self.root = MainWindow()
        self.menu = Menu(self.root, self.new_game, self.on_statistics_window_opened, self.on_options_window_opened,
                         self.exit)
        self.header = Header(self.root, self.restart)
        self.tile_grid = None

        self.button_factory = ButtonFactory(self.on_tile_button_left_click, self.on_tile_button_right_click)

        self.new_game(difficulty)
        self.root.mainloop()

    def restart(self):
        self.new_game(self.current_difficulty)

    def new_game(self, difficulty: Difficulty):
        self.current_difficulty = difficulty

        configuration = select_configuration(difficulty)
        self.width = configuration.width
        self.height = configuration.height

        self.running = True
        tiles_to_reveal = self.width * self.height
        self.game_state = GameState(tiles_to_reveal, configuration.mines)
        self.minefield = Minefield(self.height, self.width, configuration.mines, self.seed_generator.generate())
        self.header.set_mines_left(self.game_state.get_mines_left())
        self.header.set_smiley_face()

        if self.tile_grid is not None:
            self.tile_grid.destroy()
        self.tile_grid = TileGrid(self.root, self.minefield, self.button_factory, self.on_label_left_click)

        self.header.set_time(0)
        self.chronograph.reset(autostop=True)
        self.root.after(1, self.update)

    def update(self):
        if self.running:
            time = int(self.chronograph.get())

            if not self.game_state.is_game_won():
                self.header.set_time(time)
                self.root.after(1, self.update)
            else:
                self.chronograph.pause()
                self.header.set_sunglasses_face()
                if self.stats.is_best_time(self.current_difficulty, time):
                    self.stats.set_best_time(self.current_difficulty, time)
                self.stats.increment_games_won(self.current_difficulty)
                self.stats_dao.save(self.stats)

    def on_statistics_window_opened(self):
        StatisticsWindow(self.root, self.stats)

    def on_options_window_opened(self):
        OptionsWindow(self.root, self.reset_stats)

    def on_tile_button_left_click(self, row, column):
        if not self.game_state.is_game_started():
            self.start_game()

        self.minefield[row, column].revealed = True
        self.game_state.reveal_tile()
        self.tile_grid.reveal_tile(row, column)

        if self.minefield.has_mine_at_position(row, column):
            self.chronograph.pause()
            self.running = False
            self.header.set_dead_face()
        elif self.minefield[row, column].adjacent_mines == 0:
            self.reveal_surrounding_tiles(row, column)

    def start_game(self):
        self.stats.increment_games_started(self.current_difficulty)
        self.stats_dao.save(self.stats)
        self.chronograph.resume()

    def reveal_surrounding_tiles(self, row, column):
        min_row = max(0, row - 1)
        max_row = min(self.height - 1, row + 1)
        min_column = max(0, column - 1)
        max_column = min(self.width - 1, column + 1)

        for i in range(min_row, max_row + 1):
            for j in range(min_column, max_column + 1):
                if i != row or j != column:
                    if not self.is_revealed(i, j):
                        self.reveal_tile(i, j)

    def reveal_tile(self, row, column):
        self.minefield[row, column].revealed = True
        self.game_state.reveal_tile()
        self.tile_grid.reveal_tile(row, column)

        if self.minefield[row, column].adjacent_mines == 0:
            self.reveal_surrounding_tiles(row, column)

    def on_tile_button_right_click(self, row, column, button_state):
        if not self.game_state.is_game_started():
            self.start_game()

        if button_state == ButtonState.FLAGGED:
            self.minefield[row, column].flagged = True
            self.game_state.flag_tile()
        elif button_state == ButtonState.QUESTION_MARK:
            self.minefield[row, column].flagged = False
            self.game_state.unflag_tile()
        self.header.set_mines_left(self.game_state.get_mines_left())

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
                            self.reveal_tile(i, j)

    def exit(self):
        self.root.quit()

    def is_revealed(self, i, j):
        return self.minefield[i, j].revealed

    def is_flagged(self, i, j):
        return self.minefield[i, j].flagged

    def reset_stats(self):
        self.stats.reset()
        self.stats_dao.save(self.stats)
