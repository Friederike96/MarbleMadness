from source_code.constants import game_constants, state
from source_code.enumerations.game_state import GameState


def on_mouse_move(pos, rel, buttons):
    if state.game_state == GameState.MENU_PAGE:
        if game_constants.center_position_width - 50 < pos[0] < game_constants.center_position_width + 50 \
                and game_constants.center_position_height < pos[1] < game_constants.center_position_height +20:
            state.play_game_color = 'orange'
            state.quit_color = 'white'
        elif game_constants.center_position_width + 50 < pos[0] < game_constants.center_position_width + 150 \
            and game_constants.center_position_height < pos[1] < game_constants.center_position_height +20:
            state.quit_color = 'orange'
            state.play_game_color = 'white'
