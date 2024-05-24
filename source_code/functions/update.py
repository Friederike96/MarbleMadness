import random

from pgzero.builtins import keyboard

from source_code.constants import state
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState
from source_code.functions.helper_functions.increment_level import increment_level
from source_code.functions.move_marble import move_marble


def update():
    if not state.start_timer and keyboard.left or keyboard.right or keyboard.up or keyboard.down:
        state.start_timer = True

    if state.game_state == GameState.LEVEL_GAME and state.start_timer:
        state.timer -= 1 / 60
        if state.timer <= 0:
            state.game_state = GameState.GAME_OVER

        else:
            if state.marble.colliderect(state.coin) and state.score != 2:
                state.coin.x = random.randint(150, 450)
                state.coin.y = random.randint(45, 500)
                state.score += 1  # todo: score abhängig von restlichem Timer?
                state.coin_score += 1

            if keyboard.left:
                state.marble.dir = max(state.marble.dir - 1, -1)
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.right:
                state.marble.dir = min(state.marble.dir + 1, 1)
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.up:
                state.marbleh.y -= 2
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.down:
                state.marbleh.y += 1.5
                state.marble.speed = min(1, state.marble.speed + 0.1)

            move_marble()
            state.marble.speed = max(0, state.marble.speed - 0.01)

    # damit man vom Startbildschirm ins Menü kommt
    elif state.game_state == GameState.START_PAGE and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE

    elif state.game_state == GameState.GAME_WIN and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE
        state.current_level = LevelState.LEVEL_ONE
        state.marble.pos = 300, 45  # todo: wanted like this? or position of level 1
        state.marbleh.pos = 300, 60

    elif state.game_state == GameState.LEVEL_WIN and state.not_added_points_and_incremented:
        add_timing_points()
        increment_level()
        state.not_added_points_and_incremented = False


def add_timing_points():
    timer_score = int(state.timer/3)
    state.score += timer_score
    state.display_timer_score = timer_score

    state.score += state.coin_score
    state.display_coin_score = state.coin_score
    state.coin_score = 0

    state.timer = 0
