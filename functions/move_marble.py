from constants import state, game_constants
from enumerations.game_state import GameState
from enumerations.level_state import LevelState


def move_marble():
    if state.game_state != GameState.LEVEL_GAME:
        return

    center_column = get_height(state.marbleh.x, state.marbleh.y)
    left_column = get_height(state.marbleh.x - 10, state.marbleh.y + 10)
    right_column = get_height(state.marbleh.x + 10, state.marbleh.y + 10)

    if center_column is None:  # or center_column.r == 0:
        state.game_state = GameState.GAME_OVER  # reminder: change back
        return

    if left_column.r < center_column.r or right_column.r < center_column.r:
        state.marble.y += state.marble.speed
        state.marble.speed += 0.03

    state.marbleh.x += state.marble.speed * state.marble.dir
    state.marbleh.y += state.marble.speed
    state.marble.x = state.marbleh.x
    state.marble.y = (state.marbleh.y * 0.6) + ((255 - center_column.r) * 1.25)
    state.marble.angle = state.marble.angle + state.marble.speed * state.marble.dir * -10

    if state.marble.angle > 0:
        state.marble.angle = -50
    elif state.marble.angle < -50:
        state.marble.angle = 0

    # Abfrage ob man im Ziel ist
    if state.marbleh.y > 700:  # todo: level abhängig, auch von x abhängig?
        if state.current_level == LevelState.LEVEL_FOUR:
            state.game_state = GameState.GAME_WIN
        else:
            state.game_state = GameState.LEVEL_WIN
            state.not_added_points_and_incremented = True


# def on_key_down(key):
# print(key)


def get_height(x, y):
    if x > game_constants.WIDTH:
        x = game_constants.WIDTH
    if y > game_constants.HEIGHT:
        y = game_constants.HEIGHT
    try:
        return state.heightmap.get_at((int(x), int(y)))
    except IndexError as e:
        print(e)
