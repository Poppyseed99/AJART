import time
import pyautogui
import keyboard
from PIL import Image
from math import floor

# Assuming the top-left corner of the canvas is (x_start, y_start)
# We need to anchor the canvas location relative to the display resolution
x_start, y_start = 240, 129  # Adjust these to match where your canvas starts on the screen
while True:
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")

def select_color(color):
    time.sleep(1)
    if color == "cyan":
        pyautogui.click(x_start + 121, y_start + 202)
    elif color == "magenta":
        pyautogui.click(x_start + 81, y_start + 299)
    elif color == "yellow":
        pyautogui.click(x_start + 123, y_start + 121)
    elif color == "red":
        pyautogui.click(x_start + 103, y_start + 82)
    elif color == "blue":
        pyautogui.click(x_start + 95, y_start + 230)
    elif color == "green":
        pyautogui.click(x_start + 102, y_start + 150)
    else:
        raise ValueError(f"Value {color} not in colors")
    time.sleep(1)


def select_size(size):
    time.sleep(1)
    if size <= 3:
        pyautogui.click(x_start + 78, y_start + 786)
    elif size <= 7:
        pyautogui.click(x_start + 156, y_start + 784)
    elif size <= 13:
        pyautogui.click(x_start + 83, y_start + 834)
    elif size <= 20:
        pyautogui.click(x_start + 158, y_start + 828)
    elif size <= 40:
        pyautogui.click(x_start + 76, y_start + 885)
    time.sleep(1)


def getcolors(mode):
    if mode == "RGB":
        return ["red", "green", "blue"]


def click(xloc, yloc, speed):
    if speed:
        pyautogui.click(xloc, yloc)
    else:
        pyautogui.moveTo(xloc, yloc)
        pyautogui.mouseDown()
        pyautogui.mouseUp()


class Painter:
    def __init__(self, filename, mode, scaledivisor, speed, cd):
        self.speed = speed
        self.cd = cd
        self.done = False
        self.filename = filename
        self.mode = mode
        self.scaledivisor = scaledivisor
        self.img = Image.open(filename)
        self.img = self.img.convert(self.mode)
        self.width = 703  # Canvas width for Animal Jam Classic
        self.height = 430  # Canvas height for Animal Jam Classic
        self.img = self.img.resize((self.width // self.scaledivisor, self.height // self.scaledivisor))
        self.pix = self.img.load()
        self.x, self.y = self.img.size
        print(self.x, self.y)
        self.img.show()
        keyboard.add_hotkey("[", self.drawpic)

    def drawpic(self):
        time.sleep(1)
        select_size(self.scaledivisor)

        keyboard.unhook_all_hotkeys()
        stop = False
        counter = 0
        for color in getcolors(self.mode):
            if stop:
                while not keyboard.is_pressed("["):
                    pass
                stop = False
                print("unstopped")
            select_color(color)
            for xval in range(self.x):
                if stop:
                    while not keyboard.is_pressed("["):
                        pass
                    stop = False
                    print("unstopped")
                for yval in range(self.y):
                    if stop:
                        while not keyboard.is_pressed("["):
                            pass
                        stop = False
                        print("unstopped")
                    xloc = x_start + 350 + xval * self.width / self.x
                    yloc = y_start + 110 + yval * self.height / self.y

                    # Make sure the cursor stays within the canvas
                    if xloc < x_start or xloc > x_start + self.width or yloc < y_start or yloc > y_start + self.height:
                        continue

                    px = self.pix[xval, yval]
                    print(px)
                    if type(px) != int:
                        pixel = px[counter]
                    else:
                        pixel = 256 - px
                    pixmult = floor(pixel * self.cd / 256)

                    for i in range(pixmult):
                        click(xloc, yloc, self.speed)
                    if keyboard.is_pressed("]"):
                        stop = True
            counter += 1
        self.done = True


