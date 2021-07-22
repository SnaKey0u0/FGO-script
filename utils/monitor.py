import cv2
import os
from mss import mss
import numpy as np
from utils.mouse_clicker import *

rate = 0.5
target_filename = ""


def show_img(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def do_click(myScreen):
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

    # 回傳第一個位置
    if(len(rectangles) > 0):
        (x, y, w, h) = rectangles[0]
        click(x*(1/rate)+w//2, y*(1/rate)+h//2)
    else:
        print("no match")


def grab_screen_and_click(file_name, screen_num=2):
    # The simplest use, save a screen shot of the 1st monitor
    # print("filename", file_name)
    global target_filename
    target_filename = file_name
    with mss() as sct:
        myScreen = sct.shot(mon=screen_num, output='imgs/myScreen.png')
    print("target_filename", target_filename)
    do_click(myScreen)