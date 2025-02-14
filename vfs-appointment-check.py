import csv
from PIL import Image, ImageChops
import pyautogui
import pygame
import time

from utils import human_like_mouse_move, point, rectangle


def compare_region_image(region: rectangle, name):
    """
    Compares a stored baseline image with a live screenshot of a specified rectangular region.

    Parameters:
        region: A rectangle object with attributes top_left (point) and bottom_right (point)
        name: String used to locate the baseline image in the 'screenshots' folder named '{name}.png'

    Returns:
        True if the images are identical, False otherwise.
    """
    # Read baseline image from the screenshots folder
    baseline_path = f"screenshots/{name}.png"
    baseline_image = Image.open(baseline_path)

    # Take a screenshot of the specified region using PyAutoGUI
    live_image = pyautogui.screenshot(
        region=(region.top_left.x, region.top_left.y, region.width, region.height)
    )
    live_image = live_image.convert("RGB")  # Ensure format consistency

    # Compare images
    diff = ImageChops.difference(baseline_image, live_image)
    return diff.getbbox() is None


def perform_actions_from_csv(csv_file: str, region_name: str) -> bool:
    """
    Processes the actions specified in a CSV file.

    Each row in the CSV should contain:
        - description: Description of the action.
        - x, y: Coordinates for the mouse action.
        - action: The action to perform (e.g., "click", "scroll_down").
        - delay: Delay before executing the action.
    """

    if not compare_region_image(regions[region_name], region_name):
        print(f"Region '{region_name}' not found.")
        return False

    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            description = row["description"]
            x = int(row["x"])
            y = int(row["y"])
            action = row["action"].lower()
            delay = float(row["delay"])

            print(f"Waiting {delay:.2f} seconds before '{description}' action...")
            time.sleep(delay)

            human_like_mouse_move(x, y, steps=20, total_duration=1.0)

            if not compare_region_image(regions[region_name], region_name):
                print(f"Region '{region_name}' not found.")
                return False

            if action == "click":
                print(f"Moving to ({x}, {y}) in a human-like fashion for '{description}'.")
                pyautogui.click(x, y)
            elif action == "scroll_down":
                print(f"Scrolling down at ({x}, {y}) for '{description}'.")
                pyautogui.scroll(-10)
            else:
                print(f"Action '{action}' for '{description}' is not supported.")

    return True


if __name__ == "__main__":
    regions = {}
    # CSV file with screenshot regions (update the filename/path if needed)
    with open("screenshots/regions.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            top_left = point(int(row["x1"]), int(row["y1"]))
            bottom_right = point(int(row["x2"]), int(row["y2"]))
            regions[name] = rectangle(top_left, bottom_right)

    # CSV file with the actions (update the filename/path if needed)
    while True:
        perform_actions_from_csv("action-data/vfs-login.csv", "login")
        while True:
            if not perform_actions_from_csv("action-data/check-booking.csv", "appointment"):
                break
            else:
                if not compare_region_image(regions["check-booking"], "check-booking"):
                    pygame.mixer.init()
                    alert_sound = pygame.mixer.Sound("alert.wav")
                    alert_sound.play(loops=-1)
                    print("Playing alert sound indefinitely. Press Ctrl+C to stop.")
                    try:
                        while True:
                            time.sleep(1)
                    except KeyboardInterrupt:
                        pygame.mixer.stop()
                        print("Alert stopped.") 
        if perform_actions_from_csv("action-data/reminder.csv", "reminder"):
            perform_actions_from_csv("action-data/logout.csv", "appointment")
