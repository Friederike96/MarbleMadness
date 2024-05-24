import source_code.constants.game_constants as game_constants
from source_code.constants import state
from source_code.enumerations.game_state import GameState
from source_code.functions.helper_functions.load_level_files import load_level_files


def draw():
    if not state.game_state == GameState.LEVEL_GAME:
        load_level_files()

    if state.debug:
        state.screen.blit(state.current_heightmap, state.current_map_position)
        state.marbleh.draw()

    else:
        state.screen.blit(state.current_map, state.current_map_position)

        match state.game_state:
            case GameState.START_PAGE:
                state.screen.fill((0, 0, 0))
                state.screen.draw.text(
                    "Press ENTER button!",
                    center=(game_constants.center_position_width, game_constants.enter_button_pos_y),
                    color='white'
                )

            case GameState.MENU_PAGE:
                state.screen.fill((0, 0, 0))
                state.start_button.pos = game_constants.center_position_width, game_constants.start_button_pos_y
                state.start_button.draw()
                state.quit_button.pos = game_constants.center_position_width, game_constants.quit_button_pos_y
                state.quit_button.draw()
                load_level_files()

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.LEVEL_GAME:
                state.screen.blit(state.current_map, state.current_map_position)

                state.screen.draw.text('Time: ' + str(round(state.timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)  # todo
                state.screen.draw.text('Score: ' + str(state.score), ((game_constants.WIDTH-100), 10), color=(255, 255, 255), fontsize=30)  # todo

                if state.load_start_position:
                    state.marble.pos = state.marble_start_pos_y, state.marble_start_pos_y
                    state.marbleh.pos = state.marbleh_start_pos_x, state.marbleh_start_pos_y
                    state.load_start_position = False

                    state.start_marble.draw()  # todo: needed?
                    state.marble.draw()

                if state.start_timer:
                    state.marble.draw()

                if state.coin_score != 2:
                    state.coin.draw()

                if state.start_timer:
                    state.marble.draw()
                # screen.blit(game_constants.overlay_image, overlay_position)

            case GameState.GAME_OVER:
                state.screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                state.screen.draw.text("GAME OVER!", center=(game_constants.center_position_width, 200), color='white')
                state.screen.draw.text("Do you want to play again?", center=(game_constants.center_position_width, 300), color='white')
                state.screen.draw.text('Score: ' + str(state.score), (game_constants.WIDTH-100, 10), color=(255, 255, 255), fontsize=30)

                state.quit_button.pos = game_constants.center_position_width, 500
                state.quit_button.draw()

                state.play_button.pos = game_constants.center_position_width, 400
                state.play_button.draw()
                load_level_files()

            case GameState.LEVEL_WIN:

                state.screen.fill((0, 0, 0))
                state.screen.draw.text(
                    "YOU WIN!",
                    center=(game_constants.center_position_width, 250), # todo
                    owidth=0.5,
                    ocolor=(255, 255, 255),
                    color=(0, 0, 255),
                    fontsize=80
                )
                state.screen.draw.text(
                    f'+ {state.display_coin_score} Coin-Punkte',
                    center=(game_constants.center_position_width, 290), # todo
                    color='white'
                )
                state.screen.draw.text(
                    f'+ {state.display_timer_score} Timer-Punkte',
                    center=(game_constants.center_position_width, 310), # todo
                    color='white'
                )
                state.screen.draw.text(
                    "Press BUTTON for next level!",
                    center=(game_constants.center_position_width, 350), # todo
                    color='white'
                )
                state.screen.draw.text('Score: ' + str(state.score), (game_constants.WIDTH-100, 10), color=(255, 255, 255), fontsize=30)

                state.play_button.pos = game_constants.center_position_width, game_constants.play_button_pos_y
                state.play_button.draw()
                load_level_files()

            case GameState.GAME_WIN:
                state.screen.fill((0, 0, 0))
                state.screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                state.screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                state.screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                state.screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)
