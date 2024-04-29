# Marble Madness
import pgzrun
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import image, Surface
from pgzero.builtins import keyboard, Actor
import pgzero.screen
import random


HEIGHT = 570
WIDTH = 600

game_state = 0
marble = Actor('marble', center=(300, 45))
marbleh = Actor('marble', center=(300, 60))
marble.dir = marble.speed = 0
heightmap = image.load('images/height45.png')
debug = False
timer = 30
score = 0
coin = Actor('coingold')
coin.x = (150)
coin.y = (45)


def draw():
    if (debug):
        screen.blit("height45", (0, 0))
        marbleh.draw()
    else:
        screen.blit("map", (0, 0))
        if game_state == 0:
            screen.draw.text('Time: ' + str(round(timer, 2)), (10,10), color=(255,255,255), fontsize=30)
            screen.draw.text('Score: ' + str(score), (500,10), color=(255,255,255), fontsize=30)
            coin.draw()
            marble.draw()
        else:
            if game_state == 2:
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                marble.draw()
            elif game_state == 3:
                screen.draw.text("GAME OVER!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
            else:
                screen.draw.text("GAME OVER!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
        screen.blit("overlay", (0, 0))


def update():
    global timer, game_state, score

    timer -= 1 / 60
    if timer <= 0:
        game_state = 3

    if marble.colliderect(coin):
        coin.x = random.randint(150, 450)
        coin.y = random.randint(45, 500)
        score += 1

    if game_state == 0:
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


def move_marble():
    global game_state
    center_column = get_height(marbleh.x, marbleh.y)
    left_column = get_height(marbleh.x - 10, marbleh.y + 10)
    right_column = get_height(marbleh.x + 10, marbleh.y + 10)

    if center_column.r == 0:
        game_state = 1

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

    if marbleh.y > 610:
        game_state = 2


def get_height(x, y):
    return heightmap.get_at((int(x), int(y)))


surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)
pgzrun.go()
