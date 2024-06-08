from constants import game_constants, state
from enumerations.game_over_state import GameOverState
from enumerations.game_state import GameState
from functions.backend.check_collision import check_collision_with_enemy


def handle_enemy_collision():
    if check_collision_with_enemy(state.marble, state.enemy):
        state.game_state = GameState.GAME_OVER
        state.game_over_state = GameOverState.ENEMY_HIT
        state.sounds.enemysound.set_volume(0.1)
        state.sounds.enemysound.play()


def update_enemy_position():
    target_x, target_y = game_constants.enemy_positions[state.enemy_index]
    # Calculate the distance between the enemy and the target position
    distance_x = target_x - state.enemy.x
    distance_y = target_y - state.enemy.y

    state.enemy.angle += 5
    print(state.enemy.angle)
    if state.enemy.angle >= 360:
        state.enemy.angle = 0

    # Move the enemy towards the target position
    if abs(distance_x) > state.enemy_speed:
        state.enemy.x += state.enemy_speed if distance_x > 0 else -state.enemy_speed
    else:
        state.enemy.x = target_x

    if abs(distance_y) > state.enemy_speed:
        state.enemy.y += state.enemy_speed if distance_y > 0 else -state.enemy_speed
    else:
        state.enemy.y = target_y

    # Check if the enemy has reached the current target position
    if state.enemy.x == target_x and state.enemy.y == target_y:
        # Move to the next target position
        state.target_index = (state.enemy_index + 1) % len(game_constants.enemy_positions)
