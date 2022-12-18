import pyautogui
# import gettext

# Temporary debug commands:
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


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
    for i in range(cycles + 1):  # range is showing us amount of mouse cycles

#     pyautogui.moveTo(100, 100, duration=0.25)  # перемещаем мышь в заданную позиицю на экране
#     # duration - скорость перемещения. При '0' - перемещается мгновенно
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
    screen_size()
