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

            print(f"Moving to ({x}, {y}) in a human-like fashion for '{description}'.")
            human_like_mouse_move(x, y, steps=20, total_duration=1.0)

            if action == "click":
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
        perform_actions_from_csv("action-data/availability.csv", "availability")
        time.sleep(2)
        if not compare_region_image(regions["availability"], "availability"):
            pygame.mixer.init()
            alert_sound = pygame.mixer.Sound("alert.mp3")
            alert_sound.play(loops=-1)
            print("Playing alert sound indefinitely. Press Ctrl+C to stop.")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pygame.mixer.stop()
                print("Alert stopped.")
