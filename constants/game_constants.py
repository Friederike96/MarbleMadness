import os

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

# menu
center_position_width = WIDTH / 2
center_position_height = HEIGHT / 2

enter_button_pos_y = center_position_height

start_button_image = 'buttons/btn_start'
start_button_pos_y = 300

quit_button_image = 'buttons/btn_quit'
quit_button_pos_y = 400

back_button_image = 'buttons/btn_back'
back_button_pos_y = 400

play_button_image = 'buttons/btn_play'
play_button_pos_y = 400
