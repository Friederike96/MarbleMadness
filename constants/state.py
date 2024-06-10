import pygame
from pgzero.actor import Actor
from pgzero.loaders import SoundLoader
from pgzero.screen import Screen
from pygame import image, mask
from pygame.joystick import Joystick

import constants.game_constants as game_constants
from enumerations.button import Button
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState

# game states
game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE
game_over_state: GameOverState = GameOverState.UNKNOWN
selected_button: Button = Button.PLAY

map3d = None
map_mask = None

steep_map: Actor = None
steep_map_mask: mask = None

finish_map: Actor = None
finish_mask: mask = None

gravity = 0.1
friction = 0.02

screen: Screen = None

start_game: bool = True

# Joystick
joystick: Joystick = None
DEAD_ZONE = 0.1

# current map and heightmap, set in load_level_files
current_map: str = ''
current_heightmap: str = ''

# heightmap image
heightmap: image = None

# position of map and heightmap, depends on level
current_map_position: set = ()

# marble
marble: Actor = Actor(image=game_constants.marble_still_frames[0])
marbleh: Actor = Actor(image=game_constants.marble_still_frames[0])
marble.dir = marble.speed = 0
marble.acceleration = 0
marble_moved_once: bool = False

# marble animation
marble_animation_counter = 0
marble_animation_interval = 6
marble_frame = 0
current_direction = 'still'

# coin
coin: Actor = Actor(image=game_constants.coin_images[0])
coin_frame = 0
coin_animation_counter = 0
coin_animation_interval = 10
coin_index = 0

# flag
flag = Actor(image=game_constants.flag_image)

# enemy
enemy = Actor(image=game_constants.enemy_image)
enemy.x = 130  # todo in constants
enemy.y = 170
enemy.angle = 0
enemy_speed = 1
enemy_index = 0

# sounds
sounds = SoundLoader('music/sounds')

# timer
timer: int = 0
previous_timer_value: int = 0

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
