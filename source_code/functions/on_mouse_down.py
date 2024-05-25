from time import sleep

import pygame
from pgzero.builtins import mouse

from source_code.constants import state, game_constants
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState
from source_code.functions.backend.increment_level import increment_level
from source_code.functions.backend.load_level_files import load_level_files
from source_code.functions.frontend.get_font import get_monospaced_font


def on_mouse_down(pos, button):

    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if state.game_state == GameState.MENU_PAGE and state.quit_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.START_PAGE
        state.score = 0

    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif state.game_state == GameState.MENU_PAGE and state.start_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.COUNTDOWN
        state.countdown_timer = state.timer
        state.printed_timer = False

    elif state.game_state == GameState.LEVEL_WIN:
        if(
            game_constants.center_position_width-50 <= pos[0] <= game_constants.center_position_width+50
            and game_constants.center_position_height-10 <= pos[1] <= game_constants.center_position_height+10
        ):  # todo: make button colorful when hovering and clicking
            state.game_state = GameState.COUNTDOWN
            state.printed_timer = False
            #increment_level()
            load_level_files()
            print('blah')

    # wenn man im GameOver Bildschirm ist
    elif state.game_state == GameState.GAME_OVER:
        # todo: marble und marbleh in die Anfangsposition und Speed auf 0 setzen
    #    marble.pos = 300, 45
    #    marbleh.pos = 300, 60
        state.marble.speed = 0
        state.marbleh.speed = 0

        # wenn man im GameOver Bildschirm auf den Play Button drückt spielt man das Level erneut
        if state.play_button.collidepoint(pos):
            state.game_state = GameState.LEVEL_GAME

        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif state.quit_button.collidepoint(pos):
            state.game_state = GameState.START_PAGE
            state.current_level = LevelState.LEVEL_ONE
            load_level_files()
            state.score = 0
