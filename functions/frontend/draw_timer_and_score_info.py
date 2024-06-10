from constants import state, game_constants
from enumerations.color import Color
from enumerations.font_size import FontSize
from functions.frontend.get_font import get_monospaced_font


def draw_timer_and_score_info(text_color_score: tuple = None, timer: int = None):
    draw_timer_info(timer=timer)
    draw_score_info(text_color_score=text_color_score)


def draw_timer_info(timer: int = None):
    timer_to_print = int(state.timer)
    if timer:
        timer_to_print = timer

    if timer_to_print < 10:
        timer_to_print = f'0{timer_to_print}'

    state.screen.draw.text(
        text=str(timer_to_print),
        pos=(game_constants.center_position_width - 10, 10),
        color=Color.BLUE.value,
        fontname=get_monospaced_font(),
        fontsize=20,
        background=Color.GREY.value,
        align='center'
    )


def draw_score_info(text_color_score: tuple = None):
    text_color = Color.BLUE.value
    if text_color_score:
        text_color = text_color_score

    state.screen.draw.text(
        'Score',
        (10, 10),
        color=Color.BLUE.value,
        fontname=get_monospaced_font(),
        fontsize=FontSize.SMALL.value,
        background=Color.GREY.value
    )
    state.screen.draw.text(
        str(state.score) + '',
        (10, 30),
        color=text_color,
        fontname=get_monospaced_font(),
        fontsize=FontSize.SMALL.value,
        background=Color.GREY.value
    )


def draw_bonus_score_info(text_color: tuple):
    state.screen.draw.text(
        text=f'Bonus for time left:  {state.display_timer_score}',
        pos=(10, 50),
        color=text_color,
        fontname=get_monospaced_font(),
        fontsize=FontSize.SMALL.value,
        background=Color.GREY.value
    )
    state.screen.draw.text(
        text=f'Bonus for coins:  {state.display_coin_score}',
        pos=(10, 70),
        color=text_color,
        fontname=get_monospaced_font(),
        fontsize=FontSize.SMALL.value,
        background=Color.GREY.value
    )
