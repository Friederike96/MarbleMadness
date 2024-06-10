from constants import state, game_constants
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.backend.update_marble_animation import update_marble_animation


def move_marble():
    if state.game_state != GameState.LEVEL_GAME or not state.marble_moved_once:
        return

    center_column = get_height(state.marbleh.x, state.marbleh.y)
    left_column = get_height(state.marbleh.x - game_constants.HEIGHTMAP_OFFSET, state.marbleh.y + game_constants.HEIGHTMAP_OFFSET)
    right_column = get_height(state.marbleh.x + game_constants.HEIGHTMAP_OFFSET, state.marbleh.y + game_constants.HEIGHTMAP_OFFSET)

    if any([center_column, left_column, right_column]) is None:  # or center_column.r == 0:
        state.game_state = GameState.GAME_OVER  # reminder: change back
        state.game_over_state = GameOverState.FALL_OVER_EDGE
        return

    if left_column.r < center_column.r or right_column.r < center_column.r:
        state.marble.y += state.marble.speed
        state.marble.speed += game_constants.GRAVITY

    state.marbleh.x += state.marble.speed * state.marble.dir
    state.marbleh.y += state.marble.speed
    state.marble.x = state.marbleh.x

    # die in Berechnung in Zeile 33 ist lediglich eine Skalierung welche für die vorgegebene Map notwending ist.
    # bei den anderen Maps wird dies nicht benötigt deshalb marble.y = marbleh.y
    if state.current_level == LevelState.LEVEL_ENTRY or state.current_level.LEVEL_TWO:
        state.marble.y = state.marbleh.y
    elif state.current_level == LevelState.LEVEL_ONE:
        state.marble.y = (state.marbleh.y * 0.6) + ((game_constants.MAX_HEIGHTMAP_VALUE - center_column.r) * game_constants.HEIGHTMAP_VERTICAL_SCALE)
    state.marble.angle = state.marble.angle + state.marble.speed * state.marble.dir * - 10

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
