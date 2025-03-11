import csv
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import pyautogui
import pygame
import time

from utils import human_like_mouse_move, point, rectangle
from take_screeshot import take_screenshot


def compare_region_image(region: rectangle, name, threshold=0.9):
    """
    Compares a stored baseline image with a live screenshot of a specified rectangular region using SSIM.

    Parameters:
        region: A rectangle object with attributes top_left (point) and bottom_right (point)
        name: String used to locate the baseline image in the 'screenshots' folder named '{name}.png'
        threshold: SSIM threshold (default 0.9), values closer to 1 indicate more strict similarity checking.

    Returns:
        True if the SSIM score is above the threshold, False otherwise.
    """
    # Read baseline image from the screenshots folder
    baseline_path = f"screenshots/{name}.png"
    baseline_image = Image.open(baseline_path).convert("L")  # Convert to grayscale

    # Take a screenshot of the specified region using PyAutoGUI
    live_image = pyautogui.screenshot(
        region=(region.top_left.x, region.top_left.y, region.width, region.height)
    )
    live_image = live_image.convert("L")  # Convert to grayscale for SSIM

    # Convert PIL images to NumPy arrays for OpenCV processing
    baseline_np = np.array(baseline_image)
    live_np = np.array(live_image)

    # Resize images to the same size (PyAutoGUI might have slight dimension mismatches)
    if baseline_np.shape != live_np.shape:
        live_np = cv2.resize(live_np, (baseline_np.shape[1], baseline_np.shape[0]))

    # Compute SSIM score
    score, _ = ssim(baseline_np, live_np, full=True)

    print(f"SSIM Score: {score}, for region: {name}")  # Debugging info
    return score >= threshold  # Return True if images are similar enough


def perform_actions_from_csv(csv_file: str) -> bool:

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
        perform_actions_from_csv("action-data/refresh.csv")
        time.sleep(5)
        if not compare_region_image(regions["button"], "button"):
            print("Button not found. Trying again...")
            continue
        perform_actions_from_csv("action-data/check-availability.csv")
        time.sleep(5)
        if not compare_region_image(regions["availability"], "availability"):
            take_screenshot("browser")
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
