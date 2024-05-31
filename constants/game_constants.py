
import os

HEIGHT = 760
WIDTH = 900

base_path = os.getcwd()

marble_image = 'objects/marble.png'
coin_image = 'objects/coingold.png'
overlay_image = 'objects/overlay.png'

# level one
level_one = 'level_1/map.png'
level_one_heightmap ='images/level_1/heightmap.png'
level_one_map_position = (50, 0)

marble_position_level_one = (450, 45)
marbleh_position_level_one = (450, 60)

overlay_position_level_one = (0, 0)

coin_position_level_one = (250, 45)

timer_level_one = 30

# level two
level_two = 'level_2/map.png'
level_two_heightmap = 'images/level_2/heightmap_skaliert.png'
level_two_map_position = (0, 0)

marble_position_level_two = (500, 45)
marbleh_position_level_two = (500, 60)

overlay_position_level_two = (365, 150)

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
