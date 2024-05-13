# Marble Madness
import random

import pgzrun
from pgzero.actor import Actor
from pgzero.builtins import keyboard, mouse
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import Surface
from pygame import image

import source_code.constants.game_constants as game_constants
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState

HEIGHT = 760
WIDTH = 900

game_state: GameState = GameState.START_PAGE
current_level: LevelState = LevelState.LEVEL_ONE

# level images
current_map: str = ''
current_map_short: str = ''
current_heightmap: str = ''
current_heightmap_short: str = ''

current_map_position: set = ()

load_start_position: bool = True
start_timer: bool = False

marble_start_pos_x: int = 0
marble_start_pos_y: int = 0
marbleh_start_pos_x: int = 0
marbleh_start_pos_y: int = 0

heightmap: image = None

# marble
marble: Actor = Actor(image=game_constants.marble_image, center=(450, 45))
marbleh: Actor = Actor(image=game_constants.marble_image, midtop=game_constants.marbleh_position_level_one)
marble.dir = marble.speed = 0

# coin
coin: Actor = Actor(image=game_constants.coin_image, center=game_constants.coin_position_level_one)
start_marble: Actor = Actor(image=game_constants.coin_image, center=(450, 45))

# timer and scores
timer: int = 0
score: int = 0
coin_score: int = 0

# debug mode
debug: bool = False

# button
start_button: Actor = Actor(image=game_constants.start_button_image)
quit_button: Actor = Actor(image=game_constants.quit_button_image)
back_button: Actor = Actor(image=game_constants.back_button_image)
play_button: Actor = Actor(image=game_constants.play_button_image)


