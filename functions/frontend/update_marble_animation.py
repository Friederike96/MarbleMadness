from constants import state, game_constants


def update_marble_animation():

    # Determine the direction
    if state.marble.speed > 0:
        if state.marble.dir > 0.5:
            new_direction = 'right'
        elif state.marble.dir < -0.5:
            new_direction = 'left'  # Add frames for left if needed
        else:
            new_direction = 'bottom_right'
    else:
        new_direction = 'still'

    # If direction changes, reset the frame counter
    if new_direction != state.current_direction:
        state.current_direction = new_direction
        state.marble_frame = 0

    state.marble_animation_counter += 1
    if state.marble_animation_counter >= state.marble_animation_interval:
        state.marble_animation_counter = 0

        if state.current_direction == 'still':
            state.marble.image = game_constants.marble_still_frames[0]
        elif state.current_direction == 'right':
            state.marble.image = game_constants.marble_right_frames[state.marble_frame % len(game_constants.marble_right_frames)]
        elif state.current_direction == 'left':
            state.marble.image = game_constants.marble_left_frames[state.marble_frame % len(game_constants.marble_left_frames)]
        elif state.current_direction == 'bottom_right':
            state.marble.image = game_constants.marble_bottom_right_frames[state.marble_frame % len(game_constants.marble_bottom_right_frames)]
        elif state.current_direction == 'bottom_left':
            state.marble.image = game_constants.marble_bottom_left_frames[state.marble_frame % len(game_constants.marble_bottom_left_frames)]
        elif state.current_direction == 'bottom':
            state.marble.image = game_constants.marble_bottom_frames[state.marble_frame % len(game_constants.marble_bottom_frames)]

        state.marble_frame += 1
