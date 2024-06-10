import pgzrun
import pygame
from pygame import image
from pgzero.builtins import Actor, keyboard, music, sounds

# Initialize window size
HEIGHT = 570
WIDTH = 600

game_state = 0
curr_level = 0

btn_start = Actor('btn_start', center=(300, 300))
btn_quit = Actor('btn_quit', center=(300, 400))
btn_back = Actor('btn_back', center=(300, 400))
btn_play = Actor('btn_play')

marble = Actor('marble_still1', center=(300, 45))
marbleh = Actor('marble_still1', center=(300, 60))
marble.dir = marble.speed = 0

# Load the 3D map as an actor
map3d = Actor('map3d', topleft=(0, 0))

debug = False
timer = 30
score = 0
coinscore = 0

coin_images = ['coinpos1', 'coinpos2', 'coinpos3', 'coinpos4']
coin = Actor(coin_images[0])
coin.x = 150
coin.y = 45
coin_frame = 0
coin_animation_counter = 0
coin_animation_interval = 10

flag = Actor('blueflag')
flag.x = 248
flag.y = 500

enemy = Actor('shurikensml')
enemy.x = 130
enemy.y = 170

target_positions = [(200, 130), (250, 160), (180, 200), (130, 170)]
target_index = 0
enemyspeed = 1

timerlevel1 = 60

# Initialize angle for shuriken rotation
shuriken_angle = 0

# Load animation frames for each direction
marble_still_frames = ['marble_still1']  # Add the still images if you have more
marble_right_frames = ['marble_right1', 'marble_right2', 'marble_right3', 'marble_right4', 'marble_right5']
marble_bottom_right_frames = ['marble_bottom_right1', 'marble_bottom_right2', 'marble_bottom_right3', 'marble_bottom_right4', 'marble_bottom_right5', 'marble_bottom_right6', 'marble_bottom_right7']
marble_bottom_frames = ['marble_bottom1', 'marble_bottom2', 'marble_bottom3', 'marble_bottom4', 'marble_bottom5']
marble_bottom_left_frames = ['marble_bottom_left1', 'marble_bottom_left2', 'marble_bottom_left3', 'marble_bottom_left4', 'marble_bottom_left5', 'marble_bottom_left6', 'marble_bottom_left7']
marble_left_frames = ['marble_left1', 'marble_left2', 'marble_left3', 'marble_left4', 'marble_left5']

# Initialize animation variables
marble_animation_counter = 0
marble_animation_interval = 6
marble_frame = 0
current_direction = 'still'

def draw():
    global game_state
    global curr_level
    if debug:
        map3d.draw()
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
            screen.draw.text('Time: ' + str(round(timer, 2)), (10, 10), color=(255, 255, 255), fontsize=30)
            screen.draw.text('Score: ' + str(score), (500, 10), color=(255, 255, 255), fontsize=30)
            map3d.draw()
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
            screen.draw.text("YOU WIN!", center=(300, 300), owidth=0.5, ocolor=(255, 255, 255), color=(0, 0, 255), fontsize=80)
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
        coin.y = 400
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
        if keyboard.down: #or joystick.get_axis(1) > 0.1:
            marbleh.y += 2.5
            marble.speed = min(1, marble.speed + 0.1)

    move_marble()
    marble.speed = max(0, marble.speed - 0.026)
    animate_coin()

def on_key_down(key):
    global game_state
    if key == keys.RETURN:
        if game_state == 0:
            game_state = 1
        elif game_state == 11:
            game_state = 0
        elif game_state == 6:
            game_state = 1

def on_mouse_down(pos):
    global game_state
    if game_state == 1:
        if btn_start.collidepoint(pos):
            game_state = 3
        if btn_quit.collidepoint(pos):
            quit()
    elif game_state == 6:
        if btn_play.collidepoint(pos):
            game_state = 3
        elif btn_quit.collidepoint(pos):
            quit()

def move_marble():
    global game_state, marble_frame, marble_animation_counter, current_direction

    if marbleh.x < 0 or marbleh.x > WIDTH or marbleh.y < 0 or marbleh.y > HEIGHT:
        game_state = 6

    marbleh.x += marble.speed * marble.dir
    marbleh.y += marble.speed
    marble.x = marbleh.x
    marble.y = marbleh.y

    update_marble_animation()

def update_marble_animation():
    global marble_frame, marble_animation_counter, current_direction

    # Determine the direction
    if marble.speed > 0:
        if marble.dir > 0.5:
            new_direction = 'right'
        elif marble.dir < -0.5:
            new_direction = 'left'  # Add frames for left if needed
        else:
            new_direction = 'bottom_right'
    else:
        new_direction = 'still'

    # If direction changes, reset the frame counter
    if new_direction != current_direction:
        current_direction = new_direction
        marble_frame = 0

    marble_animation_counter += 1
    if marble_animation_counter >= marble_animation_interval:
        marble_animation_counter = 0

        if current_direction == 'still':
            marble.image = marble_still_frames[0]
        elif current_direction == 'right':
            marble.image = marble_right_frames[marble_frame % len(marble_right_frames)]
        elif current_direction == 'left':
            marble.image = marble_left_frames[marble_frame % len(marble_left_frames)]
        elif current_direction == 'bottom_right':
            marble.image = marble_bottom_right_frames[marble_frame % len(marble_bottom_right_frames)]
        elif current_direction == 'bottom_left':
            marble.image = marble_bottom_left_frames[marble_frame % len(marble_bottom_left_frames)]
        elif current_direction == 'bottom':
            marble.image = marble_bottom_frames[marble_frame % len(marble_bottom_frames)]

        marble_frame += 1

def animate_coin():
    global coin_frame, coin_animation_counter
    coin_animation_counter += 1
    if coin_animation_counter >= coin_animation_interval:
        coin_animation_counter = 0
        coin.image = coin_images[coin_frame % len(coin_images)]
        coin_frame += 1

def check_collision_with_shuriken(marble, shuriken):
    # Define a smaller rectangle for the shuriken
    shuriken_hitbox = Rect(shuriken.x - shuriken.width / 4, shuriken.y - shuriken.height / 4, shuriken.width / 2, shuriken.height / 2)
    return marble.colliderect(shuriken_hitbox)

def check_collision_with_flag(marble, flag):
    # Define a smaller rectangle for the flag
    flag_hitbox = Rect(flag.x - flag.width / 60, flag.y - flag.height / 60, flag.width / 60, flag.height / 60)
    return marble.colliderect(flag_hitbox)

pgzrun.go()
