# Marble Madness
import pgzrun
import pygame
from pgzero.game import screen
from pgzero.screen import Screen
from pygame import image, Surface, HWSURFACE, DOUBLEBUF, RESIZABLE
from pgzero.builtins import keyboard, Actor
import pgzero.screen
import random


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
debug = False
timer = 30
score = 0
coinscore = 0
coin = Actor('objects/coingold')
coin.x = (150)
coin.y = (45)


def draw():
    if (debug):
        screen.blit(level_one_heightmap_short, (0, 0))
        marbleh.draw()
    else:
        screen.blit(level_one_short, (0, 0))
        if game_state == 0:
            screen.draw.text('Time: ' + str(round(timer, 2)), (10,10), color=(255,255,255), fontsize=30)
            screen.draw.text('Score: ' + str(score), (500,10), color=(255,255,255), fontsize=30)
            marble.draw()
            if coinscore != 2 :
                coin.draw()
        else:
            if game_state == 2:
                screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)

                marble.draw()
            elif game_state == 3:
                screen.draw.text("GAME OVER!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500,10), color=(255,255,255), fontsize=30)
            else:
                screen.draw.text("GAME OVER!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255),
                                 fontsize=80)
                screen.draw.text('Score: ' + str(score), (500,10), color=(255,255,255), fontsize=30)

        # screen.blit("objects/overlay", (0, 0))
        screen.blit("objects/overlay", (365, 150))


def update():
    global timer, game_state, score, coinscore

    timer -= 1 / 60
    if timer <= 0:
        game_state = 3

    if marble.colliderect(coin) and score != 2:
        coin.x = random.randint(150, 450)
        coin.y = random.randint(45, 500)
        score += 1
        coinscore += 1

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
#screen = Screen(surface=surf)
# pgzrun.mod.screen.
pgzrun.go()
