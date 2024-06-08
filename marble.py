# Marble Madness

import sys

import pgzrun
from pgzero.screen import Screen
from pygame import Surface

from constants import state
from functions.draw import draw
from functions.initialize_joystick import initialize_joystick
from functions.process_input import process_input
from functions.update import update

# state.py
print(sys.path)

# do not delete, needed here
HEIGHT = 760
WIDTH = 900

# TODO: game loop einbauen
initialize_joystick()
surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
state.screen = pgzrun.mod.screen
pgzrun.go()

# while True:
#     process_input()
#     update()
#     draw()
