import random
from time import sleep

from pgzero.builtins import keyboard

from constants import state
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.backend.increment_level import increment_level
from functions.backend.load_level_files import load_level_files
from functions.move_marble import move_marble


def update():
    if not state.start_timer and keyboard.left or keyboard.right or keyboard.up or keyboard.down:
        state.start_timer = True

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
                state.marble_moved_once = True

            if keyboard.right or state.joystick is not None and state.joystick.get_axis(0) > 0.1:
                state.marble.dir = min(state.marble.dir + 1, 1)
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True

            if keyboard.up or state.joystick is not None and state.joystick.get_axis(1) < 0.1:
                state.marbleh.y -= 2
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True

            if keyboard.down or state.joystick is not None and state.joystick.get_axis(1) < -0.1:
                state.marbleh.y += 1.5
                state.marble.speed = min(1, state.marble.speed + 0.1)
                state.marble_moved_once = True


            move_marble()
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
