from pgzero.actor import Actor
from pygame import image
import os

import source_code.constants.game_constants as game_constants
from source_code.enumerations.level_state import LevelState
from source_code.enumerations.game_state import GameState

game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE

# level images
current_map: str = ''
current_heightmap: str = ''

current_map_position: set = ()

heightmap: image = None

overlay_position: set = game_constants.overlay_position_level_one

# marble
marble: Actor = Actor(image=game_constants.marble_image, center=game_constants.marble_position_level_one)
marbleh: Actor = Actor(game_constants.marble_image, center=game_constants.marbleh_position_level_one)
marble.dir = marble.speed = 0

# coin
coin: Actor = Actor(game_constants.coin_image, center=game_constants.coin_position_level_one)

# timer and scores
timer: int = 0
score: int = 0
coin_score: int = 0

# debug mode
debug: bool = True

# button
start_button: Actor = Actor(
    image=game_constants.start_button_image,
    center=(game_constants.center_position_width, game_constants.start_button_pos_y)
)
quit_button: Actor = Actor(
    image=game_constants.quit_button_image,
    center=(game_constants.center_position_width, game_constants.quit_button_pos_y)
)
back_button: Actor = Actor(
    image=game_constants.back_button_image,
    center=(game_constants.center_position_width, game_constants.back_button_pos_y)
)
play_button: Actor = Actor(
    image=game_constants.play_button_image,
    center=(game_constants.center_position_width, game_constants.play_button_pos_y)
)
