import json
import ctypes
import tkinter.filedialog as fd
import tkinter.messagebox as msg
import threading
from utils.logger import *
from utils.monitor import set_config as set_monitor, testshot as ts
from utils.window_controller import ask_config
from utils.executor import start_playing, summon, gift, set_config as set_executor
from tkinter import NORMAL, DISABLED, PhotoImage, Label, Entry, StringVar, OptionMenu, Button, Tk

config_data = {}
myThread = None


class motherHandler(threading.Thread):
    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


class ExecuteTaskHandler(motherHandler):
    def run(self):
        info_obj = create_info()
        if info_obj != None:
            start_playing(info_obj)
        else:
            msg.showinfo("script error", "請選擇腳本")
        enableBtn()


class SummonTaskHandler(motherHandler):
    def run(self):
        if entry_loop.get() == "":
            n = 999
        else:
            n = int(entry_loop.get())
        summon(n)
        enableBtn()


class GiftTaskHandler(motherHandler):
    def run(self):
        if entry_loop.get() == "":
            n = 999
        else:
            n = int(entry_loop.get())
        gift(n)
        enableBtn()


def load_and_set():
    global config_data
    with open('positions_config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
    width, height = ask_config()
    bias = 0
    if width == 1920:
        bias = 92
    rateX = (width-42-bias) / 1788
    rateY = (height-34) / 1008
    info(rateX)
    info(rateY)
    for k, v in config_data.items():
        config_data[k] = [int(v[0]*rateX), int(v[1]*rateY)]
    set_executor(config_data, rateX, rateY)
    set_monitor(config_data, rateX, rateY)


def gogo():
    global myThread
    load_and_set()
    disableBtn()
    myThread = ExecuteTaskHandler(daemon=True)
    myThread.start()


def testshot():
    load_and_set()
    ts()


def friend_summon():
    global myThread
    load_and_set()
    disableBtn()
    myThread = SummonTaskHandler(daemon=True)
    myThread.start()


def open_gift():
    load_and_set()
    disableBtn()
    myThread = GiftTaskHandler(daemon=True)
    myThread.start()


def num_validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False


def select_script():
    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='scripts',
        filetypes=filetypes)
    if filename != '':
        btn_script.config(text=filename.split('/')[-1])


def create_info():
    try:
        with open("scripts/"+btn_script.cget("text"), "r", encoding="utf-8") as f:
            info_obj = json.load(f)
        if entry_loop.get() == "":
            info_obj["loop"] = 999
        else:
            info_obj["loop"] = int(entry_loop.get())
        info_obj["apples"] = opt_apples.cget("text")
        return info_obj
    except:
        return None


def enableBtn():
    btn_gogo.config(state=NORMAL)
    btn_summon.config(state=NORMAL)
    btn_testshot.config(state=NORMAL)


def disableBtn():
    btn_gogo.config(state=DISABLED)
    btn_summon.config(state=DISABLED)
    btn_testshot.config(state=DISABLED)


def exit():
    myThread.raise_exception()
    enableBtn()


