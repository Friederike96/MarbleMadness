from constants import state, game_constants
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from enumerations.level_state import LevelState
from functions.backend.update_marble_animation import update_marble_animation


def move_marble():
    if state.game_state != GameState.LEVEL_GAME or not state.marble_moved_once:
        return

    if not marble_on_map3d():
        state.game_state = GameState.GAME_OVER
        state.game_over_state = GameOverState.FALL_OVER_EDGE
        return

    state.marbleh.x += state.marble.speed * state.marble.dir
    state.marbleh.y += state.marble.speed
    state.marble.x = state.marbleh.x
    state.marble.y = state.marbleh.y

    update_marble_animation()


def marble_on_map3d():
    marble_pos = (int(state.marble.x - state.map3d.left), int(state.marble.y - state.map3d.top))
    try:
        print(f'map: {state.map_mask.get_at(marble_pos)}')
        return state.map_mask.get_at(marble_pos)
    except Exception as e:
        print(e)


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
