from constants import state, game_constants
from functions.frontend.get_font import get_monospaced_font


def draw_start_page_message():
    state.screen.draw.text(
        "Press ENTER button!",
        center=(game_constants.center_position_width, game_constants.center_position_height),
        color='white',
        fontname=get_monospaced_font(),
        fontsize=30
    )