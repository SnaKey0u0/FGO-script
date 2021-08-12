import win32gui
import win32api
import win32con
from utils.logger import *
# import win32ui
# from ctypes import windll

config_data = {}
hWnd = None


def set_config(config):
    global config_data
    config_data = config
    try:
        global hWnd
        hWnd = win32gui.FindWindow(None, "夜神模擬器")
    except Exception as e:
        error(e)


# def click(x, y, d=0.1):
#     x_origin, y_origin = pyautogui.position()
#     config_data["screen_num"]=1
#     if config_data["screen_num"] == 1:
#         pyautogui.click(x+1920, y, duration=d)
#     else:
#         pyautogui.click(x, y, duration=d)
#     pyautogui.moveTo(x_origin, y_origin)


def click(x, y):
    x, y = int(x), int(y)
    lParam = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, 0, lParam)

# def shotTest():
#     hwndDC = win32gui.GetWindowDC(hWnd)
#     mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
#     saveDC = mfcDC.CreateCompatibleDC()

#     saveBitMap = win32ui.CreateBitmap()
#     print(saveBitMap)
#     saveBitMap.CreateCompatibleBitmap(mfcDC)

#     saveDC.SelectObject(saveBitMap)
#     result = windll.user32.PrintWindow(hWnd, saveDC.GetSafeHdc(), 0)

#     bmpinfo = saveBitMap.GetInfo()
#     bmpstr = saveBitMap.GetBitmapBits(True)
#     print(bmpstr)

#     im = Image.frombuffer(
#         'RGB',
#         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
#         bmpstr, 'raw', 'BGRX', 0, 1)

#     win32gui.DeleteObject(saveBitMap.GetHandle())
#     saveDC.DeleteDC()
#     mfcDC.DeleteDC()
#     win32gui.ReleaseDC(hwnd, hwndDC)

# if result == 1:
#     #PrintWindow Succeeded
#     im.save("test.png")

# if __name__ == "__main__":
    # shotTest()
