from pgzero.actor import Actor
from pygame import Rect


def check_collision_with_enemy(marble: Actor, enemy: Actor) -> bool:
    # Define a smaller rectangle for the enemy
    enemy_hitbox = Rect(enemy.x - enemy.width / 4, enemy.y - enemy.height / 4, enemy.width / 2, enemy.height / 2)
    return marble.colliderect(enemy_hitbox)


def check_collision_with_flag(marble: Actor, flag: Actor) -> bool:
    flag_hitbox = Rect(flag.x - flag.width / 75, flag.y - flag.height / 75, flag.width / 75, flag.height / 75)
    return marble.colliderect(flag_hitbox)
