from pgzero.builtins import mouse

from constants import state, game_constants
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.backend.load_level_files import load_level_files
#
#
# def on_mouse_down(pos):
#
#     # wenn man im Menü auf Enter drückt landet man im Startbildschirm
#     if state.game_state == GameState.MENU_PAGE and state.quit_button.collidepoint(pos) and mouse.LEFT:
#         state.game_state = GameState.START_PAGE
#         state.score = 0
#
#     # wenn man im Menü auf Start drückt landet man im ersten Level
#     elif state.game_state == GameState.MENU_PAGE and state.start_button.collidepoint(pos) and mouse.LEFT:
#         state.game_state = GameState.COUNTDOWN
#         state.countdown_timer = state.timer
#         state.printed_timer = False
#
#     elif state.game_state == GameState.LEVEL_WIN:
#         if(
#             game_constants.center_position_width-50 <= pos[0] <= game_constants.center_position_width+50
#             and game_constants.center_position_height-10 <= pos[1] <= game_constants.center_position_height+10
#         ):  # todo: make button colorful when hovering and clicking
#             state.game_state = GameState.COUNTDOWN
#             state.printed_timer = False
#             #increment_level()
#             load_level_files()
#             print('blah')
#
#     # wenn man im GameOver Bildschirm ist
#     elif state.game_state == GameState.GAME_OVER:
#         # todo: marble und marbleh in die Anfangsposition und Speed auf 0 setzen
#     #    marble.pos = 300, 45
#     #    marbleh.pos = 300, 60
#         state.marble.speed = 0
#         state.marbleh.speed = 0
#
#         # wenn man im GameOver Bildschirm auf den Play Button drückt spielt man das Level erneut
#         if state.play_button.collidepoint(pos):
#             state.game_state = GameState.LEVEL_GAME
#
#         # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
#         elif state.quit_button.collidepoint(pos):
#             state.game_state = GameState.START_PAGE
#             state.current_level = LevelState.LEVEL_ONE
#             load_level_files()
#             state.score = 0
