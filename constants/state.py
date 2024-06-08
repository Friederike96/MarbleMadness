import pygame
from pgzero.actor import Actor
from pgzero.loaders import SoundLoader
from pgzero.screen import Screen
from pygame import image
from pygame.joystick import Joystick

import constants.game_constants as game_constants
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState

# game states
game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE
game_over_state: GameOverState = GameOverState.UNKNOWN

screen: Screen = None

start_game: bool = True

# Joystick
joystick: Joystick = None

# Buttons
# TODO

play_game_color: str = 'orange'  # todo: make bool
quit_color: str = 'white'

# current map and heightmap, set in load_level_files
current_map: str = ''
current_heightmap: str = ''

# heightmap image
heightmap: image = None

# position of map and heightmap, depends on level
current_map_position: set = ()

# position of flag
flag_position: set = game_constants.flag_position_level_one

# marble
marble: Actor = Actor(image=game_constants.marble_still_frames[0], center=game_constants.marble_position_level_one)
marbleh: Actor = Actor(image=game_constants.marble_still_frames[0], center=game_constants.marbleh_position_level_one)
marble.dir = marble.speed = 0
marble_moved_once: bool = False

# marble animation
marble_animation_counter = 0
marble_animation_interval = 6
marble_frame = 0
current_direction = 'still'

# coin
coin: Actor = Actor(image=game_constants.coin_images[0], center=game_constants.coin_position_level_one)
coin_frame = 0
coin_animation_counter = 0
coin_animation_interval = 10

# flag
flag = Actor(image=game_constants.flag_image)
flag.x = 248  # todo in constants
flag.y = 500

# enemy
enemy = Actor(image=game_constants.enemy_image)
enemy.x = 130  # todo in constants
enemy.y = 170
enemy_speed = 1
enemy_angle = 0
enemy_index = 0

# sounds
sounds = SoundLoader('music/sounds')

# timer
timer: int = 0
start_timer = False
previous_clock_time: int = 0

# scores
score: int = 0
coin_score: int = 0
not_added_points_and_incremented = True

# needed for displaying countdown
printed_timer: bool = False
countdown_timer: int = 0

# needed for displaying score when won level
display_timer_score: int = 0
display_coin_score: int = 0

# needed to deduct points when lost level
score_for_current_level = 0
deducted_score_for_lost_level: bool = False

# needed for determine which color to use when blinking (level won or game over message)
blue_text: bool = False

# needed for displaying blinking score when won level
wait_counter_for_score_display: int = 10

# needed for displaying blinking game over message when lost level
wait_counter_for_game_over: int = 10

# debug mode
debug: bool = False
