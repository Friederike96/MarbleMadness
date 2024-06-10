import os
import pygame.image

from pygame import transform

# not used, defined in marble.py
HEIGHT = 760
WIDTH = 900

# center position
center_position_width = WIDTH/2
center_position_height = HEIGHT/2

level_data_path = 'data/level_data.json'
level_data_dict: dict

enemy_positions: list

coin_positions: list

# fonts
marble_madness = 'marble_madness'
courier_new = 'couriernew'



# todo: following also in json?
marble_image = 'objects/marble.png'

# todo: make state for marble rotation ?
marble_still_frames = [
    'marble/marble_still1'
]  # Add the still images if you have more
marble_right_frames = [
    'marble/marble_right1',
    'marble/marble_right2',
    'marble/marble_right3',
    'marble/marble_right4',
    'marble/marble_right5'
]
marble_bottom_right_frames = [
    'marble/marble_bottom_right1',
    'marble/marble_bottom_right2',
    'marble/marble_bottom_right3',
    'marble/marble_bottom_right4',
    'marble/marble_bottom_right5',
    'marble/marble_bottom_right6',
    'marble/marble_bottom_right7'
]
marble_bottom_frames = [
    'marble/marble_bottom1',
    'marble/marble_bottom2',
    'marble/marble_bottom3',
    'marble/marble_bottom4',
    'marble/marble_bottom5'
]
marble_bottom_left_frames = [
    'marble/marble_bottom_left1',
    'marble/marble_bottom_left2',
    'marble/marble_bottom_left3',
    'marble/marble_bottom_left4',
    'marble/marble_bottom_left5',
    'marble/marble_bottom_left6',
    'marble/marble_bottom_left7'
]
marble_left_frames = [
    'marble/marble_left1',
    'marble/marble_left2',
    'marble/marble_left3',
    'marble/marble_left4',
    'marble/marble_left5'
]

coin_images = [
    'coin/coinpos1.png',
    'coin/coinpos2.png',
    'coin/coinpos3.png',
    'coin/coinpos4.png'
]

flag_image = 'flag/blueflag.png'
enemy_image = 'enemy/shurikensml.png'

# enemy positions
enemy_positions = [(200, 130), (250, 160), (180, 200), (130, 170)]

# Marble Madness logo
LOGO_OFFSET_HEIGHT = 300
LOGO_OFFSET_WEIGHT = 150
mm_logo = os.path.join(base_path, 'images', 'objects', 'mm-logo.png')
mm_logo = transform.scale(pygame.image.load(mm_logo), (300, 156))

# Heightmap Marble Radius
HEIGHTMAP_OFFSET = 2
# Zahl Null
ZERO = 0
# für move_marble
GRAVITY = 0.03
MAX_HEIGHTMAP_VALUE = 255
HEIGHTMAP_VERTICAL_SCALE = 1.25

# level zero
level_zero = os.path.join(base_path, "images", "level_0", "level_0.png")
level_zero_heightmap = os.path.join(base_path, "images", "level_0", "level_0_heightmap.png")
level_zero_map_position = (0, 0)

marble_position_level_zero = (360, 30)
marbleh_position_level_zero = (360, 30)

timer_level_zero = 60

# level one
level_one = 'level_1/map.png'
level_one_heightmap = os.path.join(base_path, "images", "level_1", "heightmap.png")
level_one_map_position = (50, 0)

marble_position_level_one = (450, 45)
marbleh_position_level_one = (450, 60)

flag_position_level_one = (0, 0)

coin_position_level_one = (250, 45)

timer_level_one = 30

# wird alles auskommentiert weil nicht weiß ob mans braucht - alte Map von Friederike
# level two
# level_two = 'level_2/map.png'
# level_two_heightmap = 'images/level_2/heightmap_skaliert.png'
# level_two_map_position = (0, 0)
# marble_position_level_two = (500, 45)
# marbleh_position_level_two = (500, 60)
# overlay_position_level_two = (365, 150)
# coin_position_level_two = (150, 45)
# timer_level_two = 40

# level two von Nour und Serkay
level_two = os.path.join(base_path, "images", "level_3", "level_keasev2.png")
level_two_heightmap = os.path.join(base_path, "images", "level_3", "level_kease_heightmap.png")
level_two_map_position = (0, 0)

marble_position_level_two = (400, 30)
marbleh_position_level_two = (400, 30)
overlay_position_level_two = (0, 0)
timer_level_two = 40

# menu
center_position_width = WIDTH/2
center_position_height = HEIGHT/2

enter_button_pos_y = center_position_height

start_button_image = 'buttons/btn_start'
start_button_pos_y = 300

quit_button_image = 'buttons/btn_quit'
quit_button_pos_y = 400

back_button_image = 'buttons/btn_back'
back_button_pos_y = 400

play_button_image = 'buttons/btn_play'
play_button_pos_y = 400
