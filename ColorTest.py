from PIL import ImageGrab
import pyautogui as cursor
import time
from AutoFisher import isBlue, isRed, isWhite, printColor
screenSize = 1


def testing():
    while True:
        # Grab cursor position (used to find the bob)
        position = cursor.position()
        x = position.x
        y = position.y

        # Get part of image with the bob
        bbox = (x - screenSize, y - screenSize, x + screenSize, y + screenSize)
        image = ImageGrab.grab(bbox)

        # Get pixel to compare bob values to
        pixel = image.getpixel((1, 1))
        printColor(pixel)
        time.sleep(0.25)


if __name__ == '__main__':
    time.sleep(3)
    testing()
