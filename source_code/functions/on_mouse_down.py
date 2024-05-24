from pgzero.builtins import mouse

from source_code.constants import state
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState
from source_code.functions.helper_functions.load_level_files import load_level_files


def on_mouse_down(pos, button):
    # print(button)
    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if state.game_state == GameState.MENU_PAGE and state.quit_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.START_PAGE
        state.score = 0

    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif state.game_state == GameState.MENU_PAGE and state.start_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.LEVEL_GAME

    elif state.game_state == GameState.LEVEL_WIN and state.play_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.LEVEL_GAME
        load_level_files()

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
