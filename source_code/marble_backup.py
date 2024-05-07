# Marble Madness
import random

import pgzrun
from pgzero.actor import Actor
from pgzero.builtins import keyboard, mouse
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import Surface, Color
from pygame import image

import source_code.constants.game_constants as game_constants
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState


game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE

# level images
current_map: str = ''
current_map_short: str = ''
current_heightmap: str = ''
current_heightmap_short: str = ''

heightmap: image = None

overlay_position: set = game_constants.overlay_position_level_one

# marble
marble: Actor = Actor(image=game_constants.marble_image, center=game_constants.marble_position_level_one)
marbleh: Actor = Actor(game_constants.marble_image, center=game_constants.marbleh_position_level_one)
marble.dir = marble.speed = 0

# coin
coin: Actor = Actor(game_constants.coin_image, center=game_constants.coin_position_level_one)

# timer and scores
timer: int = 0
score: int = 0
coin_score: int = 0

# debug mode
debug: bool = False

# button
start_button: Actor = Actor(image=game_constants.start_button_image, center=game_constants.start_button_position)
quit_button: Actor = Actor(image=game_constants.quit_button_image, center=game_constants.quit_button_position)
back_button: Actor = Actor(image=game_constants.back_button_image, center=game_constants.back_button_position)
play_button: Actor = Actor(image=game_constants.play_button_image)

center_column: Color
left_column: Color
right_column: Color


def load_level_files():
    global current_level, current_map, current_heightmap, marble, marbleh, timer, overlay_position, heightmap

    match current_level:
        case LevelState.LEVEL_ONE:
            current_map = game_constants.level_one
            current_heightmap = game_constants.level_one_heightmap

            marble.dir = marble.speed = 0
            marble.x = game_constants.marble_position_level_one[0]
            marble.y = game_constants.marble_position_level_one[1]

            marbleh.x = game_constants.marbleh_position_level_one[0]
            marbleh.y = game_constants.marbleh_position_level_one[1]

            timer = game_constants.timer_level_one

            overlay_position = game_constants.overlay_position_level_one

        case LevelState.LEVEL_TWO:
            current_map = game_constants.level_two
            current_heightmap = game_constants.level_two_heightmap

            marble.dir = marble.speed = 0
            marble.x = game_constants.marble_position_level_two[0]
            marble.y = game_constants.marble_position_level_two[1]

            marbleh.x = game_constants.marbleh_position_level_two[0]
            marbleh.y = game_constants.marbleh_position_level_two[1]

            timer = game_constants.timer_level_two

            overlay_position = game_constants.overlay_position_level_two

        case LevelState.LEVEL_THREE:
            # TODO
            pass

        case LevelState.LEVEL_FOUR:
            # TODO
            pass

    heightmap = image.load(current_map)


def increment_level():
    global current_level

    match current_level:
        case LevelState.LEVEL_ONE:
            current_level = LevelState.LEVEL_TWO

        case LevelState.LEVEL_TWO:
            current_level = LevelState.LEVEL_THREE

        case LevelState.LEVEL_THREE:
            current_level = LevelState.LEVEL_FOUR


def draw():
    global marble, marbleh, current_map, current_heightmap, game_state, start_button, quit_button, coin, coin_score, play_button

    if not game_state == GameState.LEVEL_GAME:
        load_level_files()

    if debug:
        screen.blit(current_heightmap, (0, 0))
        marbleh.draw()

    else:
        screen.blit(current_map, (0, 0))

        match game_state:
            case GameState.START_PAGE:
                screen.fill((0, 0, 0))
                screen.draw.text("Press ENTER button!", center=(300, 400), color='white')

            case GameState.MENU_PAGE:
                screen.fill((0, 0, 0))
                start_button.pos = 300, 300
                start_button.draw()
                quit_button.pos = 300, 400
                quit_button.draw()
                load_level_files()

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.LEVEL_GAME:
                screen.blit(current_map, (0, 0))

                screen.draw.text('Time: ' + str(round(timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)  # todo
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)  # todo

                marble.draw()

                if coin_score != 2:
                    coin.draw()

                marble.draw()
                screen.blit(game_constants.overlay_image, overlay_position)

            case GameState.GAME_OVER:
                screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                screen.draw.text("GAME OVER!", center=(300, 300), color='white')
                screen.draw.text("Do you want to play again?", center=(300, 400), color='white')
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)

                quit_button.pos = 400, 500
                quit_button.draw()

                play_button.pos = 200, 500
                play_button.draw()
                load_level_files()

            case GameState.LEVEL_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("Press ENTER for next level!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)
                load_level_files()

            case GameState.GAME_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)


