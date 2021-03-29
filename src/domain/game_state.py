class GameState:

    def __init__(self, tiles_total: int, mines_total: int):
        self.game_started = False
        self.tiles_to_reveal = tiles_total
        self.mines_total = mines_total
        self.mines_left = mines_total

    def is_game_started(self):
        return self.game_started

    def is_game_won(self):
        return self.tiles_to_reveal == self.mines_total

    def reveal_tile(self):
        self.game_started = True
        if self.tiles_to_reveal > 0:
            self.tiles_to_reveal -= 1

    def flag_tile(self):
        self.game_started = True
        if self.mines_left > 0:
            self.mines_left -= 1

    def unflag_tile(self):
        if self.mines_left < self.mines_total:
            self.mines_left += 1

    def get_mines_left(self):
        return self.mines_left
