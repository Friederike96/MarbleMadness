import os

from constants import game_constants


def get_monospaced_font() -> str:  # todo: can be in game_constants
    return os.path.join(os.getcwd(), f'fonts/{game_constants.marble_madness}.ttf')
