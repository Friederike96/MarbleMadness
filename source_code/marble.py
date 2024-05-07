# Marble Madness
import random

import pgzrun
from pgzero.builtins import keyboard, mouse
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import Surface
from pygame import image

import source_code.constants.game_constants as game_constants
import source_code.constants.state as state
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState




def load_level_files():
    match state.current_level:
        case LevelState.LEVEL_ONE:
            state.current_map = game_constants.level_one
            state.current_map_short = game_constants.level_one
            state.current_heightmap = game_constants.level_one_heightmap
            state.current_heightmap_short = game_constants.level_one_heightmap

            state.marble.dir = state.marble.speed = 0
            state.marble.x = game_constants.marble_position_level_one[0]
            state.marble.y = game_constants.marble_position_level_one[1]

            state.marbleh.x = game_constants.marbleh_position_level_one[0]
            state.marbleh.y = game_constants.marbleh_position_level_one[1]

            state.timer = game_constants.timer_level_one

            state.overlay_position = game_constants.overlay_position_level_one

        case LevelState.LEVEL_TWO:
            state.current_map = game_constants.level_two
            state.current_map_short = game_constants.level_two
            state.current_heightmap = game_constants.level_two_heightmap
            state.current_heightmap_short = game_constants.level_two_heightmap

            state.marble.dir = state.marble.speed = 0
            state.marble.x = game_constants.marble_position_level_two[0]
            state.marble.y = game_constants.marble_position_level_two[1]

            state.marbleh.x = game_constants.marbleh_position_level_two[0]
            state.marbleh.y = game_constants.marbleh_position_level_two[1]

            state.timer = game_constants.timer_level_two

            state.overlay_position = game_constants.overlay_position_level_two

        case LevelState.LEVEL_THREE:
            # TODO
            pass

        case LevelState.LEVEL_FOUR:
            # TODO
            pass

    state.heightmap = image.load(state.current_map)


def increment_level():
    match state.current_level:
        case LevelState.LEVEL_ONE:
            LevelState.LEVEL_TWO

        case LevelState.LEVEL_TWO:
            LevelState.LEVEL_THREE

        case LevelState.LEVEL_THREE:
            LevelState.LEVEL_FOUR


def draw():
    load_level_files()

    if state.debug:
        screen.blit(state.current_heightmap_short, (0, 0))
        state.marbleh.draw()

    else:
        screen.blit(state.current_map_short, (0, 0))

        match state.game_state:
            case GameState.START_PAGE:
                screen.fill((0, 0, 0))
                screen.draw.text("Press ENTER button!", center=(300, 400), color='white')

            case GameState.MENU_PAGE:
                screen.fill((0, 0, 0))
                state.start_button.pos = 300, 300
                state.start_button.draw()
                state.quit_button.pos = 300, 400
                state.quit_button.draw()

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.LEVEL_GAME:
                screen.blit(state.current_map_short, (0, 0))

                screen.draw.text('Time: ' + str(round(state.timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)  # todo
                screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)  # todo

                state.marble.draw()

                if state.coin_score != 2:
                    state.coin.draw()

                state.marble.draw()
                screen.blit(game_constants.overlay_image, state.overlay_position)

            case GameState.GAME_OVER:
                screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                screen.draw.text("GAME OVER!", center=(300, 300), color='white')
                screen.draw.text("Do you want to play again?", center=(300, 400), color='white')
                screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)

                state.quit_button.pos = 400, 500
                state.quit_button.draw()

                state.play_button.pos = 200, 500
                state.play_button.draw()

            case GameState.LEVEL_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("Press ENTER for next level!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)

            case GameState.GAME_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(state.score), (500, 10), color=(255, 255, 255), fontsize=30)


def update():
    if state.game_state == GameState.LEVEL_GAME:
        state.timer -= 1 / 60
        if state.timer <= 0:
            state.game_state = GameState.GAME_OVER

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

    elif state.game_state == GameState.LEVEL_WIN and keyboard.ENTER:
        increment_level()

    # print("gameState", game_state)
    # print(keyboard)


def move_marble():
    center_column = get_height(state.marbleh.x, state.marbleh.y)
    left_column = get_height(state.marbleh.x - 10, state.marbleh.y + 10)
    right_column = get_height(state.marbleh.x + 10, state.marbleh.y + 10)

    if center_column.r == 0:
        state.game_state = GameState.GAME_OVER

    if left_column.r < center_column.r or right_column.r < center_column.r:
        state.marble.y += state.marble.speed
        state.marble.speed += 0.03

    state.marbleh.x += state.marble.speed * state.marble.dir
    state.marbleh.y += state.marble.speed
    state.marble.x = state.marbleh.x
    state.marble.y = (state.marbleh.y * 0.6) + ((255 - center_column.r) * 1.25)
    state.marble.angle = state.marble.angle + state.marble.speed * state.marble.dir * -10

    if state.marble.angle > 0:
        state.marble.angle = -50
    elif state.marble.angle < -50:
        state.marble.angle = 0

    # Abfrage ob man im Ziel ist
    if state.marbleh.y > 610:  # todo: level abhängig, auch von x abhängig?
        if state.current_level == LevelState.LEVEL_FOUR:
            state.game_state = GameState.GAME_WIN
        else:
            state.game_state = GameState.LEVEL_WIN


# def on_key_down(key):
# print(key)

def on_mouse_down(pos, button):
    # print(button)

    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if state.game_state == GameState.MENU_PAGE and state.quit_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.START_PAGE

    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif state.game_state == GameState.MENU_PAGE and state.start_button.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.LEVEL_GAME

    # wenn man im GameOver Bildschirm ist
    elif state.game_state == GameState.GAME_OVER:
        # marble und marbleh in die Anfangsposition und Speed auf 0 setzen
        state.marble.pos = 300, 45
        state.marbleh.pos = 300, 60
        state.marble.speed = 0
        state.marbleh.speed = 0

        # wenn man im GameOver Bildschirm auf den Play Button drückt landet man im ersten Level
        # todo: eigentlich spielt man doch das gerade gespielte Level nochmal? so ist es auch implementiert
        if state.start_button.collidepoint(pos):
            state.game_state = GameState.LEVEL_GAME

        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif state.quit_button.collidepoint(pos):
            state.game_state = GameState.START_PAGE


def get_height(x, y):
    return state.heightmap.get_at((int(x), int(y)))


surf = Surface(size=[game_constants.WIDTH, game_constants.HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
# screen = Screen(surface=surf)
# pgzrun.mod.screen.
pgzrun.go()

