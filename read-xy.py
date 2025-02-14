from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    print(f"Scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# Set up the listener for mouse events
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
