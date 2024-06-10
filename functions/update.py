import random
from time import sleep

import pygame
from pgzero import music
from pgzero.builtins import keyboard

from constants import state
from enumerations.button import Button
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.process_input import process_input
from functions.backend.add_scores_during_game_play import add_scores_during_game_play
from functions.backend.animate_coin import animate_coin
from functions.backend.check_collision import check_collision_with_flag
from functions.backend.handle_button_selection import handle_button_selection
from functions.backend.increment_level import increment_level
from functions.backend.load_level_data import load_level_data
from functions.backend.move_marble import move_marble
from functions.backend.update_coin import handle_coin_collision, update_coin_position
from functions.backend.update_enemy import handle_enemy_collision, update_enemy_position
from functions.backend.update_marble_position import update_marble_position


def update():
    process_input()

    if state.start_game:
        load_level_data()
        state.start_game = False

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
        load_level_data()
        state.selected_button = Button.PLAY
        sleep(0.2)  # todo update sleep

    # vom Menü in den Countdown oder zurück zur Startseite
    elif state.game_state == GameState.MENU_PAGE:
        handle_button_selection()

    # vom Countdown zum Level spielen
    elif state.game_state == GameState.COUNTDOWN:
        if int(state.countdown_timer) <= 0:
            state.game_state = GameState.LEVEL_GAME
            state.wait_counter_for_score_display = 10  # todo maybe in load level files or so
            sleep(0.2)

        else:
            state.countdown_timer -= 5
            sleep(0.2)

    # Timer-Update während eines Levels, von hier entweder WIN oder GAME_OVER
    elif state.game_state == GameState.LEVEL_GAME:

        state.timer -= 1 / 60
        add_scores_during_game_play()
        state.wait_counter_for_score_display = 10  # todo set when win or game over?

        # timer over
        if state.timer <= 0:
            state.game_state = GameState.GAME_OVER
            state.game_over_state = GameOverState.TIMER_UP

        # timer still running
        else:
            if state.coin and state.marble.colliderect(state.coin) and state.score != 2:
                state.coin.x = random.randint(150, 450)
                state.coin.y = random.randint(45, 500)
                state.coin_score += 250

            update_marble_position()
            move_marble()
            state.marble.speed = max(0, state.marble.speed - 0.01)

            if state.enemy:
                handle_enemy_collision()
                update_enemy_position()

            if state.coin:
                handle_coin_collision()
                update_coin_position()
                animate_coin()

            if check_collision_with_flag(state.marble, state.flag):
                state.game_state = GameState.LEVEL_WIN
                state.sounds.enemysound.set_volume(0.1)

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
            handle_button_selection()

    # vom verlorenen Level das Level wiederholen oder Spiel beenden
    elif state.game_state == GameState.GAME_OVER:
        state.blue_text = not state.blue_text

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
            handle_button_selection()

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
    state.wait_counter_for_game_over = 10
    state.score_for_current_level = 0
    state.deducted_score_for_lost_level = False


def quit_game():
    state.game_state = GameState.START_PAGE
    state.current_level = LevelState.LEVEL_ONE

    state.start_game = True

    state.previous_timer_value = 0

    state.blue_text = False
    state.wait_counter_for_score_display = 10
    state.wait_counter_for_game_over = 10

    state.not_added_points_and_incremented = True

    state.timer = 0
    state.score = 0
    state.coin_score = 0

    state.score_for_current_level = 0
    state.deducted_score_for_lost_level = False

    state.display_coin_score = 0
    state.display_timer_score = 0

    state.countdown_timer = 0

    sleep(0.2)
