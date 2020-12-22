from PIL import ImageGrab
import pyautogui as cursor
import time
import sys
import keyboard

# screenResX = 1920
screenResY = 1080
screenSize = 1
# bobValues = [(163, 161, 157), (179, 179, 179), (153, 6, 6), (245, 68, 68)]
x, y = 0, 0
threshold = 100
found = False
fishCounter = 0

"""
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
        print(pixel)
        time.sleep(0.5)
"""


# Displays text upon entry
def text():
    print("##############################################################")
    print("############## Welcome to Minecraft AutoFisher! ##############")
    print("##############################################################")
    print()
    print("Please check that you have the 'particles' setting set to Minimal")
    print("* Note that for better performance, it is recommended to turn the FOV down *")
    print("Hold the letter 'i' down to close the application")
    print()
    input("Enter any key to begin the auto fisher: ")
    print("Starting up! Please switch to minecraft and cast line...")


# Finds bob position
def initialize():
    global x, y, found
    # Grab cursor position (used to find the bob)
    position = cursor.position()
    x = position.x
    y = position.y

    # We now have a strip up to the bob
    bbox = (x - 1, int(y - screenResY/3), x + 1, y)
    image = ImageGrab.grab(bbox)
    # image.show()

    # Find the red bob pixel
    counter = image.height - 1

    while not found and counter > 0:
        pixel = image.getpixel((1, counter))
        # If pixel is red
        if (2 * pixel[0] - pixel[1] - pixel[2]) > threshold:
            found = True
        counter -= 1

    if not found:
        print("Calibration Failed!")
    if found:
        print("Calibration Success!")

    # We've now updated both the global x and y to be the red bob position
    y = y - (image.height - counter) - 2


def main():
    global found, fishCounter
    if not found:
        sys.exit("Red blob not found")
    print("Blobber located at position: " + str(x) + ", " + str(y))
    print()

    while True:
        # User can quit by pressing 'i'
        if keyboard.is_pressed('i'):
            sys.exit("Application closed successfully")

        # Get part of image with the bob
        bbox = (x - screenSize, y - screenSize, x + screenSize, y + screenSize)
        image = ImageGrab.grab(bbox)

        # Get pixel to compare bob values to
        pixel = image.getpixel((1, 1))

        # Fish caught
        if (2 * pixel[2] - pixel[0] - pixel[1]) > threshold:
            cursor.rightClick()
            fishCounter += 1
            print("Fish caught! Total farmed: " + str(fishCounter))
            time.sleep(1)
            cursor.rightClick()
            time.sleep(1.25)


if __name__ == '__main__':
    text()
    # User has time to switch to instance of Minecraft
    time.sleep(8)
    initialize()
    main()
    # testing()
