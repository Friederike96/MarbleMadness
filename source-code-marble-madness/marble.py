# Marble Madness
import pgzrun
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import image, Surface
from pgzero.builtins import keyboard, Actor, mouse
import random
import pgzero.screen


# HEIGHT = 570
# WIDTH = 600

HEIGHT = 760
WIDTH = 904

level_one = 'images/level_1/map.png'
level_one_short = 'level_1/map.png'
level_one_heightmap = 'images/level_1/height45.png'

level_two = 'images/level_2/map.png'
level_two_short = 'level_2/map.png'
level_two_heightmap = 'images/level_2/heightmap_skaliert.png'
level_two_heightmap_short = 'level_2/heightmap_skaliert.png'


game_state = 0
curr_level = 0

btn_start = Actor('btn_start', center=(300, 300))
btn_quit = Actor('btn_quit', center=(300, 400))
btn_back = Actor('btn_back', center=(300, 400))
btn_play = Actor('btn_play')

# marble = Actor('objects/marble', center=(300, 45))
# marbleh = Actor('objects/marble', center=(300, 60))
heightmap = image.load(level_two_heightmap)
marble = Actor('objects/marble', center=(310, 20))
marble.x = 350
marble.y = 350
marbleh = Actor('objects/marble', center=(310, 20))
marbleh.x = 350
marbleh.y = 50
marble.dir = marble.speed = 0
heightmap = image.load('images/height45.png')
debug = False
timer = 30
score = 0
coinscore = 0
coin = Actor('objects/coingold')
coin.x = (150)
coin.y = (45)


def draw():
    global game_state
    global curr_level
    if (debug):
        screen.blit(level_one_heightmap_short, (0, 0))
        marbleh.draw()
    else:
        screen.blit(level_one_short, (0, 0))
        if game_state == 0:
            screen.fill((0, 0, 0))
            screen.draw.text("Press ENTER button!", center=(300, 400), color='white')
        elif game_state == 1:
            screen.fill((0, 0, 0))
            btn_start.pos = 300, 300
            btn_start.draw()
            btn_quit.pos = 300, 400
            btn_quit.draw()
        elif game_state == 2:
            print("menu maybe?")
        elif game_state == 3:
            screen.blit("map", (0, 0))
            screen.draw.text('Time: ' + str(round(timer, 2)), (10,10), color=(255,255,255), fontsize=30)
            screen.draw.text('Score: ' + str(score), (500,10), color=(255,255,255), fontsize=30)
            marble.draw()
            if coinscore != 2:
                coin.draw()
            marble.draw()
            curr_level = 1
        elif game_state == 4:
            print("level 2")
        elif game_state == 5:
            print("level 3")
        elif game_state == 6:
            screen.fill((0, 0, 0))
            # überprüfen ob timer auf 0 wenn ja dann game over nicht anzeigen sondern timer over oder so?
            screen.draw.text("GAME OVER!", center=(300, 300), color='white')
            screen.draw.text("Do you want to play again?", center=(300, 400), color='white')
            screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)
            btn_quit.pos = 400, 500
            btn_quit.draw()
            btn_play.pos = 200, 500
            btn_play.draw()
        elif game_state == 11:
            screen.fill((0, 0, 0))
            screen.draw.text("YOU WIN!", center=(300, 300), color='white')
            screen.draw.text("Press RETURN for start screen!", center=(300, 400), color='white')
            screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                             fontsize=80)
            screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)

        # screen.blit("objects/overlay", (0, 0))
        screen.blit("objects/overlay", (365, 150))


def update():
    global timer, game_state, score, coinscore

    timer -= 1 / 60
    if timer <= 0:
        game_state = 6

    if marble.colliderect(coin) and score != 2:
        coin.x = random.randint(150, 450)
        coin.y = random.randint(45, 500)
        score += 1
        coinscore += 1

    if game_state == 3:
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
    global game_state
    center_column = get_height(marbleh.x, marbleh.y)
    left_column = get_height(marbleh.x - 10, marbleh.y + 10)
    right_column = get_height(marbleh.x + 10, marbleh.y + 10)

    if center_column.r == 0:
        game_state = 6

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
        game_state = 11

# def on_key_down(key):
    # print(key)

def on_mouse_down(pos, button):
    global game_state
    # print(button)
    # wenn man im Menü auf Enter drückt landet man im Startbildschirm
    if game_state == 1 and btn_quit.collidepoint(pos) and mouse.LEFT:
        game_state = 0
    # wenn man im Menü auf Start drückt landet man im ersten Level
    elif game_state == 1 and btn_start.collidepoint(pos) and mouse.LEFT:
        game_state = 3
    # wenn man im GameOver Bildschirm ist
    elif game_state == 6:
        # marble und marbleh in die Anfangsposition und Speed auf 0 setzen
        marble.pos = 300, 45
        marbleh.pos = 300, 60
        marble.speed = 0
        marbleh.speed = 0
        # wenn man im GameOver Bildschirm auf den Play Button drückt landet man im ersten Level
        if btn_play.collidepoint(pos):
            game_state = 3
        # wenn man im GameOver Bildschirm auf Quit drückt landet man im Startbildschirm
        elif btn_quit.collidepoint(pos):
            game_state = 0

def get_height(x, y):
    return heightmap.get_at((int(x), int(y)))


surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
#screen = Screen(surface=surf)
# pgzrun.mod.screen.
pgzrun.go()
