import pyautogui
import random
import time
# import gettext

# Temporary debug commands:
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def random_move():
    while True:
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pyautogui.moveTo(x, y, 0.5)
        time.sleep(2)


def show_screen_size():
    print(pyautogui.size())


def get_screen_size():
    width, height = pyautogui.size()


def set_mouse_rectangle():
    witdth = int(input("Please, set the rectangle width:  "))
    height = int(input("Please, set the rectangle height:  "))
    pass

def moving_mouse():
    cycles = int(input("Please, set the number of mouse cycles:  "))
    # mouse speed/ '0' turns our mouse to Übermaus with ultraspeed
    duration = float(input("Please, set the mouse moving duration (0 - ):  "))
    startpoint_x = int(input("Please, set up startpoint coordinates:  "))
    startpoint_y = int(input("Please, set up endpoint coordinates:  "))
    # range is showing us amount of mouse cycles
    for i in range(cycles + 1):
        #  pyautogui.moveTo(start_x, start_y, duration=duration)  # перемещаем мышь в заданную позиицю на экране
        pyautogui.moveTo(startpoint_x, startpoint_y, duration=duration)  # перемещаем мышь в заданную позиицю на экране
#     print(pyautogui.position())  # temporary checking command
#     pyautogui.moveTo(200, 100, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveTo(200, 200, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveTo(100, 200, duration=0.25)
#     print(pyautogui.position())
#
# for i in range(10):
#     # то же самое, но курсор перемещается относительно текущей позиции
#     # начинает квадрат с того места, где мышь оказывается на экране, когда запускается код
#     pyautogui.moveRel(100, 0, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveRel(0, 100, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveRel(-100, 0, duration=0.25)
#     print(pyautogui.position())
#     pyautogui.moveRel(0, -100, duration=0.25)
#     print(pyautogui.position())


if __name__ == '__main__':
    random_move()
