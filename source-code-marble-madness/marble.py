import pgzrun
from pgzero.game import screen
from pgzero.screen import Screen
import pygame
from pygame import image, Surface
from pgzero.builtins import keyboard, Actor, mouse
import random
import math

#joystick = pygame.joystick.Joystick(0)
#joystick.init()


HEIGHT = 570
WIDTH = 600

game_state = 0
curr_level = 0

btn_start = Actor('btn_start', center=(300, 300))
btn_quit = Actor('btn_quit', center=(300, 400))
btn_back = Actor('btn_back', center=(300, 400))
btn_play = Actor('btn_play')

marble = Actor('marble', center=(300, 45))
marbleh = Actor('marble', center=(300, 60))
marble.dir = marble.speed = 0
heightmap = image.load('images/height45.png')
debug = False
timer = 30
score = 0
coinscore = 0



coin_images = ['coinpos1', 'coinpos2', 'coinpos3', 'coinpos4']
coin = Actor(coin_images[0])
coin.x = (150)
coin.y = (45)
coin_frame = 0
coin_animation_counter = 0
coin_animation_interval = 10

flag = Actor('blueflag')
flag.x = 248
flag.y = 500

enemy = Actor('shurikensml')
enemy.x = (130)
enemy.y = (170)

target_positions = [(200, 130), (250, 160), (180, 200), (130, 170)]
target_index = 0
enemyspeed = 1

timerlevel1 = 60

# Initialize angle for shuriken rotation
shuriken_angle = 0

def draw():
    global game_state
    global curr_level
    if debug:
        screen.blit("height45", (0, 0))
        marbleh.draw()
    else:
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
            enemy.draw()
            flag.draw()
            if coinscore != 6:
                coin.draw()
            marble.draw()
            curr_level = 1
        elif game_state == 4:
            print("level 2")
        elif game_state == 5:
            print("level 3")
        elif game_state == 6:
            screen.fill((0, 0, 0))
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

def update():
    global timer, game_state, score, coinscore, enemy, target_index, shuriken_angle, coin_frame, coin_animation_counter

    # Handle music based on game state
    if game_state == 3:
        if not music.is_playing('level1music'):
            music.play('level1music')
        music.set_volume(0.1)
    else:
        music.stop()

    # Get the current target position
    target_x, target_y = target_positions[target_index]
    # Calculate the distance between the enemy and the target position
    distance_x = target_x - enemy.x
    distance_y = target_y - enemy.y

    shuriken_angle += 5
    if shuriken_angle >= 360:
        shuriken_angle = 0
    enemy.angle = shuriken_angle

    # Move the enemy towards the target position
    if abs(distance_x) > enemyspeed:
        enemy.x += enemyspeed if distance_x > 0 else -enemyspeed
    else:
        enemy.x = target_x

    if abs(distance_y) > enemyspeed:
        enemy.y += enemyspeed if distance_y > 0 else -enemyspeed
    else:
        enemy.y = target_y

    # Check if the enemy has reached the current target position
    if enemy.x == target_x and enemy.y == target_y:
        # Move to the next target position
        target_index = (target_index + 1) % len(target_positions)

    if check_collision_with_shuriken(marble, enemy):
        game_state = 6
        sounds.enemysound.set_volume(0.1)
        sounds.enemysound.play()

    if check_collision_with_flag(marble, flag):
        game_state = 11
        sounds.enemysound.set_volume(0.1)


    if game_state == 3:
        timer -= 1 / 60
    else:
        timer = timerlevel1

    if timer <= 0:
        game_state = 6

    sounds.sfx_coin_single1.set_volume(0.1)
    if marble.colliderect(coin) and score == 0:
        coin.x = 60
        coin.y = 130
        score += 1
        coinscore += 1
        sounds.sfx_coin_single1.play()
    elif marble.colliderect(coin) and score == 1:
        coin.x = 160
        coin.y = 45
        score += 1
        coinscore += 1
        sounds.sfx_coin_single1.play()
    elif marble.colliderect(coin) and score == 2:
        coin.x = 300
        coin.y = 360
        score += 1
        coinscore += 1
        sounds.sfx_coin_single1.play()
    elif marble.colliderect(coin) and score == 3:
        coin.x = 360
        coin.y = 200
        score += 1
        coinscore += 1
        sounds.sfx_coin_single1.play()
    elif marble.colliderect(coin) and score == 4:
        coin.x = 240
        coin.y = 520
        score += 1
        coinscore += 1
        sounds.sfx_coin_single1.play()
    elif marble.colliderect(coin) and score == 5:
        score += 1
        coinscore += 1
        sounds.sfx_coin_single1.play()

    if game_state == 3:
        if keyboard.left: #or joystick.get_axis(0) < -0.1:
            marble.dir = max(marble.dir - 0.1, -1)
            marble.speed = min(1, marble.speed + 0.1)
        if keyboard.right: #or joystick.get_axis(0) > 0.1:
            marble.dir = min(marble.dir + 0.1, 1)
            marble.speed = min(1, marble.speed + 0.1)
        if keyboard.up: #or joystick.get_axis(1) < 0.1:
            marbleh.y -= 2.5
            marble.speed = min(1, marble.speed + 0.1)
        if keyboard.down: #or joystick.get_axis(1) < -0.1:
            marbleh.y += 1.5
            marble.speed = min(1, marble.speed + 0.1)
        move_marble()
        marble.speed = max(0, marble.speed - 0.01)
    # Damit man vom Startbildschirm ins Menü kommt
    elif game_state == 0 and keyboard.RETURN:
        game_state = 1
    elif game_state == 11 and keyboard.RETURN:
        game_state = 1
        marble.pos = 300, 45
        marbleh.pos = 300, 60

    # Update coin animation
    coin_animation_counter += 1
    if coin_animation_counter >= coin_animation_interval:
        coin_frame = (coin_frame + 1) % len(coin_images)
        coin.image = coin_images[coin_frame]
        coin_animation_counter = 0

