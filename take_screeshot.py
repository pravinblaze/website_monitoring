import csv
import os
import sys
import pyautogui
from utils import point, rectangle

def take_screenshot(target_region):

    csv_file = 'screenshots/regions.csv'

    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    region_found = False
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'] == target_region:
                region = rectangle(
                    point(int(row['x1']), int(row['y1'])),
                    point(int(row['x2']), int(row['y2']))
                )
                screenshot = pyautogui.screenshot(
                    region=(region.top_left.x, region.top_left.y, region.width, region.height)
                )
                screenshot.save(f'screenshots/{target_region}.png')
                region_found = True
                print(f"Screenshot for region '{target_region}' has been taken.")
                break

    if not region_found:
        print(f"Region '{target_region}' not found in {csv_file}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python take-screenshot.py <region_name>")
        sys.exit(1)

    target_region = sys.argv[1]
    take_screenshot(target_region)
