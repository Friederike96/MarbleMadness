import json
import os.path

import constants.game_constants as game_constants
import constants.state as state
from enumerations.level_state import LevelState
from pygame import image


def load_level_data():
    level = state.current_level.value
    data_dict = game_constants.level_data_dict

    state.current_map = data_dict[level]['map']
    state.current_heightmap = data_dict[level]['heightmap']
    state.current_map_position = data_dict[level]['map_position']

    state.timer = data_dict[level]['timer']
    state.countdown_timer = state.timer

    state.marble.dir = state.marble.speed = 0
    state.marble.pos = data_dict[level]['marble_position']
    state.marbleh.pos = data_dict[level]['marbleh_position']

    state.flag.pos = data_dict[level]['flag_position']

    game_constants.enemy_positions = data_dict[level]['enemy_positions']
    if game_constants.enemy_positions:
        state.enemy.pos = game_constants.enemy_positions[state.enemy_index]
    else:
        state.enemy = None

    game_constants.coin_positions = data_dict[level]['coin_positions']
    if game_constants.coin_positions:
        state.coin.pos = game_constants.coin_positions[state.coin_index]
    else:
        state.coin = None


    # todo: general data, make function from this
    state.previous_timer_value = 0
    state.marble_moved_once = False

    state.heightmap = image.load(state.current_heightmap)
