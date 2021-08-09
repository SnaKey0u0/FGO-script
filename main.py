import sys
import json
import tkinter as tk
from threading import Thread
from tkinter import filedialog as fd
from mss import mss
from utils.executor import start_playing, set_config as set_executor
from utils.monitor import set_config as set_monitor
from utils.mouse_clicker import set_config as set_mouse_clicker

config_data = {}


class ExecuteTaskHandler(Thread):

    def run(self):
        info_obj = create_info()
        start_playing(info_obj)
        # 啟用按鈕
        btn_gogo.config(state=tk.NORMAL)
        btn_testshot.config(state=tk.NORMAL)


def load_and_set():
    global config_data
    with open('positions_config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
    set_executor(config_data)
    set_monitor(config_data)
    set_mouse_clicker(config_data)


def gogo():
    # 禁用按鈕
    btn_gogo.config(state=tk.DISABLED)
    btn_testshot.config(state=tk.DISABLED)
    ExecuteTaskHandler(daemon=True).start()


def testshot():
    with mss() as sct:
        sct.shot(mon=config_data["screen_num"], output='myScreen.png')


def num_validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False


def select_img():
    filetypes = (
        ('img files', '*.png'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='imgs',
        filetypes=filetypes)
    if filename != '':
        btn_server.config(text=filename.split('/')[-1][:-4])


def select_script():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='scripts',
        filetypes=filetypes)
    if filename != '':
        btn_script.config(text=filename.split('/')[-1])


def create_info():
    with open("scripts/"+btn_script.cget("text"), "r", encoding="utf-8") as f:
        data = f.read().splitlines()
    final = list()
    for d in data:
        foo = list()
        for i in d.split(','):
            fooo = list()
            for e in i:
                fooo.append(e)
            foo.append(fooo)
        final.append(foo)
    info_obj = {"loop": int(entry_loop.get()),
                "team": opt_team.cget("text"),
                "class": opt_use_class.cget("text"),
                "server": btn_server.cget("text"),
                "instructions": final}
    return info_obj


def exit():
    sys.exit()


if __name__ == '__main__':

    # 匯入設定檔
    load_and_set()

    # init
    window = tk.Tk()
    vcmd = (window.register(num_validate), '%P')
    use_team = ["不變更", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    use_class = ["不變更", "全", "劍", "弓", "槍", "騎", "術", "殺", "狂", "外", "混"]
    card_color = ["不在乎", "B", "A", "Q"]

    # 設定視窗標題、大小和背景顏色
    window.title('FGO-script')
    # window.geometry('640x360')
    window.configure(background='blue')

    # 標題文字
    tk.Label(window, text='神遊快樂腳本', bg='white', font=('TkDefaultFont', 16)).grid(column=0, row=0, padx=0, pady=5)

    # input
    tk.Label(window, text='Loop次數', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=1, padx=0, pady=5)
    entry_loop = tk.Entry(window, validate='key', validatecommand=vcmd)
    entry_loop.grid(column=1, row=1, padx=0, pady=5)

    # 下拉選單
    tk.Label(window, text='使用隊伍', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=2, padx=0, pady=5)
    variable = tk.StringVar(window)
    variable.set(use_team[0])
    opt_team = tk.OptionMenu(window, variable, *use_team)
    opt_team.grid(column=1, row=2, padx=0, pady=5)

    # 下拉選單
    tk.Label(window, text='使用職階', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=3, padx=0, pady=5)
    variable = tk.StringVar(window)
    variable.set(use_class[0])
    opt_use_class = tk.OptionMenu(window, variable, *use_class)
    opt_use_class.grid(column=1, row=3, padx=0, pady=5)

    # file
    tk.Label(window, text='使用從者', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=4, padx=0, pady=5)
    btn_server = tk.Button(window, text='選擇檔案', command=select_img)
    btn_server.grid(column=1, row=4, padx=0, pady=5)

    # file
    tk.Label(window, text='使用腳本', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=5, padx=0, pady=5)
    btn_script = tk.Button(window, text='選擇檔案', command=select_script)
    btn_script.grid(column=1, row=5, padx=0, pady=5)

    # 下拉選單
    tk.Label(window, text='優先卡色', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=6, padx=0, pady=5)
    variable = tk.StringVar(window)
    variable.set(card_color[0])
    opt_prefer_color = tk.OptionMenu(window, variable, *card_color)
    opt_prefer_color.grid(column=1, row=6, padx=0, pady=5)

    # 單選
    tk.Label(window, text='優先弱點', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=7)
    radioValue = tk.IntVar()
    radioYes = tk.Radiobutton(window, text='是', variable=radioValue, value=1)
    radioYes.grid(column=1, row=7, padx=0, pady=5)
    radioNo = tk.Radiobutton(window, text='否', variable=radioValue, value=0)
    radioNo.grid(column=2, row=7, padx=0, pady=5)

    # 按鈕
    btn_testshot = tk.Button(window, text='測試截圖', command=testshot)
    btn_testshot.grid(column=0, row=8, padx=0, pady=5)
    btn_gogo = tk.Button(window, text='開始執行', command=gogo)
    btn_gogo.grid(column=1, row=8, padx=0, pady=5)
    btn_exit = tk.Button(window, text='緊急逃生', command=exit)
    btn_exit.grid(column=2, row=8, padx=0, pady=5)

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
