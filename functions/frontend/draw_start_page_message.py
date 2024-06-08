from constants import state, game_constants
from enumerations.color import Color
from enumerations.font_size import FontSize
from functions.frontend.get_font import get_monospaced_font


def draw_start_page_message():
    state.screen.draw.text(
        text="Press ENTER button!",
        center=(game_constants.center_position_width, game_constants.center_position_height),
        color=Color.WHITE.value,
        fontname=get_monospaced_font(),
        fontsize=FontSize.LARGE.value
    )