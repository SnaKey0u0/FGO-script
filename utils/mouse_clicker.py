import pyautogui


def click(x, y, d=0.1):
    pyautogui.click(x, y, duration=d)
