from pgzero.keyboard import keyboard

from constants import state


def update_marble_position():
    # if state.joystick is not None:
    # print(f"Joystick axis 0: {state.joystick.get_axis(0)}")
    # print(f"Joystick axis 1: {state.joystick.get_axis(1)}")

    # Joystick-Input prüfen und nur berücksichtigen, wenn er außerhalb der Dead Zone liegt
    # TODO Joystick movement neu schreiben, da UP und DOWN nicht richtig funktionieren
    if keyboard.left or (state.joystick is not None and state.joystick.get_axis(0) < -state.DEAD_ZONE):
        state.marble.dir = max(state.marble.dir - 1, -1)
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True

    if keyboard.right or (state.joystick is not None and state.joystick.get_axis(0) > state.DEAD_ZONE):
        state.marble.dir = min(state.marble.dir + 1, 1)
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True

    if keyboard.up or (state.joystick is not None and state.joystick.get_axis(1) < -state.DEAD_ZONE):
        state.marble.y += 2  # Passe die Geschwindigkeit nach Bedarf an
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True

    if keyboard.down or (state.joystick is not None and state.joystick.get_axis(1) > state.DEAD_ZONE):
        state.marble.y -= 2  # Passe die Geschwindigkeit nach Bedarf an
        state.marble.speed = min(1, state.marble.speed + 0.1)
        state.marble_moved_once = True
