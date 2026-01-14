import time
import pyautogui
import random

# Get screen size
screen_width, screen_height = pyautogui.size()

# Start at the center of the screen
x, y = screen_width // 2, screen_height // 2

for i in range(50):  # run 5 iterations (adjust as needed)
    delay = random.randint(1, 60)  # random delay between 1 and 60 sec
    print(f"Iteration {i+1} - Sleeping for {delay} seconds")
    time.sleep(delay)

    # Move to center
    pyautogui.moveTo(x, y, duration=0.5)

    # Draw a square
    pyautogui.dragRel(100, 0, duration=0.5)
    pyautogui.dragRel(0, 100, duration=0.5)
    pyautogui.dragRel(-100, 0, duration=0.5)
    pyautogui.dragRel(0, -100, duration=0.5)
