from constants import state, game_constants


def animate_coin():
    state.coin_animation_counter += 1

    if state.coin_animation_counter >= state.coin_animation_interval:
        state.coin_animation_counter = 0
        state.coin.image = game_constants.coin_images[state.coin_frame % len(game_constants.coin_images)]
        state.coin_frame += 1
