import time
import pyautogui
from PIL import ImageGrab

SCAN_BOX = (500, 340, 650, 390)
OBSTACLE_THRESHOLD = 50


def obstacle_in_path(box):
    img = ImageGrab.grab(bbox=box).convert("L")
    pixels = list(img.getdata())

    dark_pixels = sum(1 for p in pixels if p < OBSTACLE_THRESHOLD)
    ratio = dark_pixels / len(pixels)

    return ratio > 0.02


last_jump = 0


def main():
    global last_jump
    print("Focus the game window. Bot starts in 3 seconds.")
    time.sleep(3)

    pyautogui.press("space")

    while True:
        if obstacle_in_path(SCAN_BOX):
            now = time.time()
            if now - last_jump > 0.2:
                pyautogui.press("space")
                last_jump = now
        time.sleep(0.01)


if __name__ == "__main__":
    main()
