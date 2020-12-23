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
found = False
fishCounter = 0


# Displays text upon entry
def text():
    print("##############################################################")
    print("############## Welcome to Minecraft AutoFisher! ##############")
    print("##############################################################")
    print()
    print("1. Please check that you have the 'particles' setting set to Minimal")
    print("2. Hold the letter 'i' down to close the application")
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
    bbox = (x - 1, int(y - screenResY/8), x + 1, int(y + screenResY/8))
    image = ImageGrab.grab(bbox)
    # image.show()

    # Find the red bob pixel
    counter = image.height - 1

    while not found and counter > 0:
        pixel = image.getpixel((1, counter))
        if isRed(pixel):
            found = True
        counter -= 1

    if not found:
        print("Calibration Failed!")
    if found:
        print("Calibration Success!")

    # We've now updated both the global x and y to be the red bob position
    y = y - (int(image.height/2) - counter) - 2

    if not found:
        sys.exit("Red bob not found")
    print("Bobber located at position: " + str(x) + ", " + str(y))
    print()


def initialize2():
    global x, y, found
    # Grab cursor position (used to find the bob)
    position = cursor.position()
    x = position.x
    y = position.y


def main():
    global fishCounter
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
        if isBlue(pixel):
            cursor.rightClick()
            fishCounter += 1
            print("Fish caught! Total farmed: " + str(fishCounter))
            time.sleep(1)
            cursor.rightClick()
            time.sleep(1.25)

        time.sleep(0.25)


def printColor(pixel):
    if isBlue(pixel):
        print(str(pixel) + " is blue")
    elif isRed(pixel):
        print(str(pixel) + " is red")
    elif isWhite(pixel):
        print(str(pixel) + " is white")
    elif isBlack(pixel):
        print(str(pixel) + " is black")
    else:
        print(str(pixel) + " is some other color")


def isBlack(pixel):
    diff = 20
    return pixel[0] < diff and pixel[1] < diff and pixel[2] < diff


def isWhite(pixel):
    diff = 25
    mean = (pixel[0] + pixel[1] + pixel[2]) / 3
    if pixel[0] < 100 or pixel[1] < 100 or pixel[2] < 100:
        return False
    if abs(pixel[0] - mean) > diff or abs(pixel[1] - mean) > diff or abs(pixel[2] - mean) > diff:
        return False
    return True


def isRed(pixel):
    threshold = 130
    return (2 * pixel[0] - pixel[1] - pixel[2]) > threshold


def isBlue(pixel):
    threshold = 105
    return (2 * pixel[2] - pixel[0] - pixel[1]) > threshold


if __name__ == '__main__':
    text()
    # User has time to switch to instance of Minecraft
    time.sleep(8)
    initialize()
    main()
