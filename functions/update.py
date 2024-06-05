import random
from time import sleep

from pgzero import music
from pgzero.builtins import keyboard

from constants import state, game_constants
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.backend.check_collision import check_collision_with_shuriken, check_collision_with_flag
from functions.backend.increment_level import increment_level
from functions.backend.load_level_files import load_level_files
from functions.backend.move_marble import move_marble
from functions.frontend.animate_coin import animate_coin


def update():
    if not state.start_timer and keyboard.left or keyboard.right or keyboard.up or keyboard.down:
        state.start_timer = True

    # Handle music based on game state   # TODO: depending on state ? or just always playing
    if state.game_state in [GameState.COUNTDOWN, GameState.LEVEL_GAME, GameState.LEVEL_WIN, GameState.GAME_OVER]:
        if not music.is_playing('level1music'):
            music.play('level1music')
        music.set_volume(0.1)
    else:
        music.stop()

    # vom Startbildschirm ins Menü
    if state.game_state == GameState.START_PAGE and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE
        load_level_files()
        state.play_game_color = 'orange'
        state.quit_color = 'white'
        sleep(0.2)

    # vom Menü in den Countdown oder zurück zur Startseite
    elif state.game_state == GameState.MENU_PAGE:
        if state.play_game_color == 'orange':
            if keyboard.down:
                state.quit_color = 'orange'
                state.play_game_color = 'white'

            elif keyboard.RETURN:
                state.game_state = GameState.COUNTDOWN
                state.countdown_timer = state.timer
                state.printed_timer = False

        elif state.quit_color == 'orange':
            if keyboard.up:
                state.play_game_color = 'orange'
                state.quit_color = 'white'

            elif keyboard.RETURN:
                quit_game()

    # vom Countdown zum Level spielen
    elif state.game_state == GameState.COUNTDOWN:
        if int(state.countdown_timer) == 0:
            state.game_state = GameState.LEVEL_GAME
            state.wait_counter_for_score_display = 10
            sleep(0.2)

        elif state.printed_timer:
            state.countdown_timer -= 5
            sleep(0.2)

    # Timer-Update während eines Levels, von hier entweder WIN oder GAME_OVER
    elif state.game_state == GameState.LEVEL_GAME:  # and state.start_timer:
        state.sounds.sfx_coin_single1.set_volume(0.1)
        state.sounds.sfx_coin_single1.play()
        # if marble.colliderect(coin) and score == 0:  # todo: save positions in game constants and modularize
        #     coin.x = 60
        #     coin.y = 130
        #     score += 1
        #     coinscore += 1
        #     sounds.sfx_coin_single1.play()
        # elif marble.colliderect(coin) and score == 1:
        #     coin.x = 160
        #     coin.y = 45
        #     score += 1
        #     coinscore += 1
        #     sounds.sfx_coin_single1.play()
        # elif marble.colliderect(coin) and score == 2:
        #     coin.x = 300
        #     coin.y = 360
        #     score += 1
        #     coinscore += 1
        #     sounds.sfx_coin_single1.play()
        # elif marble.colliderect(coin) and score == 3:
        #     coin.x = 360
        #     coin.y = 200
        #     score += 1
        #     coinscore += 1
        #     sounds.sfx_coin_single1.play()
        # elif marble.colliderect(coin) and score == 4:
        #     coin.x = 240
        #     coin.y = 520
        #     score += 1
        #     coinscore += 1
        #     sounds.sfx_coin_single1.play()
        # elif marble.colliderect(coin) and score == 5:
        #     score += 1
        #     coinscore += 1
        #     sounds.sfx_coin_single1.play()
        # Get the current target position
        target_x, target_y = game_constants.enemy_positions[state.enemy_index]
        # Calculate the distance between the enemy and the target position
        distance_x = target_x - state.enemy.x
        distance_y = target_y - state.enemy.y

        state.enemy_angle += 5
        if state.enemy_angle >= 360:
            state.enemy.angle = 0

        # Move the enemy towards the target position
        if abs(distance_x) > state.enemy_speed:
            state.enemy.x += state.enemy_speed if distance_x > 0 else -state.enemy_speed
        else:
            state.enemy.x = target_x

        if abs(distance_y) > state.enemy_speed:
            state.enemy.y += state.enemy_speed if distance_y > 0 else -state.enemy_speed
        else:
            state.enemy.y = target_y

        # Check if the enemy has reached the current target position
        if state.enemy.x == target_x and state.enemy.y == target_y:
            # Move to the next target position
            state.target_index = (state.enemy_index + 1) % len(game_constants.enemy_positions)

        if check_collision_with_shuriken(state.marble, state.enemy):
            state.game_state = GameState.GAME_OVER
            state.game_over_state = GameOverState.ENEMY_HIT
            state.sounds.enemysound.set_volume(0.1)
            state.sounds.enemysound.play()

        if check_collision_with_flag(state.marble, state.flag):
            state.game_state = GameState.LEVEL_WIN
            state.sounds.enemysound.set_volume(0.1)

        state.timer -= 1 / 60
        state.wait_counter_for_score_display = 10

        if state.previous_clock_time == 0:
            state.previous_clock_time = round(state.timer, 2)

        if round(state.timer, 2) < state.previous_clock_time - 0.2 and state.previous_clock_time != 0:
            state.score += 10
            state.score_for_current_level += 10
            state.previous_clock_time = round(state.timer, 2)

        if state.timer <= 0:
            state.game_state = GameState.GAME_OVER
            state.game_over_state = GameOverState.TIMER_UP
        else:
            if state.marble.colliderect(state.coin) and state.score != 2:
                state.coin.x = random.randint(150, 450)
                state.coin.y = random.randint(45, 500)
                state.coin_score += 250

            if keyboard.left or state.joystick is not None and state.joystick.get_axis(0) < -0.1:
                state.marble.dir = max(state.marble.dir - 1, -1)
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True  # todo: still needed??

            if keyboard.right or state.joystick is not None and state.joystick.get_axis(0) > 0.1:
                state.marble.dir = min(state.marble.dir + 1, 1)
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True

            if keyboard.up or state.joystick is not None and state.joystick.get_axis(1) < 0.1:
                state.marbleh.y -= 2  # todo: change how fast? > 2,5
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True

            if keyboard.down or state.joystick is not None and state.joystick.get_axis(1) < -0.1:
                state.marbleh.y += 1.5  # todo: change how fast? > 2,5
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True

            move_marble()
            animate_coin()
            state.marble.speed = max(0, state.marble.speed - 0.01)

    # vom gewonnen Level zum nächsten oder Spiel beenden
    elif state.game_state == GameState.LEVEL_WIN:
        if state.not_added_points_and_incremented:
            add_points_for_remaining_time()
            increment_level()
            state.not_added_points_and_incremented = False

        if state.wait_counter_for_score_display != 0:
            state.wait_counter_for_score_display -= 1
            sleep(0.2)
        else:
            if state.play_game_color == 'orange':
                if keyboard.down:
                    state.quit_color = 'orange'
                    state.play_game_color = 'white'

                elif keyboard.RETURN:
                    state.game_state = GameState.COUNTDOWN
                    load_level_files()
                    state.countdown_timer = state.timer
                    state.printed_timer = False

            elif state.quit_color == 'orange':
                if keyboard.up:
                    state.play_game_color = 'orange'
                    state.quit_color = 'white'

                elif keyboard.RETURN:
                    quit_game()

    # vom verlorenen Level das Level wiederholen oder Spiel beenden
    elif state.game_state == GameState.GAME_OVER:
        if not state.deducted_score_for_lost_level:
            state.score = state.score - state.score_for_current_level
            if state.score < 0:
                state.score = 0
            state.deducted_score_for_lost_level = True

        if state.wait_counter_for_game_over != 0:
            state.wait_counter_for_game_over -= 1
            sleep(0.2)
            if state.wait_counter_for_game_over == 0:
                sleep(0.5)
        else:
            if state.play_game_color == 'orange':
                if keyboard.down:
                    state.quit_color = 'orange'
                    state.play_game_color = 'white'

                elif keyboard.RETURN:
                    state.game_state = GameState.COUNTDOWN
                    load_level_files()
                    reset_state()

            elif state.quit_color == 'orange':
                if keyboard.up:
                    state.play_game_color = 'orange'
                    state.quit_color = 'white'

                elif keyboard.RETURN:
                    quit_game()

    # vom gewonnen Spiel zurück zur Startseite
    elif state.game_state == GameState.GAME_WIN and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE
        quit_game()


def add_points_for_remaining_time():
    timer_score = int(state.timer) * 100
    state.score += timer_score
    state.display_timer_score = timer_score

    state.score += state.coin_score
    state.display_coin_score = state.coin_score
    state.coin_score = 0

    state.score_for_current_level = 0


def reset_state():
    state.countdown_timer = state.timer
    state.printed_timer = False
    state.wait_counter_for_game_over = 10
    state.score_for_current_level = 0
    state.deducted_score_for_lost_level = False


def quit_game():
    state.game_state = GameState.START_PAGE
    state.current_level = LevelState.LEVEL_ONE

    state.start_game = True

    state.play_game_color = 'orange'
    state.quit_color = 'white'

    state.previous_clock_time = 0

    state.colorful = False
    state.wait_counter_for_score_display = 10
    state.wait_counter_for_game_over = 10

    state.start_timer = False
    state.not_added_points_and_incremented = True

    state.timer = 0
    state.score = 0
    state.coin_score = 0

    state.score_for_current_level = 0
    state.deducted_score_for_lost_level = False

    state.display_coin_score = 0
    state.display_timer_score = 0

    state.printed_timer = False
    state.countdown_timer = 0

    sleep(0.2)