if __name__ == '__main__':

    # init
    window = Tk()
    window.resizable(width=False, height=False)
    vcmd = (window.register(num_validate), '%P')
    apples = ["銅蘋果", "銀蘋果", "金蘋果", "彩色蘋果"]
    # use_class = ["不變更", "全", "劍", "弓", "槍", "騎", "術", "殺", "狂", "外", "混"]
    # card_color = ["不在乎", "B", "A", "Q"]

    # 設定視窗標題、大小和背景顏色
    window.title('FGO-script')
    window.iconbitmap('fgo.ico')
    # window.geometry('320x180')
    # window.configure(background='blue')
    bg = PhotoImage(file="wife.png")
    # bg = bg.subsample(4) #mechanically, here it is adjusted to 32 instead of 320
    bg_label = Label(window, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 標題文字
    Label(window, text='FGO宇宙神遊', bg='white', font=('TkDefaultFont', 16)).grid(column=0, row=0, padx=0, pady=5)

    # input
    Label(window, text='Loop次數', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=1, padx=0, pady=5)
    entry_loop = Entry(window, validate='key', validatecommand=vcmd, width=16)
    entry_loop.grid(column=1, row=1, padx=0, pady=5)

    # 下拉選單
    Label(window, text='體力回復', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=2, padx=0, pady=5)
    variable = StringVar(window)
    variable.set(apples[0])
    opt_apples = OptionMenu(window, variable, *apples)
    opt_apples.grid(column=1, row=2, padx=0, pady=5)

    # # 下拉選單
    #  Label(window, text='使用職階', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=3, padx=0, pady=5)
    # variable =  StringVar(window)
    # variable.set(use_class[0])
    # opt_use_class =  OptionMenu(window, variable, *use_class)
    # opt_use_class.grid(column=1, row=3, padx=0, pady=5)

    # # file
    #  Label(window, text='使用從者', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=4, padx=0, pady=5)
    # btn_server =  Button(window, text='選擇檔案', command=select_img)
    # btn_server.grid(column=1, row=4, padx=0, pady=5)

    # file
    Label(window, text='使用腳本', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=3, padx=0, pady=5)
    btn_script = Button(window, text='選擇檔案', command=select_script)
    btn_script.grid(column=1, row=3, padx=0, pady=5)

    # # 下拉選單
    #  Label(window, text='優先卡色', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=6, padx=0, pady=5)
    # variable =  StringVar(window)
    # variable.set(card_color[0])
    # opt_prefer_color =  OptionMenu(window, variable, *card_color)
    # opt_prefer_color.grid(column=1, row=6, padx=0, pady=5)

    # # 單選
    #  Label(window, text='優先弱點', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=7)
    # radioValue =  IntVar()
    # radioYes =  Radiobutton(window, text='是', variable=radioValue, value=1)
    # radioYes.grid(column=1, row=7, padx=0, pady=5)
    # radioNo =  Radiobutton(window, text='否', variable=radioValue, value=0)
    # radioNo.grid(column=2, row=7, padx=0, pady=5)

    # 按鈕
    btn_testshot = Button(window, text='測試截圖', command=testshot)
    btn_testshot.grid(column=0, row=4, padx=0, pady=4)
    btn_gogo = Button(window, text='開始執行', command=gogo)
    btn_gogo.grid(column=1, row=4, padx=0, pady=4)
    btn_exit = Button(window, text='緊急逃生', command=exit)
    btn_exit.grid(column=2, row=4, padx=0, pady=4)
    btn_summon = Button(window, text='友抽', command=friend_summon)
    btn_summon.grid(column=1, row=0, padx=0, pady=5)
    btn_box = Button(window, text='自動開箱', command=open_gift)
    btn_box.grid(column=2, row=0, padx=0, pady=5)

    # 運行主程式
    window.mainloop()

    # # 基本設定
    # loop = 1

    # # 流程設定
    # use_team = 3  # 無用
    # use_class = "術"  # 無用
    # use_server = "CBA"
    # prefer_color = "B"
    # prefer_weak = True
    # instructions = list()

    # ######################################################################
    # ######################################################################
    # # 指令說明
    # # EX: [1, 2]            => 從者1施放2技(不用選擇目標)
    # # EX: [1, 2, 3]         => 從者1施放2技給從者3
    # # EX: ["CLOTH", 1]      => 使用衣服技能1(不用選擇目標)
    # # EX: ["CLOTH", 1, 2]   => 衣服技能1施放給從者2
    # # EX: ["CLOTH", 3, 2, 6]=> 換人禮裝專用，從者2換從者6
    # # EX: ["ATTACK", 1]     => 開始戰鬥，從者1施放寶具(僅能1人施放)
    # ######################################################################
    # ######################################################################

    # # 雙CBA不換人(2003)
    # # wave_1 = [[2, 1, 1], [3, 1, 1], ["CLOTH", 3, 1], ["ATTACK", 1]]
    # # wave_2 = [[1, 3], [2, 3, 1], ["ATTACK", 1]]
    # # wave_3 = [[2, 2], [3, 2], [3, 3, 1], ["ATTACK", 1]]

    # # 尼祿換人3T
    # # wave_1 = [[2, 1, 1], [2, 2, 1], ["CLOTH", 3, 2, 6], [2, 1, 1], [3, 1, 1], ["ATTACK", 1]]
    # # wave_2 = [[1, 3], [2, 3, 1], ["ATTACK", 1]]
    # # wave_3 = [[2, 2], [3, 2], [3, 3, 1], ["ATTACK", 1]]

    # # 尼祿換人3T V2
    # wave_1 = [[2, 1, 1], [3, 1, 1], ["ATTACK", 1]]
    # wave_2 = [[3, 2], [3, 3, 1], ["CLOTH", 3, 3, 6], [1, 3], [3, 1, 1], [3, 2, 1], ["ATTACK", 1]]
    # wave_3 = [[2, 2], [2, 3, 1], ["CLOTH", 1], ["ATTACK", 1]]

    # instructions.append(wave_1)
    # instructions.append(wave_2)
    # instructions.append(wave_3)

    # info_obj = {"loop": loop,
    #             "team": use_team,
    #             "class": use_class,
    #             "server": use_server,
    #             "instructions": instructions}

    # # 開始腳本
    # gogo(info_obj)
    # # testshot()
