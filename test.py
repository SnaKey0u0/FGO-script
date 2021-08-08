import tkinter as tk
from tkinter import filedialog as fd
import main as m


# 限制只能輸入數字
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
        initialdir='C:\\Users\\jacky\\Desktop\\FGO-script\\imgs',
        filetypes=filetypes)
    if filename != '':
        server.config(text=filename.split('/')[-1][:-4])


def select_script():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='C:\\Users\\jacky\\Desktop\\FGO-script\\scripts',
        filetypes=filetypes)
    if filename != '':
        script.config(text=filename.split('/')[-1][:-4])


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
header_label = tk.Label(window, text='神遊快樂腳本', bg='white', font=('TkDefaultFont', 16)).grid(column=0, row=0, padx=0, pady=5)

# input
loop_label = tk.Label(window, text='Loop次數', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=1, padx=0, pady=5)
loop = tk.Entry(window, validate='key', validatecommand=vcmd).grid(column=1, row=1, padx=0, pady=5)

# 下拉選單
team_label = tk.Label(window, text='使用隊伍', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=2, padx=0, pady=5)
variable = tk.StringVar(window)
variable.set(use_team[0])
team = tk.OptionMenu(window, variable, *use_team).grid(column=1, row=2, padx=0, pady=5)

# 下拉選單
use_class_label = tk.Label(window, text='使用職階', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=3, padx=0, pady=5)
variable = tk.StringVar(window)
variable.set(use_class[0])
use_class = tk.OptionMenu(window, variable, *use_class).grid(column=1, row=3, padx=0, pady=5)

# file
server_label = tk.Label(window, text='使用從者', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=4, padx=0, pady=5)
server = tk.Button(window, text='選擇檔案', command=select_img)
server.grid(column=1, row=4, padx=0, pady=5)

# file
script_label = tk.Label(window, text='使用腳本', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=5, padx=0, pady=5)
script = tk.Button(window, text='選擇檔案', command=select_script)
script.grid(column=1, row=5, padx=0, pady=5)

# 下拉選單
prefer_color_label = tk.Label(window, text='優先卡色', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=6, padx=0, pady=5)
variable = tk.StringVar(window)
variable.set(card_color[0])
prefer_color = tk.OptionMenu(window, variable, *card_color).grid(column=1, row=6, padx=0, pady=5)

# 單選
prefer_weak_label = tk.Label(window, text='優先弱點', bg='white', font=('TkDefaultFont', 12)).grid(column=0, row=7)
radioValue = tk.IntVar()
rdioYes = tk.Radiobutton(window, text='是', variable=radioValue, value=1).grid(column=1, row=7, padx=0, pady=5)
rdioNo = tk.Radiobutton(window, text='否', variable=radioValue, value=0).grid(column=2, row=7, padx=0, pady=5)

# 測試與開始按鈕
testShot_btn = tk.Button(window, text='測試截圖', command=m.testshot).grid(column=0, row=8, padx=0, pady=5)
gogo_btn = tk.Button(window, text='開始執行', command=m.gogo).grid(column=1, row=8, padx=0, pady=5)

# 運行主程式
window.mainloop()
