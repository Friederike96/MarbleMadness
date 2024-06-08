from pgzero.keyboard import keyboard

from constants import state
from enumerations.button import Button
from enumerations.game_state import GameState
from functions.backend.load_level_data import load_level_data


def handle_button_selection():
    from functions.update import quit_game
    if state.selected_button == Button.PLAY:
        if keyboard.down:
            state.selected_button = Button.QUIT

        elif keyboard.RETURN:
            state.game_state = GameState.COUNTDOWN
            load_level_data()

    elif state.selected_button == Button.QUIT:
        if keyboard.up:
            state.selected_button = Button.PLAY

        elif keyboard.RETURN:
            quit_game()
