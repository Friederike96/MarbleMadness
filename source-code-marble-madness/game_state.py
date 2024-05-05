from enum import Enum


class GameState(Enum):
    # states for starting pages
    START_PAGE = 'start_page'
    MENU_PAGE = 'menu_page'

    # level states
    LEVEL_GAME = 'level_game'

    # states for win or lose
    WIN = 'win'
    GAME_OVER = 'game_over'

    # placeholder
    PLACEHOLDER = 'placeholder'
