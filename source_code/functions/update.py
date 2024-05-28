import random
from time import sleep

from pgzero.builtins import keyboard

from source_code.constants import state
from source_code.enumerations.game_state import GameState
from source_code.enumerations.level_state import LevelState
from source_code.functions.backend.increment_level import increment_level
from source_code.functions.backend.load_level_files import load_level_files
from source_code.functions.move_marble import move_marble


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
            state.wait_counter = 10
            sleep(0.2)

        elif state.printed_timer:
            state.countdown_timer -= 5  # todo: should be in update
            sleep(0.2)

    # Timer-Update während eines Levels, von hier entweder WIN oder GAME_OVER
    elif state.game_state == GameState.LEVEL_GAME:  # and state.start_timer:
        state.timer -= 1 / 60
        state.wait_counter = 10

        if state.previous_clock_time == 0:
            state.previous_clock_time = round(state.timer, 2)

        if round(state.timer, 2) < state.previous_clock_time - 0.2 and state.previous_clock_time != 0:
            state.score += 10
            state.previous_clock_time = round(state.timer, 2)

        if state.timer <= 0:
            state.game_state = GameState.GAME_OVER
        else:
            if state.marble.colliderect(state.coin) and state.score != 2:
                state.coin.x = random.randint(150, 450)
                state.coin.y = random.randint(45, 500)
                state.coin_score += 250

            if keyboard.left:
                state.marble.dir = max(state.marble.dir - 1, -1)
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.right:
                state.marble.dir = min(state.marble.dir + 1, 1)
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.up:
                state.marbleh.y -= 2
                state.marble.speed = min(1, state.marble.speed + 0.1)

            if keyboard.down:
                state.marbleh.y += 1.5
                state.marble.speed = min(1, state.marble.speed + 0.1)

            move_marble()
            state.marble.speed = max(0, state.marble.speed - 0.01)

    # vom gewonnen Level zum nächsten oder Spiel beenden
    elif state.game_state == GameState.LEVEL_WIN:
        if state.not_added_points_and_incremented:
            add_points_for_remaining_time()
            increment_level()
            state.not_added_points_and_incremented = False

        if state.wait_counter != 0:
            state.wait_counter -= 1
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
    # todo

    # vom gewonnen Spiel zurück zur Startseite
    elif state.game_state == GameState.GAME_WIN and keyboard.RETURN:
        state.game_state = GameState.MENU_PAGE
        state.current_level = LevelState.LEVEL_ONE
        state.marble.pos = 300, 45  # todo: wanted like this? or position of level 1
        state.marbleh.pos = 300, 60


def add_points_for_remaining_time():
    timer_score = int(state.timer) * 100
    state.score += timer_score
    state.display_timer_score = timer_score

    state.score += state.coin_score
    state.display_coin_score = state.coin_score
    state.coin_score = 0


def quit_game():
    state.game_state = GameState.START_PAGE
    state.current_level = LevelState.LEVEL_ONE
    load_level_files()
    state.score = 0
    state.coin_score = 0
    state.display_score = 0
    state.display_timer_score = 0
    state.play_game_color = 'orange'
    state.quit_color = 'white'
    sleep(0.2)
