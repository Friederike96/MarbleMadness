import constants.state as state
from enumerations.level_state import LevelState


def increment_level():
    if state.current_level == LevelState.LEVEL_ENTRY:
        state.current_level = LevelState.LEVEL_ONE

    elif state.current_level == LevelState.LEVEL_ONE:
        state.current_level = LevelState.LEVEL_TWO

    elif state.current_level == LevelState.LEVEL_TWO:
        state.current_level = LevelState.LEVEL_THREE

    elif state.current_level == LevelState.LEVEL_THREE:
        state.current_level = LevelState.LEVEL_FOUR
