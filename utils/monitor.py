import cv2
import time
import numpy as np
from utils.logger import *
from utils.window_controller import *

rateX = 1
rateY = 1
config_data = {}


def set_config(config, X, Y):
    global config_data, rateX, rateY
    config_data = config
    rateX = X
    rateY = Y


def show_img(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def testshot(name="myScreen"):
    bmpstr, width, height = getWinBitStr()
    img = np.frombuffer(bmpstr, dtype='uint8')
    img.shape = (height, width, 4)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imwrite(name+".png", img)


def grab_screen_and_click(target_filename):
    myScreen = grab_screen()
    info("matching "+target_filename)
    rectangles = match_img(myScreen, target_filename)
    return click_match(rectangles)


def grab_screen():
    bmpstr, width, height = getWinBitStr()
    # convert the raw data into a format opencv can read
    img = np.frombuffer(bmpstr, dtype='uint8')
    img.shape = (height, width, 4)
    # img = np.ascontiguousarray(img)

    # The simplest use, save a screen shot of the 1st monitor
    # with mss() as sct:
    #     sct_img = np.array(sct.grab(sct.monitors[config_data["screen_num"]]))

    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)


def match_img(myScreen, target_filename):
    # img = cv2.resize(myScreen, (0, 0), fy=rate, fx=rate)

    # 解決中文路徑問題
    target_img = cv2.imdecode(np.fromfile('imgs/'+target_filename+'.png', dtype=np.uint8), -1)
    target_img = cv2.cvtColor(target_img, cv2.COLOR_BGRA2BGR)
    target_img = cv2.resize(target_img, (0, 0), fy=rateY, fx=rateX)

    # 匹配
    result = cv2.matchTemplate(myScreen, target_img, cv2.TM_CCOEFF_NORMED)

    # 定義圖片大小
    w = target_img.shape[1]
    h = target_img.shape[0]

    # 過濾門檻
    threshold = .60

    # 選最像的地方
    if (target_filename == "confirm" or target_filename == "close" or target_filename == "yes"):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > threshold:
            return [(max_loc[0], max_loc[1], w, h)]

    # 篩選高分區域
    yloc, xloc = np.where(result >= threshold)

    # 準備合併相似區域
    rectangles = list()
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    # 合併相似區域
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    return rectangles


def click_match(rectangles):
    # 點擊第一個位置
    if(len(rectangles) > 0):
        (x, y, w, h) = rectangles[0]
        click(x+w*0.5, y+h*0.5)
        return True
    else:
        warning("no match")
        return False


def wait_until(target_filename):
    start = time.time()
    info("waiting for " + target_filename)
    while True:
        now = time.time()
        if (now - start) > 60:
            # cv2.imwrite("ggFuck.png", myScreen)
            error("過場中斷，可能是網路不穩定或電腦卡頓")
            return False
        myScreen = grab_screen()
        rectangles = match_img(myScreen, target_filename)
        if len(rectangles) > 0:
            if target_filename == "wave":
                info("enter a new wave")
                time.sleep(8)
            elif target_filename == "attack":
                info("enter a new wave")
                time.sleep(1)
            else:
                info("ending game")
                time.sleep(1)
            return True
        time.sleep(0.3)


# def switch_server(front, back):
#     # 目前沒用
#     myScreen = grab_screen()
#     myScreen = cv2.cvtColor(myScreen, cv2.COLOR_BGR2GRAY)
#     img = myScreen[375:650, 95:1780]
#     img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#     # oring = img
#     # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = cv2.medianBlur(img, 5)
#     img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 999, 2)
#     # img = cv2.Canny(img, 400, 800)
#     kernel = np.ones((5, 5), np.uint8)
#     # img = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel)
#     # img = cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel)
#     img = cv2.dilate(img, kernel, iterations=4)
#     img = cv2.erode(img, kernel, iterations=1)
#     contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     print(hierarchy)
#     contours = contours[5::-1]
#     M = cv2.moments(contours[front-1])
#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])
#     click(cX*2+95, cY*2+375)
#     time.sleep(1)
#     M = cv2.moments(contours[back-1])
#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])
#     click(cX*2+95, cY*2+375)
#     time.sleep(1)

#     # print(len(contours))
#     # for c in contours[5::-1]:
#     #     M = cv2.moments(c)
#     #     cX = int(M["m10"] / M["m00"])
#     #     cY = int(M["m01"] / M["m00"])
#     #     cv2.circle(oring, (cX, cY), 15, (0, 255, 255), 2)
#     #     cv2.drawContours(oring, [c], -1, (0, 255, 0), 2)
#     #     show_img(oring)


def select_team(team_num):
    # myScreen = grab_screen()

    # r = match_img(myScreen, "teams")
    # if(len(r) > 0):
    #     (x, y, w, h) = r[0]

    img = cv2.imread("imgs/teams.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img = cv2.medianBlur(img, 3)
    img = 255-img
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=2)
    # show_img(img)
    # img = cv2.erode(img, kernel, iterations=4)
    # show_img(img)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(contours))
    try:
        foo = list()
        for c in contours:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # print(cX)
            foo.append((cX, cY))
        foo.sort()
        # 點擊測試
        # for i in range(1, 11):
        #     click(foo[i - 1][0]*2*rateX+config_data["teams"][0], foo[i - 1][1]*2*rateY+config_data["teams"][1])
        #     time.sleep(1)
        # time.sleep(100)
        click(foo[team_num % 10][0]*2*rateX+config_data["teams"][0], foo[team_num % 10][1]*2*rateY+config_data["teams"][1])
        time.sleep(1)
        click(foo[team_num-1][0]*2*rateX+config_data["teams"][0], foo[team_num-1][1]*2*rateY+config_data["teams"][1])
    except Exception as e:
        error(e)
        error("選擇隊伍錯誤，腳本停止")


def select_card(prefer_card, prefer_weak):
    myScreen = grab_screen()
    myScreen = myScreen[int(525*rateY):, :, :]
    rectangles_card = match_img(myScreen, prefer_card)
    pos_score = [0, 0, 0, 0, 0]
    for (x, y, w, h) in rectangles_card:
        closest = 999
        for i in range(0, 5):
            pos = config_data["card"+str(i+1)]
            if closest > abs(x - pos[0]):
                closest = abs(x - pos[0])
                index = i
        pos_score[index] += 1
    if prefer_weak:
        rectangles_weak = match_img(myScreen, "weak")
        for (x, y, w, h) in rectangles_weak:
            closest = 999
            for i in range(0, 5):
                pos = config_data["card"+str(i+1)]
                if closest > abs(x - pos[0]):
                    closest = abs(x - pos[0])
                    index = i
            pos_score[index] += 2
        rectangles_resist = match_img(myScreen, "resist")
        for (x, y, w, h) in rectangles_resist:
            closest = 999
            for i in range(0, 5):
                pos = config_data["card"+str(i+1)]
                if closest > abs(x - pos[0]):
                    closest = abs(x - pos[0])
                    index = i
            pos_score[index] -= 2
    # print(pos_score)
    pos_score = sorted(range(len(pos_score)), key=lambda k: pos_score[k])
    pos_score.reverse()
    for i in range(3):
        info("card " + str(pos_score[i]+1))
        pos = config_data["card"+str(pos_score[i]+1)]
        click(pos[0], pos[1])
        time.sleep(1)
