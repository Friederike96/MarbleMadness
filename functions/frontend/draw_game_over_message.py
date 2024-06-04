from constants import state, game_constants
from enumerations.game_over_state import GameOverState
from functions.frontend.get_font import get_monospaced_font


def draw_game_over_message():
    if state.colorful:
        text_color = (0, 0, 139)
    else:
        text_color = 'orange'

    state.colorful = not state.colorful
    if state.game_over_state == GameOverState.TIMER_UP:
        state.screen.draw.text(
            'Timer is up !',
            (game_constants.center_position_width - 200, game_constants.center_position_height-50),
            color=text_color,
            fontname=get_monospaced_font(),
            fontsize=30,
            background='grey'
        )

    elif state.game_over_state == GameOverState.FALL_OVER_EDGE:
        state.screen.draw.text(
            'Oops, you fell over the edge !',
            (game_constants.center_position_width - 300, game_constants.center_position_height-50),
            color=text_color,
            fontname=get_monospaced_font(),
            fontsize=20,
            background='grey'
        )

    elif state.game_over_state == GameOverState.ENEMY_HIT:
        state.screen.draw.text(
            'You hit the enemy !',
            (game_constants.center_position_width - 200, game_constants.center_position_height-50),
            color=text_color,
            fontname=get_monospaced_font(),
            fontsize=20,
            background='grey'
        )