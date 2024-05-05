# Marble Madness
import pgzrun
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import image, Surface
from pgzero.builtins import keyboard, Actor, mouse
import random
import pgzero.screen
import state
import game_constants
from game_state import GameState


def draw():
    # if current_level == 0:
    state.current_map = game_constants.level_one
    state.current_map_short = game_constants.level_one_short
    state.current_heightmap = game_constants.level_one_heightmap
    state.current_heightmap_short = game_constants.level_one_heightmap_short

    heightmap = image.load(state.current_map)

    if state.debug:
        screen.blit(state.current_heightmap_short, (0, 0))
        marbleh.draw()

    else:
        screen.blit(state.current_map_short, (0, 0))

        match state.game_state:
            case GameState.START_PAGE:
                screen.fill((0, 0, 0))
                screen.draw.text("Press ENTER button!", center=(300, 400), color='white')

            case GameState.MENU_PAGE:
                screen.fill((0, 0, 0))
                btn_start.pos = 300, 300
                btn_start.draw()
                btn_quit.pos = 300, 400
                btn_quit.draw()

            case GameState.PLACEHOLDER:
                print("menu maybe?")

            case GameState.LEVEL_ONE:
                screen.blit("map", (0, 0))
                screen.draw.text('Time: ' + str(round(timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)
                marble.draw()
                if coinscore != 2:
                    coin.draw()
                marble.draw()
                # screen.blit("objects/overlay", (0, 0))
                screen.blit("objects/overlay", (365, 150))
                curr_level = 1

            case GameState.LEVEL_TWO:
                print("level 2")

            case GameState.LEVEL_THREE:
                print("level 3")

            case GameState.LEVEL_FOUR:
                print("level 4")

            case GameState.GAME_OVER:
                screen.fill((0, 0, 0))
                # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
                screen.draw.text("GAME OVER!", center=(300, 300), color='white')
                screen.draw.text("Do you want to play again?", center=(300, 400), color='white')
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)
                btn_quit.pos = 400, 500
                btn_quit.draw()
                btn_play.pos = 200, 500
                btn_play.draw()

            case GameState.WIN:
                screen.fill((0, 0, 0))
                screen.draw.text("YOU WIN!", center=(300, 300), color='white')
                screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)




def update():
    state.timer -= 1 / 60
    if state.timer <= 0:
        state.game_state = GameState.GAME_OVER

    if marble.colliderect(coin) and score != 2:
        coin.x = random.randint(150, 450)
        coin.y = random.randint(45, 500)
        score += 1
        coinscore += 1

    if state.game_state in [GameState.LEVEL_ONE, GameState.LEVEL_TWO, GameState.LEVEL_THREE, GameState.LEVEL_FOUR]:
        if keyboard.left:
            marble.dir = max(marble.dir - 0.1, -1)
            marble.speed = min(1, marble.speed + 0.1)
        if keyboard.right:
            marble.dir = min(marble.dir + 0.1, 1)
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
    elif game_state == 0 and keyboard.RETURN:
        game_state = 1
    elif game_state == 11 and keyboard.RETURN:
        game_state = 1
        marble.pos = 300, 45
        marbleh.pos = 300, 60

    # print("gameState", game_state)
    # print(keyboard)


def move_marble():
    center_column = get_height(marbleh.x, marbleh.y)
    left_column = get_height(marbleh.x - 10, marbleh.y + 10)
    right_column = get_height(marbleh.x + 10, marbleh.y + 10)

    if center_column.r == 0:
        state.game_state = GameState.GAME_OVER

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
    if marbleh.y > 610:
        state.game_state = GameState.WIN


# def on_key_down(key):
# print(key)

def on_mouse_down(pos, button):
    # print(button)
    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if state.game_state == GameState.MENU_PAGE and btn_quit.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.START_PAGE
    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif state.game_state == GameState.MENU_PAGE and btn_start.collidepoint(pos) and mouse.LEFT:
        state.game_state = GameState.LEVEL_ONE
    # wenn man im GameOver Bildschirm ist
    elif state.game_state == GameState.GAME_OVER:
        # marble und marbleh in die Anfangsposition und Speed auf 0 setzen
        marble.pos = 300, 45
        marbleh.pos = 300, 60
        marble.speed = 0
        marbleh.speed = 0
        # wenn man im GameOver Bildschirm auf den Play Button drückt landet man im ersten Level
        if btn_play.collidepoint(pos):
            state.game_state = GameState.LEVEL_ONE
        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif btn_quit.collidepoint(pos):
            state.game_state = GameState.START_PAGE


def get_height(x, y):
    return state.heightmap.get_at((int(x), int(y)))


surf = Surface(size=[game_constants.WIDTH, game_constants.HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
# screen = Screen(surface=surf)
# pgzrun.mod.screen.
pgzrun.go()
