import os

import pygame.font
from pygame.font import Font

from source_code.constants import gui_constants, game_constants


def get_monospaced_font() -> str:
    return os.path.join(game_constants.base_path, f'fonts\\{gui_constants.marble_madness}.ttf')
