import pyautogui

config_data = {}


def set_config(config):
    global config_data
    config_data = config


def click(x, y, d=0.1):
    if config_data["screen_num"] == 1:
        pyautogui.click(x+1920, y, duration=d)
    else:
        pyautogui.click(x, y, duration=d)


def scroll(unit=-100):
    pyautogui.scroll(unit)


def screenshot():
    pyautogui.screenshot('imgs/test.png')
