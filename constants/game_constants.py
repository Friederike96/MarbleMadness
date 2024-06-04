
import os

# not used, defined in marble.py
HEIGHT = 760
WIDTH = 900

base_path = os.getcwd()

marble_image = 'objects/marble.png'

#marble_still_frames = ['marble_still1']  # Add the still images if you have more
marble_right_frames = ['marble_right1', 'marble_right2', 'marble_right3', 'marble_right4', 'marble_right5']
marble_bottom_right_frames = ['marble_bottom_right1', 'marble_bottom_right2', 'marble_bottom_right3', 'marble_bottom_right4', 'marble_bottom_right5', 'marble_bottom_right6', 'marble_bottom_right7']
marble_bottom_frames = ['marble_bottom1', 'marble_bottom2', 'marble_bottom3', 'marble_bottom4', 'marble_bottom5']
marble_bottom_left_frames = ['marble_bottom_left1', 'marble_bottom_left2', 'marble_bottom_left3', 'marble_bottom_left4', 'marble_bottom_left5', 'marble_bottom_left6', 'marble_bottom_left7']
marble_left_frames = ['marble_left1', 'marble_left2', 'marble_left3', 'marble_left4', 'marble_left5']


coin_images = ['coin/coinpos1.png', 'coinpos2', 'coinpos3', 'coinpos4']
overlay_image = 'objects/overlay.png'

# enemy positions
enemy_positions = [(200, 130), (250, 160), (180, 200), (130, 170)]

# level one
level_one = 'level_1/map.png'
level_one_heightmap ='images/level_1/heightmap.png'
level_one_map_position = (50, 0)

marble_position_level_one = (450, 45)
marbleh_position_level_one = (450, 60)

flag_position_level_one = (0, 0)

coin_position_level_one = (250, 45)

timer_level_one = 30

# level two
level_two = 'level_2/map.png'
level_two_heightmap = 'images/level_2/heightmap_skaliert.png'
level_two_map_position = (0, 0)

marble_position_level_two = (550, 45)
marbleh_position_level_two = (550, 60)

flag_position_level_two = (365, 150)

coin_position_level_two = (150, 45)

timer_level_two = 40

# menu
center_position_width = WIDTH/2
center_position_height = HEIGHT/2

enter_button_pos_y = center_position_height

start_button_image = 'buttons/btn_start'
start_button_pos_y = 300

quit_button_image ='buttons/btn_quit'
quit_button_pos_y = 400

back_button_image = 'buttons/btn_back'
back_button_pos_y = 400

play_button_image = 'buttons/btn_play'
play_button_pos_y = 400
