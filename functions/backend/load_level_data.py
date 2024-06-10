import json
import os.path
from pgzero.actor import Actor

import constants.game_constants as game_constants
import constants.state as state
from enumerations.level_state import LevelState
from pygame import image, mask


def load_level_data():
    level = state.current_level.value
    data_dict = game_constants.level_data_dict

    state.current_map = data_dict[level]['map']
    state.current_heightmap = data_dict[level]['heightmap']
    state.current_map_position = data_dict[level]['map_position']

    state.map3d = Actor(data_dict[level]['map3d_short'], topleft=state.current_map_position)
    map_image = image.load(data_dict[level]['map3d'])
    state.map_mask = mask.from_surface(map_image)

    state.steep_map = Actor(data_dict[level]['mapslide_short'], topleft=state.current_map_position)
    steep_map_image = image.load(data_dict[level]['mapslide'])
    state.steep_map_mask = mask.from_surface(steep_map_image)

    state.finish_map = Actor(data_dict[level]['mapfinish_short'], topleft=state.current_map_position)
    finish_map_image = image.load(data_dict[level]['mapfinish'])
    state.finish_mask = mask.from_surface(finish_map_image)

    state.timer = data_dict[level]['timer']
    state.countdown_timer = state.timer

    state.marble.dir = state.marble.speed = 0
    state.marble.pos = data_dict[level]['marble_position']
    state.marbleh.pos = data_dict[level]['marbleh_position']

    if data_dict[level]['flag_position']:
        state.flag.pos = data_dict[level]['flag_position']
    else:
        state.flag = None

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
