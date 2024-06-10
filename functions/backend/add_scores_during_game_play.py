from constants import state


def add_scores_during_game_play():
    if state.previous_timer_value == 0:
        state.previous_timer_value = round(state.timer, 2)

    elif (
            round(state.timer, 2) < state.previous_timer_value - 0.2
            and state.previous_timer_value != 0
    ):
        state.score += 10
        state.score_for_current_level += 10
        state.previous_timer_value = round(state.timer, 2)
