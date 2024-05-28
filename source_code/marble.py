# Marble Madness

import pgzrun
import pygame
from pgzero.screen import Screen
from pygame import Surface

from source_code.constants import state
from source_code.functions import on_mouse_move
from source_code.functions.draw import draw
from source_code.functions.helper_functions.initialize_joystick import initialize_joystick
from source_code.functions.move_marble import move_marble
from source_code.functions.on_mouse_down import on_mouse_down
from source_code.functions.on_mouse_move import on_mouse_move
from source_code.functions.update import update

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
