import os
import time
from PIL import ImageGrab
from pynput import keyboard

output_directory = "screenshots"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def capture_screenshot():
    screenshot = ImageGrab.grab()
    return screenshot

def save_screenshot(screenshot, quality=95):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = f"screenshot_{timestamp}.jpg"
    file_path = os.path.join(output_directory, filename)
    screenshot.save(file_path, format="JPEG", quality=quality)
    print(f"Screenshot saved as {file_path}")

def on_key_release(key):
    if key == keyboard.Key.print_screen:
        quality = int(input("Enter image quality (1-100): "))
        quality = max(1, min(100, quality))  # Ensure quality is between 1 and 100
        screenshot = capture_screenshot()
        save_screenshot(screenshot, quality)

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
