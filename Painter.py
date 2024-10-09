import time
import pyautogui
import keyboard
from PIL import Image
from math import floor


def select_color(color):
    time.sleep(1)
    if color == "cyan":
        pyautogui.click(121, 202)
    elif color == "magenta":
        pyautogui.click(81, 299)
    elif color == "yellow":
        pyautogui.click(123, 121)
    elif color == "red":
        pyautogui.click(103, 82)
    elif color == "blue":
        pyautogui.click(95, 230)
    elif color == "green":
        pyautogui.click(102, 150)
    else:
        raise ValueError(f"Value {color} not in colors")
    time.sleep(1)


def select_size(size):
    time.sleep(1)
    if size <= 3:
        pyautogui.click(78, 786)
    elif size <= 7:
        pyautogui.click(156, 784)
    elif size <= 13:
        pyautogui.click(83, 834)
    elif size <= 20:
        pyautogui.click(158, 828)
    elif size <= 40:
        pyautogui.click(76, 885)
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
                    xloc = 350 + xval * self.width / self.x
                    yloc = 110 + yval * self.height / self.y

                    # Make sure the cursor stays within the canvas
                    if xloc < 0 or xloc > self.width or yloc < 0 or yloc > self.height:
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


