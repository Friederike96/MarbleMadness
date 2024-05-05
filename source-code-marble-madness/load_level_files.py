from pygame import image

import game_constants
import state
from level_state import LevelState


def load_level_files():
    match state.current_level:

        case LevelState.LEVEL_ONE:
            state.current_map = game_constants.level_one
            state.current_map_short = game_constants.level_one_short
            state.current_heightmap = game_constants.level_one_heightmap
            state.current_heightmap_short = game_constants.level_one_heightmap_short

            state.marble.dir = state.marble.speed = 0
            state.marble.x = game_constants.marble_position_level_one[0]
            state.marble.y = game_constants.marble_position_level_one[1]

            state.marbleh.x = game_constants.marbleh_position_level_one[0]
            state.marbleh.y = game_constants.marbleh_position_level_one[1]

            state.timer = game_constants.timer_level_one

            state.overlay_position = game_constants.overlay_position_level_one

        case LevelState.LEVEL_TWO:
            state.current_map = game_constants.level_two
            state.current_map_short = game_constants.level_two_short
            state.current_heightmap = game_constants.level_two_heightmap
            state.current_heightmap_short = game_constants.level_two_heightmap_short

            state.marble.dir = state.marble.speed = 0
            state.marble.x = game_constants.marble_position_level_two[0]
            state.marble.y = game_constants.marble_position_level_two[1]

            state.marbleh.x = game_constants.marbleh_position_level_two[0]
            state.marbleh.y = game_constants.marbleh_position_level_two[1]

            state.timer = game_constants.timer_level_two

            state.overlay_position = game_constants.overlay_position_level_two

        case LevelState.LEVEL_THREE:
            # TODO
            pass

        case LevelState.LEVEL_FOUR:
            # TODO
            pass

    state.heightmap = image.load(state.current_map)
