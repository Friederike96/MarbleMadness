from source_code.constants import game_constants, state
from source_code.functions.frontend.get_font import get_monospaced_font


def draw_menu_buttons(text_one: str, text_two: str):
    arrow_pos = (game_constants.center_position_width - 120, game_constants.center_position_height - 25)
    if state.quit_color == 'orange':
        arrow_pos = (game_constants.center_position_width - 120, game_constants.center_position_height + 25)

    state.screen.draw.text(
        text_one,
        (game_constants.center_position_width - 100, game_constants.center_position_height - 25),
        color=state.play_game_color,
        fontname=get_monospaced_font(),
        fontsize=20,
        background='black'
    )
    state.screen.draw.text(
        text_two,
        (game_constants.center_position_width - 100, game_constants.center_position_height + 25),
        color=state.quit_color,
        fontname=get_monospaced_font(),
        fontsize=20,
        background='black'
    )
    state.screen.draw.text(
        '>',
        arrow_pos,
        color='orange',
        fontname=get_monospaced_font(),
        fontsize=20,
        background='black'
    )
