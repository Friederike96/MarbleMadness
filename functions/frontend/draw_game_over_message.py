from constants import state, game_constants
from enumerations.color import Color
from enumerations.font_size import FontSize
from enumerations.game_over_state import GameOverState
from functions.frontend.calculate_text_size import calculate_text_size
from functions.frontend.get_font import get_monospaced_font


def draw_game_over_message():
    if state.blue_text:
        text_color = Color.BLUE.value
    else:
        text_color = Color.ORANGE.value

    if state.game_over_state == GameOverState.TIMER_UP:
        draw_given_game_over_message(
            text='Timer is up !',
            text_color=text_color
        )

    elif state.game_over_state == GameOverState.FALL_OVER_EDGE:
        draw_given_game_over_message(
            text='Oops, you fell over the edge !',
            text_color=text_color
        )

    elif state.game_over_state == GameOverState.ENEMY_HIT:
        draw_given_game_over_message(
            text='You hit the enemy !',
            text_color=text_color
        )


def draw_given_game_over_message(text: str, text_color: tuple):
    size = FontSize.MEDIUM.value
    text_width, text_height = calculate_text_size(text=text, size=size)

    text_position_width = game_constants.center_position_width - (text_width / 2)

    state.screen.draw.text(
        text=text,
        pos=(text_position_width, game_constants.center_position_height-100),  # todo: use constant
        color=text_color,
        fontname=get_monospaced_font(),
        fontsize=size,
        background='grey',
        align='center'
    )
