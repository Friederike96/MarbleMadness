from constants import state, game_constants
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.backend.update_marble_animation import update_marble_animation


def move_marble():
    if state.game_state != GameState.LEVEL_GAME or not state.marble_moved_once:
        return

    center_column = get_height(state.marbleh.x, state.marbleh.y)
    left_column = get_height(state.marbleh.x - 10, state.marbleh.y + 10)
    right_column = get_height(state.marbleh.x + 10, state.marbleh.y + 10)

    if center_column is None or left_column is None or right_column is None:  # or center_column.r == 0:
        state.game_state = GameState.GAME_OVER  # reminder: change back
        state.game_over_state = GameOverState.FALL_OVER_EDGE
        return

    if left_column.r < center_column.r or right_column.r < center_column.r:
        state.marble.y += state.marble.speed
        state.marble.speed += 0.03

    state.marbleh.x += state.marble.speed * state.marble.dir
    state.marbleh.y += state.marble.speed
    state.marble.x = state.marbleh.x
    updated_marble_y = (state.marbleh.y * 0.6) + ((255 - center_column.r) * 1.25)
    if updated_marble_y < state.marble.y + 200:# or (state.level_timer - state.timer) >= 2:
        state.marble.y = updated_marble_y
    state.marble.angle = state.marble.angle + state.marble.speed * state.marble.dir * -10

    if state.marble.angle > 0:
        state.marble.angle = 0
    elif state.marble.angle < 0:
        state.marble.angle = 0

    # Abfrage ob man im Ziel ist
    if state.marbleh.y > 700:  # todo: level abhängig, auch von x abhängig?
        if state.current_level == LevelState.LEVEL_FOUR:
            state.game_state = GameState.GAME_WIN
        else:
            state.game_state = GameState.LEVEL_WIN
            state.not_added_points_and_incremented = True

    update_marble_animation()


# def on_key_down(key):
# print(key)


def get_height(x, y):
    # if x < 0:
    #     x = 0
    # elif x > WIDTH - 1:
    #     x = WIDTH - 1
    # if y < 0:
    #     y = 0
    # elif y > HEIGHT - 1:
    #     y = HEIGHT - 1
    if x > game_constants.WIDTH:
        x = game_constants.WIDTH
    if y > game_constants.HEIGHT:
        y = game_constants.HEIGHT
    try:
        return state.heightmap.get_at((int(x), int(y)))
    except IndexError as e:
        print(e)
