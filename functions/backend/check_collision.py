from pygame import Rect


def check_collision_with_shuriken(marble, shuriken):
    # Define a smaller rectangle for the shuriken
    shuriken_hitbox = Rect(shuriken.x - shuriken.width / 4, shuriken.y - shuriken.height / 4, shuriken.width / 2, shuriken.height / 2)
    return marble.colliderect(shuriken_hitbox)


def check_collision_with_flag(marble, flag):
    # Define a smaller rectangle for the shuriken
    flag_hitbox = Rect(flag.x - flag.width / 75, flag.y - flag.height / 75, flag.width / 75, flag.height / 75)
    return marble.colliderect(flag_hitbox)