def move_marble():
    global game_state
    center_column = get_height(marbleh.x, marbleh.y)
    left_column = get_height(marbleh.x - 10, marbleh.y + 10)
    right_column = get_height(marbleh.x + 10, marbleh.y + 10)

    if center_column.r == 0:
        game_state = 6

    if left_column.r < center_column.r or right_column.r < center_column.r:
        marble.y += marble.speed
        marble.speed += 0.02

    marbleh.x += marble.speed * marble.dir
    marbleh.y += marble.speed
    marble.x = marbleh.x
    marble.y = (marbleh.y * 0.6) + ((255 - center_column.r) * 1.25)
    marble.angle = marble.angle + marble.speed * marble.dir * -10

    if marble.angle > 0:
        marble.angle = -50
    elif marble.angle < -50:
        marble.angle = 0


def on_mouse_down(pos, button):
    global game_state
    # Wenn man im Menü auf Enter drückt, landet man im Startbildschirm
    if game_state == 1 and btn_quit.collidepoint(pos) and mouse.LEFT:
        game_state = 0
    # Wenn man im Menü auf Start drückt, landet man im ersten Level
    elif game_state == 1 and btn_start.collidepoint(pos) and mouse.LEFT:
        game_state = 3
    # Wenn man im GameOver Bildschirm ist
    elif game_state == 6:
        # Marble und marbleh in die Anfangsposition und Speed auf 0 setzen
        marble.pos = 300, 45
        marbleh.pos = 300, 60
        marble.speed = 0
        marbleh.speed = 0
        # Wenn man im GameOver Bildschirm auf den Play Button drückt, landet man im ersten Level
        if btn_play.collidepoint(pos):
            game_state = 3
        # Wenn man im GameOver Bildschirm auf Quit drückt, landet man im Startbildschirm
        elif btn_quit.collidepoint(pos):
            game_state = 0

def get_height(x, y):
    return heightmap.get_at((int(x), int(y)))

def check_collision_with_shuriken(marble, shuriken):
    # Define a smaller rectangle for the shuriken
    shuriken_hitbox = Rect(shuriken.x - shuriken.width / 4, shuriken.y - shuriken.height / 4, shuriken.width / 2, shuriken.height / 2)
    return marble.colliderect(shuriken_hitbox)

def check_collision_with_flag(marble, flag):
    # Define a smaller rectangle for the shuriken
    flag_hitbox = Rect(flag.x - flag.width / 50, flag.y - flag.height / 50, flag.width / 50, flag.height / 50)
    return marble.colliderect(flag_hitbox)

surf = Surface(size=[WIDTH, HEIGHT])
pgzrun.mod.screen = Screen(surface=surf)

pgzrun.go()
