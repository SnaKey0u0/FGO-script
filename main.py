from mss import mss
from utils.loader import *
from utils.executor import start_playing, set_config as set_executor
from utils.monitor import set_config as set_monitor
from utils.mouse_clicker import set_config as set_mouse_clicker

config_data = {}


def gogo(info_obj):
    global config_data
    config_data = load_config()
    set_executor(config_data)
    set_monitor(config_data)
    set_mouse_clicker(config_data)
    start_playing(info_obj)


def testshot():
    with mss() as sct:
        sct.shot(mon=config_data["screen_num"], output='imgs/myScreen.png')


if __name__ == '__main__':
    # 基本設定
    loop = 2

    # 流程設定
    use_team = 3  # 無用
    use_class = "術"  # 無用
    use_server = "CBA"
    instructions = list()

    # [1,2]             => 從者1施放2技(不用選擇目標)
    # [1,2,3]           => 從者1施放2技給從者3
    # ["CLOTH", 1]      => 使用衣服技能1(不用選擇目標)
    # ["CLOTH", 1, 2]   => 衣服技能1施放給從者2
    # ["CLOTH", 3, 2, 6]=> 換人禮裝專用，從者2換從者6
    # ["ATTACK", 1]     => 開始戰鬥，從者1施放寶具(僅能1人施放)

    # 雙CBA不換人(2003)
    # wave_1 = [[2, 1, 1], [3, 1, 1], ["CLOTH", 3, 1], ["ATTACK", 1]]
    # wave_2 = [[1, 3], [2, 3, 1], ["ATTACK", 1]]
    # wave_3 = [[2, 2], [3, 2], [3, 3, 1], ["ATTACK", 1]]

    # 尼祿換人3T
    wave_1 = [[2, 1, 1], [2, 2, 1], ["CLOTH", 3, 2, 6], [2, 1, 1], [3, 1, 1], ["ATTACK", 1]]
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
    # testshot()
