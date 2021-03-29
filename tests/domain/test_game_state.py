from unittest import TestCase

from src.domain.game_state import GameState


class GameStateTest(TestCase):

    MINES_TOTAL = 5
    TILES_TOTAL = 10
    TILES_TO_REVEAL = TILES_TOTAL - MINES_TOTAL

    def setUp(self):
        self.game_state = GameState(self.TILES_TOTAL, self.MINES_TOTAL)

    def test_game_is_not_started_initially(self):
        is_started = self.game_state.is_game_started()

        self.assertFalse(is_started)

    def test_game_is_started_after_revealing_first_tile(self):
        self.game_state.reveal_tile()

        is_started = self.game_state.is_game_started()

        self.assertTrue(is_started)

    def test_game_is_started_after_first_tile_flagged(self):
        self.game_state.flag_tile()

        is_started = self.game_state.is_game_started()

        self.assertTrue(is_started)

    def test_flag_tile_should_decrease_mines_left(self):
        initial_mines_left = self.game_state.get_mines_left()

        self.game_state.flag_tile()

        self.assertEqual(self.game_state.get_mines_left(), initial_mines_left - 1)

    def test_flag_tile_should_not_decrease_mines_left_below_zero(self):
        for _ in range(self.MINES_TOTAL + 1):
            self.game_state.flag_tile()

        self.assertEqual(self.game_state.get_mines_left(), 0)

    def test_unflag_tile_should_increase_mines_left(self):
        self.game_state.flag_tile()
        initial_mines_left = self.game_state.get_mines_left()

        self.game_state.unflag_tile()

        self.assertEqual(self.game_state.get_mines_left(), initial_mines_left + 1)

    def test_unflag_tile_should_not_increase_mines_left_above_mines_total(self):
        initial_mines_left = self.game_state.get_mines_left()

        self.game_state.unflag_tile()

        self.assertEqual(self.game_state.get_mines_left(), initial_mines_left)

    def test_game_is_not_won_initially(self):
        game_won = self.game_state.is_game_won()

        self.assertFalse(game_won)

    def test_game_is_not_won_while_there_are_tiles_to_reveal(self):
        for _ in range(self.TILES_TO_REVEAL - 1):
            self.game_state.reveal_tile()

        game_won = self.game_state.is_game_won()

        self.assertFalse(game_won)

    def test_game_is_won_when_all_tiles_are_revealed(self):
        for _ in range(self.TILES_TO_REVEAL):
            self.game_state.reveal_tile()

        game_won = self.game_state.is_game_won()

        self.assertTrue(game_won)
