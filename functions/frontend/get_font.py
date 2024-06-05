import os

from constants import gui_constants, game_constants


def get_monospaced_font() -> str:  # todo: can be in game_constants
    return os.path.join(game_constants.base_path, f'fonts/{gui_constants.marble_madness}.ttf')
