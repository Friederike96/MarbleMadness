import pygame

from constants import state


def initialize_joystick():
    try:
        state.joystick = pygame.joystick.Joystick(0)
        state.joystick.init()
    except:
        print("No joystick")
