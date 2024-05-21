# Marble Madness
import random

import pgzrun
from pgzero.builtins import keyboard, mouse
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import Surface

import source_code.constants.game_constants as game_constants
from source_code.constants import state
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState
from source_code.helper_functions.increment_level import increment_level
from source_code.helper_functions.load_level_files import load_level_files

# do not delete, needed here
HEIGHT = 760
WIDTH = 900


# TODO: game loop einbauen

def draw():
    if not state.game_state == GameState.LEVEL_GAME:
        load_level_files()

    if state.debug:
        screen.blit(state.current_heightmap, state.current_map_position)
        state.marbleh.draw()

    else:
        screen.blit(state.current_map, state.current_map_position)

        match state.game_state:
            case GameState.START_PAGE:
                screen.fill((0, 0, 0))
                screen.draw.text(
                    "Press ENTER button!",
                    center=(game_constants.center_position_width, game_constants.enter_button_pos_y),
                    color='white'
                )

            case GameState.MENU_PAGE:
                screen.fill((0, 0, 0))
                state.start_button.pos = game_constants.center_position_width, game_constants.start_button_pos_y
                state.start_button.draw()
                state.quit_button.pos = game_constants.center_position_width, game_constants.quit_button_pos_y
                state.quit_button.draw()
                load_level_files()

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.LEVEL_GAME:
                screen.blit(state.current_map, state.current_map_position)

                screen.draw.text('Time: ' + str(round(state.timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)  # todo
                screen.draw.text('Score: ' + str(state.score), ((game_constants.WIDTH-100), 10), color=(255, 255, 255), fontsize=30)  # todo

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
                screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                screen.draw.text("GAME OVER!", center=(game_constants.center_position_width, 200), color='white')
                screen.draw.text("Do you want to play again?", center=(game_constants.center_position_width, 300), color='white')
                screen.draw.text('Score: ' + str(state.score), (game_constants.WIDTH-100, 10), color=(255, 255, 255), fontsize=30)

                state.quit_button.pos = game_constants.center_position_width, 500
                state.quit_button.draw()

                state.play_button.pos = game_constants.center_position_width, 400
                state.play_button.draw()
                load_level_files()

            case GameState.LEVEL_WIN:

                screen.fill((0, 0, 0))
                screen.draw.text(
                    "YOU WIN!",
                    center=(game_constants.center_position_width, 250), # todo
                    owidth=0.5,
                    ocolor=(255, 255, 255),
                    color=(0, 0, 255),
                    fontsize=80
                )
                screen.draw.text(
                    f'+ {state.display_coin_score} Coin-Punkte',
                    center=(game_constants.center_position_width, 290), # todo
                    color='white'
                )
                screen.draw.text(
                    f'+ {state.display_timer_score} Timer-Punkte',
                    center=(game_constants.center_position_width, 310), # todo
                    color='white'
                )
                screen.draw.text(
                    "Press BUTTON for next level!",
                    center=(game_constants.center_position_width, 350), # todo
                    color='white'
                )
                screen.draw.text('Score: ' + str(state.score), (game_constants.WIDTH-100, 10), color=(255, 255, 255), fontsize=30)

                state.play_button.pos = game_constants.center_position_width, game_constants.play_button_pos_y
                state.play_button.draw()
                load_level_files()

            case GameState.GAME_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)


def update():
    if not state.start_timer and keyboard.left or keyboard.right or keyboard.up or keyboard.down:
        state.start_timer = True

    if state.game_state == GameState.LEVEL_GAME and state.start_timer:
        state.timer -= 1 / 60
        if state.timer <= 0:
            state.game_state = GameState.GAME_OVER

        else:
            if state.marble.colliderect(state.coin) and state.score != 2:
                state.coin.x = random.randint(150, 450)
                state.coin.y = random.randint(45, 500)
                state.score += 1  # todo: score abhängig von restlichem Timer?
                state.coin_score += 1

            if keyboard.left:
                state.marble.dir = max(state.marble.dir - 1, -1)
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.right:
                state.marble.dir = min(state.marble.dir + 1, 1)
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.up:
                state.marbleh.y -= 2
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.down:
                state.marbleh.y += 1.5
                state.marble.speed = min(1, state.marble.speed + 0.1)

            move_marble()
            state.marble.speed = max(0, state.marble.speed - 0.01)

    # damit man vom Startbildschirm ins Menü kommt
    elif state.game_state == GameState.START_PAGE and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE

    elif state.game_state == GameState.GAME_WIN and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE
        state.current_level = LevelState.LEVEL_ONE
        state.marble.pos = 300, 45  # todo: wanted like this? or position of level 1
        state.marbleh.pos = 300, 60

    elif state.game_state == GameState.LEVEL_WIN and state.not_added_points_and_incremented:
        add_timing_points()
        increment_level()
        state.not_added_points_and_incremented = False


def add_timing_points():
    timer_score = int(state.timer/3)
    state.score += timer_score
    state.display_timer_score = timer_score

    state.score += state.coin_score
    state.display_coin_score = state.coin_score
    state.coin_score = 0

    state.timer = 0


def move_marble():
    center_column = get_height(state.marbleh.x, state.marbleh.y)
    left_column = get_height(state.marbleh.x - 10, state.marbleh.y + 10)
    right_column = get_height(state.marbleh.x + 10, state.marbleh.y + 10)

    if center_column is None: # or center_column.r == 0:
        state.game_state = GameState.GAME_OVER  # reminder: change back
        return

    if left_column.r < center_column.r or right_column.r < center_column.r:
        state.marble.y += state.marble.speed
        state.marble.speed += 0.03

    state.marbleh.x += state.marble.speed * state.marble.dir
    state.marbleh.y += state.marble.speed
    state.marble.x = state.marbleh.x
    state.marble.y = (state.marbleh.y * 0.6) + ((255 - center_column.r) * 1.25)
    state.marble.angle = state.marble.angle + state.marble.speed *state.marble.dir * -10

    if state.marble.angle > 0:
        state.marble.angle = -50
    elif state.marble.angle < -50:
        state.marble.angle = 0

    # Abfrage ob man im Ziel ist
    if state.marbleh.y > 700:  # todo: level abhängig, auch von x abhängig?
        if state.current_level == LevelState.LEVEL_FOUR:
            state.game_state = GameState.GAME_WIN
        else:
            state.game_state = GameState.LEVEL_WIN
            state.not_added_points_and_incremented = True


# def on_key_down(key):
# print(key)

def on_mouse_down(pos, button):
    # print(button)
    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if state.game_state == GameState.MENU_PAGE and state.quit_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.START_PAGE
        state.score = 0

    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif state.game_state == GameState.MENU_PAGE and state.start_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.LEVEL_GAME

    elif state.game_state == GameState.LEVEL_WIN and state.play_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.LEVEL_GAME
        load_level_files()

    # wenn man im GameOver Bildschirm ist
    elif state.game_state == GameState.GAME_OVER:
        # todo: marble und marbleh in die Anfangsposition und Speed auf 0 setzen
    #    marble.pos = 300, 45
    #    marbleh.pos = 300, 60
        state.marble.speed = 0
        state.marbleh.speed = 0

        # wenn man im GameOver Bildschirm auf den Play Button drückt spielt man das Level erneut
        if state.play_button.collidepoint(pos):
            state.game_state = GameState.LEVEL_GAME

        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif state.quit_button.collidepoint(pos):
            state.game_state = GameState.START_PAGE
            state.current_level = LevelState.LEVEL_ONE
            load_level_files()
            state.score = 0


def get_height(x, y):
    if x > game_constants.WIDTH:
        x = game_constants.WIDTH
    if y > game_constants.HEIGHT:
        y = game_constants.HEIGHT
    try:
        return state.heightmap.get_at((int(x), int(y)))
    except IndexError as e:
        print(e)


surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
pgzrun.go()
