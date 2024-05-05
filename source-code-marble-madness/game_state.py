from enum import Enum


class GameState(Enum):
    # states for starting pages
    START_PAGE = 'start_page'
    MENU_PAGE = 'menu_page'

    # level states
    LEVEL_ONE = 'level_one'
    LEVEL_TWO = 'level_two'
    LEVEL_THREE = 'level_three'
    LEVEL_FOUR = 'level_four'

    # states for win or lose
    WIN = 'win'
    GAME_OVER = 'game_over'

    # placeholder
    PLACEHOLDER = 'placeholder'
