from constants import state, game_constants
from functions.frontend.get_font import get_monospaced_font


def draw_countdown_message():
    state.screen.draw.text(
        "TIME TO FINISH RACE:",
        center=(game_constants.center_position_width, game_constants.center_position_height - 30),
        color='orange',
        fontname=get_monospaced_font(),
        fontsize=40,
        background='black'
    )
    state.screen.draw.text(
        f'{int(state.countdown_timer)}',
        center=(game_constants.center_position_width, game_constants.center_position_height + 30),
        color='blue',
        fontname=get_monospaced_font(),
        fontsize=60,
        background='black'
    )
    timer_to_print = (int(state.timer) - int(state.countdown_timer))
    if timer_to_print < 10:
        timer_to_print = f'0{timer_to_print}'

    state.screen.draw.text(
        f'{timer_to_print}',
        (game_constants.center_position_width - 10, 10),
        color=(0, 0, 139),
        fontname=get_monospaced_font(),
        fontsize=20,
        background='grey',
        align='center'
    )
    state.screen.draw.text(
        'Score',
        (10, 10),
        color=(0, 0, 139),
        fontname=get_monospaced_font(),
        fontsize=15,
        background='grey'
    )
    state.screen.draw.text(
        str(int(state.score)) + '',
        (10, 30),
        color=(0, 0, 139),
        fontname=get_monospaced_font(),
        fontsize=15,
        background='grey'
    )
