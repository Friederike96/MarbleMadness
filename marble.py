# Marble Madness

import pgzrun
from pgzero.screen import Screen
from pygame import Surface

# state.py

from constants import state
from functions.draw import draw
from functions.backend.initialize_joystick import initialize_joystick
from functions.move_marble import move_marble
from functions.on_mouse_down import on_mouse_down
from functions.on_mouse_move import on_mouse_move
from functions.update import update

import sys
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

while True:
    draw()
    update()
    move_marble()
    on_mouse_move()  # should be in update
    on_mouse_down()  # should be in update
