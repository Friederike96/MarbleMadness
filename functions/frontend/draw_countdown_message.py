from constants import state, game_constants
from enumerations.color import Color
from enumerations.font_size import FontSize
from functions.frontend.draw_timer_and_score_info import draw_timer_and_score_info
from functions.frontend.get_font import get_monospaced_font


def draw_countdown_message():
    state.screen.draw.text(
        text="TIME TO FINISH RACE:",
        center=(game_constants.center_position_width, game_constants.center_position_height - 30),
        color=Color.ORANGE.value,
        fontname=get_monospaced_font(),
        fontsize=FontSize.LARGE.value,
        background=Color.BLACK.value,
        align='center'
    )

    countdown_timer_text = f'{int(state.countdown_timer)}'
    if state.countdown_timer < 10:
        countdown_timer_text = f'0{int(state.countdown_timer)}'

    state.screen.draw.text(
        text=countdown_timer_text,
        center=(game_constants.center_position_width, game_constants.center_position_height + 30),
        color=Color.BLUE.value,
        fontname=get_monospaced_font(),
        fontsize=FontSize.SUPER_LARGE.value,
        background=Color.BLACK.value,
        align='center'
    )

    timer = (int(state.timer) - int(state.countdown_timer))
    draw_timer_and_score_info(timer=timer)
