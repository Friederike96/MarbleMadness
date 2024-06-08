from constants import state
from enumerations.color import Color
from enumerations.game_state import GameState
from functions.frontend.draw_countdown_message import draw_countdown_message
from functions.frontend.draw_game_over_message import draw_game_over_message
from functions.frontend.draw_menu_buttons import draw_menu_buttons
from functions.frontend.draw_start_page_message import draw_start_page_message
from functions.frontend.draw_timer_and_score_info import draw_timer_and_score_info, draw_bonus_score_info
from functions.frontend.fill_screen import fill_screen_black, fill_screen_with_map


def draw():
    # debug mode for using heightmap instead of map
    if state.debug:
        state.screen.blit(state.current_heightmap, state.current_map_position)
        state.marbleh.draw()
        return

    # regular mode
    if state.game_state == GameState.START_PAGE:
        fill_screen_black()
        draw_start_page_message()

    elif state.game_state == GameState.MENU_PAGE:
        fill_screen_black()
        draw_menu_buttons(text_button_one='Play Game', text_button_two='Quit Game')

    elif state.game_state == GameState.COUNTDOWN:
        fill_screen_with_map()
        state.marble.draw()
        draw_countdown_message()

    elif state.game_state == GameState.LEVEL_GAME:
        fill_screen_with_map()
        draw_timer_and_score_info()

        state.marble.draw()
        state.flag.draw()

        if state.enemy:
            state.enemy.draw()
        if state.coin_score != 6:  # todo add bool value
            state.coin.draw()

    elif state.game_state == GameState.GAME_OVER:
        fill_screen_with_map()
        draw_timer_and_score_info()

        if state.wait_counter_for_game_over != 0:
            draw_game_over_message()
        elif state.wait_counter_for_game_over == 0:
            draw_menu_buttons(text_button_one='Retry Level', text_button_two='Quit Game')

    elif state.game_state == GameState.LEVEL_WIN:
        fill_screen_with_map()
        if state.wait_counter_for_score_display == 0 or state.blue_text:
            text_color = Color.BLUE.value
        else:
            text_color = Color.ORANGE.value

        state.blue_text = not state.blue_text  # todo in update
        draw_timer_and_score_info(text_color_score=text_color)
        draw_bonus_score_info(text_color=text_color)

        if state.wait_counter_for_score_display == 0:
            draw_menu_buttons(text_button_one='Next Level', text_button_two='Quit Game')

    elif state.game_state == GameState.GAME_WIN:
        fill_screen_black()

        # todo
        state.screen.draw.text("YOU WIN!", center=(300, 300), color='white')
        state.screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
        state.screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                               fontsize=80)
        state.screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)
