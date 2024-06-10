from pgzero.keyboard import keyboard

from constants import state


def update_marble_position():
    if keyboard.left or state.joystick is not None and state.joystick.get_axis(0) < -0.1:
        state.marble.dir = max(state.marble.dir - 1, -1)
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True  # todo: still needed??

    if keyboard.right or state.joystick is not None and state.joystick.get_axis(0) > 0.1:
        state.marble.dir = min(state.marble.dir + 1, 1)
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True

    if keyboard.up or state.joystick is not None and state.joystick.get_axis(1) < 0.1:
        state.marbleh.y -= 2  # todo: change how fast? > 2,5
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True

    if keyboard.down or state.joystick is not None and state.joystick.get_axis(1) < -0.1:
        state.marbleh.y += 1.5  # todo: change how fast? > 2,5
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True
