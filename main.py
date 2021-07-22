from numpy import array
from utils.loader import *
from utils.executor import *


def gogo(info_obj):
    config_data = load_config()
    set_config(config_data)
    start_playing(info_obj)


if __name__ == '__main__':
    # 設定流程
    # use_team = 3
    # use_class = "術"
    loop = 2
    use_server = "CBA"
    instructions = []
    wave_1 = [[1, 1, 2]]
    wave_2 = []
    wave_3 = []
    instructions.append(wave_1)
    instructions.append(wave_2)
    instructions.append(wave_3)

    # 開始腳本
    info_obj = {"loop": loop, "server": use_server, "instructions": instructions}
    gogo(info_obj)
