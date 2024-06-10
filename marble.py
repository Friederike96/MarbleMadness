# Marble Madness

import pgzrun
from pgzero.screen import Screen
from pygame import Surface

from constants import state
from functions.backend.load_json_data import load_json_data
from functions.draw import draw
from functions.initialize_joystick import initialize_joystick
from functions.process_input import process_input
from functions.update import update

# do not delete, needed here
HEIGHT = 760
WIDTH = 900

# TODO: game loop einbauen
initialize_joystick()
load_json_data()

surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
state.screen = pgzrun.mod.screen
pgzrun.go()

# while True:
#     process_input()
#     update()
#     draw()
