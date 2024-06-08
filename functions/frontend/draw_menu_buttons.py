from constants import state, game_constants
from constants.gui_constants import FONTSIZES, COLORS
from functions.frontend.get_font import get_monospaced_font


def draw_menu_buttons(text_button_one: str, text_button_two: str):
    arrow_pos = (game_constants.center_position_width - 120, game_constants.center_position_height - 25)
    if state.quit_color == 'orange':
        arrow_pos = (game_constants.center_position_width - 120, game_constants.center_position_height + 25)

    state.screen.draw.text(  # todo: make function
        text=text_button_one,
        pos=(game_constants.center_position_width - 100, game_constants.center_position_height - 25),
        color=state.play_game_color,
        fontname=get_monospaced_font(),
        fontsize=FONTSIZES.MEDIUM.value,
        background=COLORS.BLACK.value
    )
    state.screen.draw.text(
        text=text_button_two,
        pos=(game_constants.center_position_width - 100, game_constants.center_position_height + 25),
        color=state.quit_color,
        fontname=get_monospaced_font(),
        fontsize=FONTSIZES.MEDIUM.value,
        background=COLORS.BLACK.value
    )
    state.screen.draw.text(
        text='>',
        pos=arrow_pos,
        color=COLORS.ORANGE.value,
        fontname=get_monospaced_font(),
        fontsize=FONTSIZES.MEDIUM.value,
        background=COLORS.BLACK.value
    )
