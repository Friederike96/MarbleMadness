from constants import state, game_constants
from enumerations.button import Button
from enumerations.color import Color
from enumerations.font_size import FontSize
from functions.frontend.get_font import get_monospaced_font


def draw_menu_buttons(text_button_one: str, text_button_two: str):
    arrow_pos = (game_constants.center_position_width - 120, game_constants.center_position_height - 25)
    play_button_color = Color.ORANGE.value
    quit_button_color = Color.WHITE.value

    if state.selected_button == Button.QUIT:
        arrow_pos = (game_constants.center_position_width - 120, game_constants.center_position_height + 25)
        quit_button_color = Color.ORANGE.value
        play_button_color = Color.WHITE.value

    state.screen.draw.text(  # todo: make function
        text=text_button_one,
        pos=(game_constants.center_position_width - 100, game_constants.center_position_height - 25),
        color=play_button_color,
        fontname=get_monospaced_font(),
        fontsize=FontSize.MEDIUM.value,
        background=Color.BLACK.value
    )
    state.screen.draw.text(
        text=text_button_two,
        pos=(game_constants.center_position_width - 100, game_constants.center_position_height + 25),
        color=quit_button_color,
        fontname=get_monospaced_font(),
        fontsize=FontSize.MEDIUM.value,
        background=Color.BLACK.value
    )
    state.screen.draw.text(
        text='>',
        pos=arrow_pos,
        color=Color.ORANGE.value,
        fontname=get_monospaced_font(),
        fontsize=FontSize.MEDIUM.value,
        background=Color.BLACK.value
    )
