from time import sleep

from constants import state
from enumerations.game_state import GameState
from enumerations.level_state import LevelState


def reset_state():
    state.wait_counter_for_game_over = 10
    state.score_for_current_level = 0
    state.deducted_score_for_lost_level = False
    state.previous_timer_value = 0
    state.marble_moved_once = False


def quit_game():
    reset_state()

    state.game_state = GameState.START_PAGE
    state.current_level = LevelState.LEVEL_ONE

    state.start_game = True

    state.blue_text = False
    state.wait_counter_for_score_display = 10

    state.not_added_points_and_incremented = True

    state.timer = 0
    state.score = 0
    state.coin_score = 0

    state.display_coin_score = 0
    state.display_timer_score = 0

    state.countdown_timer = 0

    sleep(0.2)
