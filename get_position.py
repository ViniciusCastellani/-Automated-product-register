import time
import pyautogui


def get_mouse_position():
    time.sleep(5)
    print(pyautogui.position())


def main():
    get_mouse_position()


if __name__ == "__main__":
    main()