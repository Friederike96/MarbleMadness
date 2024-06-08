from typing import Any

from constants import state
from enumerations.color import Color


def fill_screen_black():
    fill_screen_with_background(color=Color.BLACK.value)


def fill_screen_with_background(color: Any):
    state.screen.fill(color=color)


def fill_screen_with_map():
    state.screen.blit(state.current_map, state.current_map_position)
