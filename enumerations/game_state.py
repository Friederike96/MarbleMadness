from enum import Enum


class GameState(Enum):
    # states for starting pages
    START_PAGE = 'start_page'
    MENU_PAGE = 'menu_page'

    # level states
    COUNTDOWN = 'countdown'
    LEVEL_GAME = 'level_game'

    # states for win or lose
    LEVEL_WIN = 'level_win'
    GAME_WIN = 'game_win'
    GAME_OVER = 'game_over'

    # placeholder
    PLACEHOLDER = 'placeholder'