def load_level_files():
    global current_level, current_map, current_heightmap, marble, marbleh, timer, overlay_position, heightmap, \
        current_map_position, load_start_position, marble_start_pos_x, marble_start_pos_y, marbleh_start_pos_x, marbleh_start_pos_y, \
    start_timer, start_marble

    match current_level:
        case LevelState.LEVEL_ONE:
            current_map = game_constants.level_one
            current_heightmap = game_constants.level_one_heightmap
            current_map_position = game_constants.level_one_map_position

            marble.dir = marble.speed = 0

            marble_start_pos_x = game_constants.marble_position_level_one[0]
            marble_start_pos_y = game_constants.marble_position_level_one[0]

            marbleh_start_pos_x = game_constants.marbleh_position_level_one[0]
            marbleh_start_pos_y = game_constants.marbleh_position_level_one[0]

            load_start_position = True
            start_timer = False

            timer = game_constants.timer_level_one

            overlay_position = game_constants.overlay_position_level_one

        case LevelState.LEVEL_TWO:
            current_map = game_constants.level_two
            current_heightmap = game_constants.level_two_heightmap
            current_map_position = game_constants.level_two_map_position

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

    heightmap = image.load(current_heightmap)


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
    global marble, load_start_position, marbleh, current_map, current_heightmap, game_state, start_button, quit_button, \
        coin, coin_score, play_button, current_map_position, marble_start_pos_x, marble_start_pos_y, marbleh_start_pos_x,\
        marbleh_start_pos_y, start_timer

    if not game_state == GameState.LEVEL_GAME:
        load_level_files()

    if debug:
        screen.blit(current_heightmap, current_map_position)
        marbleh.draw()

    else:
        screen.blit(current_map, current_map_position)

        match game_state:
            case GameState.START_PAGE:
                screen.fill((0, 0, 0))
                screen.draw.text(
                    "Press ENTER button!",
                    center=(game_constants.center_position_width, game_constants.enter_button_pos_y),
                    color='white'
                )

            case GameState.MENU_PAGE:
                screen.fill((0, 0, 0))
                start_button.pos = game_constants.center_position_width, game_constants.start_button_pos_y
                start_button.draw()
                quit_button.pos = game_constants.center_position_width, game_constants.quit_button_pos_y
                quit_button.draw()
                load_level_files()

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.LEVEL_GAME:
                screen.blit(current_map, current_map_position)

                screen.draw.text('Time: ' + str(round(timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)  # todo
                screen.draw.text('Score: ' + str(score), ((WIDTH-100), 10), color=(255, 255, 255), fontsize=30)  # todo

                if load_start_position:
                    marble.pos = marble_start_pos_y, marble_start_pos_y
                    marbleh.pos = marbleh_start_pos_x, marbleh_start_pos_y
                    load_start_position = False

                    start_marble.draw()
                    marble.draw()

                if start_timer:
                    marble.draw()

                if coin_score != 2:
                    coin.draw()

                if start_timer:
                    marble.draw()
                # screen.blit(game_constants.overlay_image, overlay_position)

            case GameState.GAME_OVER:
                screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                screen.draw.text("GAME OVER!", center=(game_constants.center_position_width, 200), color='white')
                screen.draw.text("Do you want to play again?", center=(game_constants.center_position_width, 300), color='white')
                screen.draw.text('Score: ' + str(score), (WIDTH-100, 10), color=(255, 255, 255), fontsize=30)

                quit_button.pos = game_constants.center_position_width, 400
                quit_button.draw()

                play_button.pos = game_constants.center_position_width, 500
                play_button.draw()
                load_level_files()

            case GameState.LEVEL_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text(
                    "Press BUTTON for next level!",
                    center=(game_constants.center_position_width, 350), # todo
                    color='white'
                )
                screen.draw.text(
                    "YOU WIN!",
                    center=(WIDTH/2, 250), # todo
                    owidth=0.5,
                    ocolor=(255, 255, 255),
                    color=(0, 0, 255),
                    fontsize=80
                )
                screen.draw.text('Score: ' + str(score), (WIDTH-100, 10), color=(255, 255, 255), fontsize=30)

                play_button.pos = game_constants.center_position_width, game_constants.play_button_pos_y
                play_button.draw()
                load_level_files()

            case GameState.GAME_WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)


def update():
    global game_state, timer, score, coin_score, start_timer

    if not start_timer and keyboard.left or keyboard.right or keyboard.up or keyboard.down:
        start_timer = True

    if game_state == GameState.LEVEL_GAME and start_timer:
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

    elif game_state == GameState.LEVEL_WIN:
        add_timing_points()
        increment_level()

    # print("gameState", game_state)
    # print(keyboard)


def add_timing_points():
    global score, timer

    score_to_add = int(timer/3)
    score += score_to_add
    timer = 0


def move_marble():
    global marble, marbleh, game_state, current_level, center_column, left_column, right_column

    center_column = get_height(marbleh.x, marbleh.y)
    left_column = get_height(marbleh.x - 10, marbleh.y + 10)
    right_column = get_height(marbleh.x + 10, marbleh.y + 10)

    if center_column is None: # or center_column.r == 0:
        game_state = GameState.GAME_OVER  # reminder: change back
        return

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
    if marbleh.y > 700:  # todo: level abhängig, auch von x abhängig?
        if current_level == LevelState.LEVEL_FOUR:
            game_state = GameState.GAME_WIN
        else:
            game_state = GameState.LEVEL_WIN


# def on_key_down(key):
# print(key)

def on_mouse_down(pos, button):
    # print(button)
    global game_state, marbleh, marble, quit_button, start_button, current_level, score

    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if game_state == GameState.MENU_PAGE and quit_button.collidepoint(pos) and mouse.LEFT:
        game_state = GameState.START_PAGE
        score = 0

    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif game_state == GameState.MENU_PAGE and start_button.collidepoint(pos) and mouse.LEFT:
        game_state = GameState.LEVEL_GAME

    elif game_state == GameState.LEVEL_WIN and play_button.collidepoint(pos) and mouse.LEFT:
        game_state = GameState.LEVEL_GAME

    # wenn man im GameOver Bildschirm ist
    elif game_state == GameState.GAME_OVER:
        # marble und marbleh in die Anfangsposition und Speed auf 0 setzen
    #    marble.pos = 300, 45
    #    marbleh.pos = 300, 60
        marble.speed = 0
        marbleh.speed = 0

        # wenn man im GameOver Bildschirm auf den Play Button drückt spielt man das Level erneut
        if start_button.collidepoint(pos):
            game_state = GameState.LEVEL_GAME

        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif quit_button.collidepoint(pos):
            game_state = GameState.START_PAGE
            current_level = LevelState.LEVEL_ONE
            load_level_files()
            score = 0


def get_height(x, y):
    global heightmap
    if x > game_constants.WIDTH:
        x = game_constants.WIDTH
    if y > game_constants.HEIGHT:
        y = game_constants.HEIGHT
    try:
        return heightmap.get_at((int(x), int(y)))
    except IndexError as e:
        print(e)


surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
# screen = Screen(surface=surf)
# pgzrun.mod.screen.
pgzrun.go()

