import csv
import time
import pyautogui

from utils import human_like_mouse_move, point, rectangle

if __name__ == "__main__":
    regions = {
        "login": rectangle(point(6786, 225), point(7258, 349)),
        # "check_booking": rectangle(point(, ), point(, ))
    }

    # CSV file with the actions (update the filename/path if needed)
    for csv_file in [
        "action-data/vfs-login.csv",
        "action-data/check-booking.csv"
        ]:
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

                human_like_mouse_move(x, y, steps=20, total_duration=2.0)
                if action == "click":
                    print(f"Moving to ({x}, {y}) in a human-like fashion for '{description}'.")
                    pyautogui.click(x, y)
                elif action == "scroll_down":
                    print(f"Scrolling down at ({x}, {y}) for '{description}'.")
                    pyautogui.scroll(-10)
                else:
                    print(f"Action '{action}' for '{description}' is not supported.")

    print("All actions completed.")
