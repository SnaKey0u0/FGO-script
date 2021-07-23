import cv2
import time
import numpy as np
from mss import mss
from utils.mouse_clicker import *

rate = 0.5
config_data = {}
# monitor = {'left': 1920, 'top': 0, 'width': 1920, 'height': 1080}


def set_config(config):
    global config_data
    config_data = config


def show_img(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def click_match(rectangles):
    # 回傳第一個位置
    if(len(rectangles) > 0):
        (x, y, w, h) = rectangles[0]
        click(x*(1/rate)+w//2, y*(1/rate)+h//2)
        return True
    else:
        print("no match")
        return False


def match_img(myScreen, target_filename):
    img = cv2.imread(myScreen)
    img = cv2.resize(img, (0, 0), fy=rate, fx=rate)
    target_img = cv2.imread('imgs/'+target_filename+'.png')
    target_img = cv2.resize(target_img, (0, 0), fy=rate, fx=rate)

    # 匹配
    result = cv2.matchTemplate(img, target_img, cv2.TM_CCOEFF_NORMED)

    # 定義圖片大小
    w = target_img.shape[1]
    h = target_img.shape[0]
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # cv2.rectangle(img, max_loc, (max_loc[0]+w, max_loc[1]+h), (0, 225, 225), 2)
    # print(max_val)
    # show_img(img)

    # 過濾區域
    threshold = .60
    yloc, xloc = np.where(result >= threshold)

    # 準備合併相似區域
    rectangles = list()
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    # 合併相似區域
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    # for (x, y, w, h) in rectangles:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 225), 2)
    # show_img(img)

    return rectangles


def grab_screen_and_click(target_filename):
    # The simplest use, save a screen shot of the 1st monitor
    with mss() as sct:
        myScreen = sct.shot(mon=config_data["screen_num"], output='imgs/myScreen.png')
        # sct_img = np.array(sct.grab(monitor))
    #     mss.tools.to_png(sct_img.rgb, sct_img.size, output='imgs/myScreen.png')
    # match_img('imgs/myScreen.png')
    print("matching "+target_filename)
    rectangles = match_img(myScreen, target_filename)
    return click_match(rectangles)


def wait_wave():
    with mss() as sct:
        while True:
            time.sleep(0.5)
            print("waiting")
            myScreen = sct.shot(mon=config_data["screen_num"], output='imgs/myScreen.png')
            rectangles = match_img(myScreen, "wave")
            if len(rectangles) > 0:
                print("enter a new wave")
                time.sleep(5)
                break
