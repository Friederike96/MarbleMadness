# HEIGHT = 570
# WIDTH = 600
import os

HEIGHT = 760
WIDTH = 904

base_path = os.getcwd()

marble_image = os.path.join(base_path, 'images\\objects\\marble')
coin_image = os.path.join(base_path, 'images\\objects\\coingold')
overlay_image = os.path.join(base_path, 'images\\objects\\overlay')

# level one
level_one = os.path.join(base_path, 'images\\level_1\\map.png')
level_one_heightmap = os.path.join(base_path, 'images\\level_1\\heightmap')

marble_position_level_one = (300, 45)
marbleh_position_level_one = (300, 60)

overlay_position_level_one = (0, 0)

coin_position_level_one = (150, 45)

timer_level_one = 30

# level two
level_two = os.path.join(base_path, 'images\\level_2\\map.png')
level_two_heightmap = os.path.join(base_path, 'images\\level_2\\heightmap_skaliert.png')

marble_position_level_two = (300, 45)
marbleh_position_level_two = (300, 60)

overlay_position_level_two = (365, 150)

coin_position_level_two = (150, 45)

timer_level_two = 30

# menu
start_button_image = os.path.join(base_path, 'images\\buttons\\btn_start')
start_button_position = (300, 300)

quit_button_image = os.path.join(base_path, 'images\\buttons\\btn_quit')
quit_button_position = (300, 400)

back_button_image = os.path.join(base_path, 'images\\buttons\\btn_back')
back_button_position = (300, 400)

play_button_image = os.path.join(base_path, 'images\\buttons\\btn_play')
