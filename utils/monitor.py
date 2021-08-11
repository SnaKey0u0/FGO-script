import cv2
import time
import numpy as np
from mss import mss
from utils.mouse_clicker import *

rate = 0.5
config_data = {}


def set_config(config):
    global config_data
    config_data = config


def show_img(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def click_match(rectangles):
    # 點擊第一個位置
    if(len(rectangles) > 0):
        (x, y, w, h) = rectangles[0]
        click(x*(1/rate)+w, y*(1/rate)+h)
        return True
    else:
        print("no match")
        return False


def grab_screen():
    # The simplest use, save a screen shot of the 1st monitor
    with mss() as sct:
        # myScreen = sct.shot(mon=config_data["screen_num"], output='imgs/myScreen.png')
        sct_img = np.array(sct.grab(sct.monitors[config_data["screen_num"]]))
    # mss.tools.to_png(sct_img.rgb, sct_img.size, output='imgs/myScreen.png')
    # match_img('imgs/myScreen.png')
    return cv2.cvtColor(sct_img, cv2.COLOR_BGRA2BGR)


def match_img(myScreen, target_filename):
    img = cv2.resize(myScreen, (0, 0), fy=rate, fx=rate)
    # 解決中文路徑問題
    target_img = cv2.imdecode(np.fromfile('imgs/'+target_filename+'.png', dtype=np.uint8), -1)
    target_img = cv2.cvtColor(target_img, cv2.COLOR_BGRA2BGR)
    # target_img = cv2.imread('imgs/'+target_filename+'.png')
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
    myScreen = grab_screen()
    print("matching "+target_filename)
    rectangles = match_img(myScreen, target_filename)
    return click_match(rectangles)


def wait_until(target_filename):
    start = time.time()
    while True:
        now = time.time()
        if (now - start) > 30:
            print("opps! something went wrong, script stop!")
            return False
        time.sleep(0.3)
        print("waiting for", target_filename)
        myScreen = grab_screen()
        rectangles = match_img(myScreen, target_filename)
        if len(rectangles) > 0:
            if target_filename == "wave":
                print("enter a new wave")
                time.sleep(8)
            else:
                print("ending game")
            return True


def switch_server(front, back):
    # 目前沒用
    myScreen = grab_screen()
    myScreen = cv2.cvtColor(myScreen, cv2.COLOR_BGR2GRAY)
    img = myScreen[375:650, 95:1780]
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    # oring = img
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 999, 2)
    # img = cv2.Canny(img, 400, 800)
    kernel = np.ones((5, 5), np.uint8)
    # img = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel)
    # img = cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel)
    img = cv2.dilate(img, kernel, iterations=4)
    img = cv2.erode(img, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(hierarchy)
    contours = contours[5::-1]
    M = cv2.moments(contours[front-1])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    click(cX*2+95, cY*2+375)
    time.sleep(1)
    M = cv2.moments(contours[back-1])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    click(cX*2+95, cY*2+375)
    time.sleep(1)

    # print(len(contours))
    # for c in contours[5::-1]:
    #     M = cv2.moments(c)
    #     cX = int(M["m10"] / M["m00"])
    #     cY = int(M["m01"] / M["m00"])
    #     cv2.circle(oring, (cX, cY), 15, (0, 255, 255), 2)
    #     cv2.drawContours(oring, [c], -1, (0, 255, 0), 2)
    #     show_img(oring)


def select_team(team_num):
    myScreen = grab_screen()
    myScreen = cv2.cvtColor(myScreen, cv2.COLOR_BGR2GRAY)
    img = myScreen[85:115, 765:1120]
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img = cv2.medianBlur(img, 5)
    img = 255-img
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=2)
    img = cv2.erode(img, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    foo = list()
    for c in contours:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # print(cX)
        foo.append((cX, cY))
    foo.sort()
    click(foo[team_num][0]*2+765, foo[team_num][1]*2+85)
    time.sleep(1)
    click(foo[team_num-1][0]*2+765, foo[team_num-1][1]*2+85)


def select_card(prefer_card, prefer_weak):
    myScreen = grab_screen()
    myScreen = myScreen[525:, :, :]
    rectangles_card = match_img(myScreen, prefer_card)
    pos_score = [0, 0, 0, 0, 0]
    for (x, y, w, h) in rectangles_card:
        closest = 999
        for i in range(0, 5):
            pos = config_data["card"+str(i+1)]
            if closest > abs(x*2 - pos[0]):
                closest = abs(x*2 - pos[0])
                index = i
        pos_score[index] += 1
    if prefer_weak:
        rectangles_weak = match_img(myScreen, "weak")
        for (x, y, w, h) in rectangles_weak:
            closest = 999
            for i in range(0, 5):
                pos = config_data["card"+str(i+1)]
                if closest > abs(x*2 - pos[0]):
                    closest = abs(x*2 - pos[0])
                    index = i
            pos_score[index] += 2
    pos_score = sorted(range(len(pos_score)), key=lambda k: pos_score[k])
    pos_score.reverse()
    for i in range(3):
        print("card", pos_score[i]+1)
        pos = config_data["card"+str(pos_score[i]+1)]
        click(pos[0], pos[1])
        time.sleep(1)
