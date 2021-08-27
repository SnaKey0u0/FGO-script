import win32gui
import win32api
import win32con
import win32ui
from utils.logger import *
# from ctypes import windll

# config_data = {}
hwnd = None
width = 1920
height = 1080


def ask_config():
    # global config_data
    # config_data = config
    try:
        global hwnd, width, height
        hwnd = win32gui.FindWindow(None, "夜神模擬器")
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bottom - top
        return width, height
        # 待修改
        # width, height = 1920, 1080
    except Exception as e:
        error(e)
        return False


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
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)


def getWinBitStr():

    hwindc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)
    # bmp.SaveBitmapFile(memdc, "shot.bmp")

    bmpstr = bmp.GetBitmapBits(True)
    # convert the raw data into a format opencv can read
    # img = np.frombuffer(bmpstr, dtype='uint8')
    # img.shape = (height, width, 4)
    # # img = np.ascontiguousarray(img)
    # cv2.imshow("123", img)
    # cv2.waitKey()

    # bmpinfo = bmp.GetInfo()
    # img = Image.frombuffer(
    #         'RGB',
    #         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    #         bmpstr, 'raw', 'BGRX', 0, 1)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return bmpstr, width, height


# if __name__ == "__main__":
#     set_config()
#     # click(960,540)
#     getWinBitStr(1920, 1080)
