import constants.game_constants as game_constants
import constants.state as state
from enumerations.level_state import LevelState
from pygame import image


def load_level_files():
    if state.current_level == LevelState.LEVEL_ONE:
        state.current_map = game_constants.level_one
        state.current_heightmap = game_constants.level_one_heightmap
        state.current_map_position = game_constants.level_one_map_position

        state.marble.dir = state.marble.speed = 0
        state.marble.pos = game_constants.marble_position_level_one
        state.marbleh.pos = game_constants.marbleh_position_level_one

        state.start_timer = False

        state.timer = game_constants.timer_level_one
        state.countdown_timer = int(state.timer)

        state.previous_clock_time = 0

        state.marble_moved_once = False

    elif state.current_level == LevelState.LEVEL_TWO:
        state.current_map = game_constants.level_two
        state.current_heightmap = game_constants.level_two_heightmap
        state.current_map_position = game_constants.level_two_map_position

        state.marble.dir = state.marble.speed = 0
        state.marble.pos = game_constants.marble_position_level_two
        state.marbleh.pos = game_constants.marbleh_position_level_two

        state.start_timer = False

        state.timer = game_constants.timer_level_two
        state.countdown_timer = state.timer

        state.previous_clock_time = 0
        state.marble_moved_once = False

    elif state.current_level == LevelState.LEVEL_THREE:
        # TODO
        pass

    elif state.current_level == LevelState.LEVEL_FOUR:
        # TODO
        pass

    state.heightmap = image.load(state.current_heightmap)