def update():
    global game_state, timer, score, coin_score

    if game_state == GameState.LEVEL_GAME:
        timer -= 1 / 60
        if timer <= 0:
            game_state = GameState.GAME_OVER

        if marble.colliderect(coin) and score != 2:
            coin.x = random.randint(150, 450)
            coin.y = random.randint(45, 500)
            score += 1  # todo: score abhängig von restlichem Timer?
            coin_score += 1

        if keyboard.left:
            marble.dir = max(marble.dir - 1, -1)
            marble.speed = min(1, marble.speed + 0.1)

        if keyboard.right:
            marble.dir = min(marble.dir + 1, 1)
            marble.speed = min(1, marble.speed + 0.1)

        if keyboard.up:
            marbleh.y -= 2
            marble.speed = min(1, marble.speed + 0.1)

        if keyboard.down:
            marbleh.y += 1.5
            marble.speed = min(1, marble.speed + 0.1)

        move_marble()
        marble.speed = max(0, marble.speed - 0.01)

    # damit man vom Startbildschirm ins Menü kommt
    elif game_state == GameState.START_PAGE and keyboard.RETURN:
        game_state = GameState.MENU_PAGE

    elif game_state == GameState.GAME_WIN and keyboard.RETURN:
        game_state = GameState.MENU_PAGE
        current_level = LevelState.LEVEL_ONE
        marble.pos = 300, 45  # todo: wanted like this? or position of level 1
        marbleh.pos = 300, 60

    elif game_state == GameState.LEVEL_WIN and keyboard.ENTER:
        increment_level()

    # print("gameState", game_state)
    # print(keyboard)


def move_marble():
    global marble, marbleh, game_state, current_level, center_column, left_column, right_column

    center_column = get_height(marbleh.x, marbleh.y)
    left_column = get_height(marbleh.x - 10, marbleh.y + 10)
    right_column = get_height(marbleh.x + 10, marbleh.y + 10)

    if center_column.r == 0:
        game_state = GameState.GAME_OVER

    if left_column.r < center_column.r or right_column.r < center_column.r:
        marble.y += marble.speed
        marble.speed += 0.03

    marbleh.x += marble.speed * marble.dir
    marbleh.y += marble.speed
    marble.x = marbleh.x
    marble.y = (marbleh.y * 0.6) + ((255 - center_column.r) * 1.25)
    marble.angle = marble.angle + marble.speed * marble.dir * -10

    if marble.angle > 0:
        marble.angle = -50
    elif marble.angle < -50:
        marble.angle = 0

    # Abfrage ob man im Ziel ist
    if marbleh.y > 610:  # todo: level abhängig, auch von x abhängig?
        if current_level == LevelState.LEVEL_FOUR:
            game_state = GameState.GAME_WIN
        else:
            game_state = GameState.LEVEL_WIN


# def on_key_down(key):
# print(key)

def on_mouse_down(pos, button):
    # print(button)
    global game_state, marbleh, marble

    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if game_state == GameState.MENU_PAGE and quit_button.collidepoint(pos) and mouse.LEFT:
        game_state = GameState.START_PAGE

    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif game_state == GameState.MENU_PAGE and start_button.collidepoint(pos) and mouse.LEFT:
        game_state = GameState.LEVEL_GAME

    # wenn man im GameOver Bildschirm ist
    elif game_state == GameState.GAME_OVER:
        # marble und marbleh in die Anfangsposition und Speed auf 0 setzen
        marble.pos = 300, 45
        marbleh.pos = 300, 60
        marble.speed = 0
        marbleh.speed = 0

        # wenn man im GameOver Bildschirm auf den Play Button drückt landet man im ersten Level
        # todo: eigentlich spielt man doch das gerade gespielte Level nochmal? so ist es auch implementiert
        if start_button.collidepoint(pos):
            game_state = GameState.LEVEL_GAME

        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif quit_button.collidepoint(pos):
            game_state = GameState.START_PAGE


def get_height(x, y):
    global heightmap
    try:
        return heightmap.get_at((int(x), int(y)))
    except IndexError:
        print("IndexError")


surf = Surface(size=[game_constants.WIDTH, game_constants.HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
# screen = Screen(surface=surf)
# pgzrun.mod.screen.
pgzrun.go()

