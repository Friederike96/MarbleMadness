from pgzero.actor import Actor
from pgzero.screen import Screen
from pygame import image
import os

import source_code.constants.game_constants as game_constants
from source_code.enumerations.level_state import LevelState
from source_code.enumerations.game_state import GameState

game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE

screen: Screen = None

# level images
current_map: str = ''
current_heightmap: str = ''

current_map_position: set = ()

heightmap: image = None

overlay_position: set = game_constants.overlay_position_level_one

marble_start_pos_x: int = 0
marble_start_pos_y: int = 0
marbleh_start_pos_x: int = 0
marbleh_start_pos_y: int = 0

# marble
marble: Actor = Actor(image=game_constants.marble_image, center=(450, 45))
marbleh: Actor = Actor(image=game_constants.marble_image, midtop=game_constants.marbleh_position_level_one)
marble.dir = marble.speed = 0

# coin
coin: Actor = Actor(image=game_constants.coin_image, center=game_constants.coin_position_level_one)
start_marble: Actor = Actor(image=game_constants.coin_image, center=(450, 45))

# timer and scores
start_timer = False
not_added_points_and_incremented = True

timer: int = 0
score: int = 0
coin_score: int = 0

display_timer_score: int = 0
display_coin_score: int = 0

# debug mode
debug: bool = False

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
