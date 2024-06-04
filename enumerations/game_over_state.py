from enum import Enum


class GameOverState(Enum):
    TIMER_UP = 'timer_up'
    ENEMY_HIT = 'enemy_hit'
    FALL_OVER_EDGE = 'fall_over_edge'
    UNKNOWN = 'unknown'
