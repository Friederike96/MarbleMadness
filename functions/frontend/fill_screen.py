from typing import Any

from constants import state


def fill_screen_black():
    fill_screen_with_background(color=(0, 0, 0))


def fill_screen_with_background(color: Any):
    state.screen.fill(color=color)
