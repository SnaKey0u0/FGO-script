from mss import mss
from utils.loader import *
from utils.executor import start_playing, set_config as set_executor
from utils.monitor import set_config as set_monitor
from utils.mouse_clicker import set_config as set_mouse_clicker


def gogo(info_obj):
    config_data = load_config()
    set_executor(config_data)
    set_monitor(config_data)
    set_mouse_clicker(config_data)
    start_playing(info_obj)


def testshot():
    with mss() as sct:
        sct.shot(mon=1, output='imgs/myScreen.png')


if __name__ == '__main__':
    # 基本設定
    loop = 2  # 無用

    # 流程設定
    use_team = 3  # 無用
    use_class = "術"  # 無用
    use_server = "CBA"
    instructions = list()
    wave_1 = [[2, 1, 1], [3, 1, 1], ["CLOTH", 3, 1], ["ATTACK", 1]]
    wave_2 = [[1, 3], [2, 3, 1], ["ATTACK", 1]]
    wave_3 = [[2, 2], [3, 2], [3, 3, 1], ["ATTACK", 1]]
    instructions.append(wave_1)
    instructions.append(wave_2)
    instructions.append(wave_3)

    # 開始腳本
    info_obj = {"loop": loop,
                "team": use_team,
                "class": use_class,
                "server": use_server,
                "instructions": instructions}
    gogo(info_obj)
