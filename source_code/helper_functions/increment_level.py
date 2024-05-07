import source_code.constants.state as state
from source_code.enumerations.level_state import LevelState


def increment_level():
    match state.current_level:
        case LevelState.LEVEL_ONE:
            LevelState.LEVEL_TWO

        case LevelState.LEVEL_TWO:
            LevelState.LEVEL_THREE

        case LevelState.LEVEL_THREE:
            LevelState.LEVEL_FOUR
