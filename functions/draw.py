import constants.game_constants as game_constants
from constants import state
from enumerations.game_state import GameState
from functions.backend.load_level_files import load_level_files
from functions.frontend.get_font import get_monospaced_font
from functions.frontend.draw_menu_buttons import draw_menu_buttons


def draw():
    if state.start_game:
        load_level_files()
        state.start_game = False

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
                    center=(game_constants.center_position_width, game_constants.center_position_height),
                    color='white',
                    fontname=get_monospaced_font(),
                    fontsize=30
                )

            case GameState.MENU_PAGE:
                state.screen.fill((0, 0, 0))
                draw_menu_buttons(text_one='Play Game', text_two='Quit Game')
                load_level_files() # todo: should be in update

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.COUNTDOWN:
                state.marble.x = state.marble_start_pos_x
                state.marble.y = state.marble_start_pos_y
                state.marble.draw()
                state.screen.blit(state.current_map, state.current_map_position)
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
                    fontsize=20,
                    background='grey'
                )
                state.printed_timer = True

            case GameState.LEVEL_GAME:
                state.screen.blit(state.current_map, state.current_map_position)

                state.screen.draw.text(
                    str(int(state.timer)),
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
                    str(state.score) + '',
                    (10, 30),
                    color=(0, 0, 139),
                    fontname=get_monospaced_font(),
                    fontsize=20,
                    background='grey'
                )
                state.marble.draw()

                if state.coin_score != 2:
                    state.coin.draw()
                # screen.blit(game_constants.overlay_image, overlay_position)

            case GameState.GAME_OVER:
                state.screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                state.screen.draw.text("GAME OVER!", center=(game_constants.center_position_width, 200), color='white')
                state.screen.draw.text("Do you want to play again?", center=(game_constants.center_position_width, 300), color='white')
                state.screen.draw.text('Score: ' + str(state.score), (game_constants.WIDTH - 100, 10), color=(255, 255, 255), fontsize=30)

                state.quit_button.pos = game_constants.center_position_width, 500
                state.quit_button.draw()

                state.play_button.pos = game_constants.center_position_width, 400
                state.play_button.draw()
                load_level_files()

            case GameState.LEVEL_WIN:

                if state.wait_counter == 0 or state.colorful:
                    text_color = (0, 0, 139)
                else:
                    text_color = 'orange'

                state.colorful = not state.colorful

                state.screen.draw.text(
                    str(int(state.timer)),
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
                    str(state.score) + '',
                    (10, 30),
                    color=text_color,
                    fontname=get_monospaced_font(),
                    fontsize=15,
                    background='grey'
                )
                state.screen.draw.text(
                    f'Bonus for time left:  {state.display_timer_score}',
                    (10, 50),
                    color=text_color,
                    fontname=get_monospaced_font(),
                    fontsize=15,
                    background='grey'
                )
                state.screen.draw.text(
                    f'Bonus for coins:  {state.display_coin_score}',
                    (10, 70),
                    color=text_color,
                    fontname=get_monospaced_font(),
                    fontsize=15,
                    background='grey'
                )

                if state.wait_counter == 0:
                    draw_menu_buttons(text_one='Next Level', text_two='Quit Game')

            case GameState.GAME_WIN:
                state.screen.fill((0, 0, 0))
                state.screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                state.screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                state.screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                       fontsize=80)
                state.screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)
