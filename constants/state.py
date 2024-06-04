import pygame
from pgzero.actor import Actor
from pgzero.screen import Screen
from pygame import image
from pygame.joystick import Joystick

import constants.game_constants as game_constants
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState

game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE
game_over_state: GameOverState = GameOverState.UNKNOWN

screen: Screen = None

start_game: bool = True

# Joystick
joystick: Joystick = None

# new buttons
play_game_color: str = 'orange'
quit_color: str = 'white'

# level images
current_map: str = ''
current_heightmap: str = ''

current_map_position: set = ()

heightmap: image = None

overlay_position: set = game_constants.overlay_position_level_one

# marble
marble: Actor = Actor(image=game_constants.marble_image, center=game_constants.marble_position_level_one)
marbleh: Actor = Actor(image=game_constants.marble_image, center=game_constants.marbleh_position_level_one)
marble.dir = marble.speed = 0
marble_moved_once: bool = False

# coin
coin: Actor = Actor(image=game_constants.coin_image, center=game_constants.coin_position_level_one)

# timer and scores
previous_clock_time: int = 0

colorful: bool = False
wait_counter_for_score_display: int = 10
wait_counter_for_game_over: int = 10

start_timer = False
not_added_points_and_incremented = True

timer: int = 0
level_timer = 0
score: int = 0
coin_score: int = 0

score_for_current_level = 0
deducted_score_for_lost_level: bool = False

display_timer_score: int = 0
display_coin_score: int = 0

printed_timer: bool = False
countdown_timer: int = 0

# debug mode
debug: bool = False
