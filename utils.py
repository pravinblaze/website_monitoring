import pyautogui
import random

def human_like_mouse_move(target_x, target_y, steps=20, total_duration=2.0):
    """
    Moves the mouse from its current position to (target_x, target_y) in a human-like manner.

    Parameters:
      target_x, target_y: Destination coordinates.
      steps: Number of intermediate moves.
      total_duration: Total time (in seconds) for the movement.
    """
    start_x, start_y = pyautogui.position()
    step_duration = total_duration / steps

    for i in range(1, steps):
        fraction = i / steps
        # Linear interpolation between the starting point and the target.
        intermediate_x = start_x + fraction * (target_x - start_x)
        intermediate_y = start_y + fraction * (target_y - start_y)

        # Add a random offset to simulate human inaccuracy.
        # Use a smaller offset near the start and end to ensure smooth landing.
        offset_range = 10 if 0.2 < fraction < 0.8 else 3
        offset_x = random.uniform(-offset_range, offset_range)
        offset_y = random.uniform(-offset_range, offset_range)

        new_x = int(intermediate_x + offset_x)
        new_y = int(intermediate_y + offset_y)

        pyautogui.moveTo(new_x, new_y, duration=step_duration)

    # Ensure the final position is exactly the target.
    pyautogui.moveTo(target_x, target_y, duration=step_duration)

class point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class rectangle:
    def __init__(self, top_left:point, bottom_right:point):
        self.top_left = top_left
        self.width = bottom_right.x - top_left.x
        self.height = bottom_right.y - top_left.y

