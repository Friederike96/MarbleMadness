from pgzero.actor import Actor
from pygame import Rect

from constants import state


def check_collision_with_enemy(marble: Actor, enemy: Actor) -> bool:
    # Define a smaller rectangle for the enemy
    enemy_hitbox = Rect(enemy.x - enemy.width / 4, enemy.y - enemy.height / 4, enemy.width / 2, enemy.height / 2)
    return marble.colliderect(enemy_hitbox)


def check_collision_with_flag(marble: Actor, flag: Actor) -> bool:
    # Define a smaller rectangle for the shuriken
    flag_hitbox = Rect(flag.x - flag.width / 75, flag.y - flag.height / 75, flag.width / 75, flag.height / 75)
    return marble.colliderect(flag_hitbox)


def check_collision_with_finish_box():
    marble_pos = (int(state.marble.x - state.finish_map.left), int(state.marble.y - state.finish_map.top))
    try:
        print(f'finish map: {state.finish_mask.get_at(marble_pos)}')
        return state.finish_mask.get_at(marble_pos)
    except Exception as e:
        print(e)
