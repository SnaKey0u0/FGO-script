import time
from random import randint
from utils.monitor import *
from utils.mouse_clicker import *

config_data = {}


def set_config(config):
    global config_data
    config_data = config


def print_config():
    print(config_data)


def start_playing(info_obj):
    for i in range(info_obj["loop"]):
        if not grab_screen_and_click("select_episode1"):
            grab_screen_and_click("select_episode2")
        time.sleep(2)
        first = True
        while not grab_screen_and_click(info_obj["server"]):
            if first:
                first = False
            else:
                time.sleep(10)
            grab_screen_and_click("refresh")
            time.sleep(1)
            grab_screen_and_click("yes")
            time.sleep(2)
        time.sleep(2)
        grab_screen_and_click("start_episode")
        for wave in info_obj["instructions"]:
            wait_until("wave")
            for step in wave:
                # 特殊指令
                if isinstance(step[0], str):
                    if step[0] == "CLOTH":
                        use_cloth(step[1:])
                    elif step[0] == "ATTACK":
                        use_ult(step[1:])
                        break
                else:
                    pos = config_data["skill"+str(step[0])+str(step[1])]
                    click(pos[0], pos[1])

                    if(len(step) == 2):
                        time.sleep(4)
                    else:
                        time.sleep(1)
                    # 若是指定技
                    if (len(step) == 3):
                        pos = config_data["select"+str(step[2])]
                        click(pos[0], pos[1])
                        time.sleep(4)
        wait_until("click_screen")
        ending_game()
        time.sleep(8)


def use_cloth(step):
    pos = config_data["cloth"]
    click(pos[0], pos[1])
    time.sleep(1)
    pos = config_data["master-skill"+str(step[0])]
    click(pos[0], pos[1])
    time.sleep(2)

    # 指定技能
    if len(step) == 2:
        pos = config_data["select"+str(step[1])]
        click(pos[0], pos[1])
        time.sleep(2)

    # 換人
    elif len(step) == 3:
        switch_server(step[1], step[2])
        # pos = config_data["switch_pick"+str(step[1])]
        # click(pos[0], pos[1])
        # time.sleep(1)
        # pos = config_data["switch_pick"+str(step[2])]
        # click(pos[0], pos[1])
        grab_screen_and_click("switch")
        time.sleep(2)
    time.sleep(2)


def use_ult(step):
    grab_screen_and_click("attack")
    time.sleep(4)
    pos = config_data["ult"+str(step[0])]
    click(pos[0], pos[1])
    time.sleep(1)
    pos = config_data["card1"]
    click(pos[0], pos[1])
    time.sleep(1)
    pos = config_data["card2"]
    click(pos[0], pos[1])
    time.sleep(1)


def ending_game():
    grab_screen_and_click("click_screen")
    time.sleep(2)
    grab_screen_and_click("click_screen")
    time.sleep(2)
    grab_screen_and_click("next")
    time.sleep(1)
    grab_screen_and_click("close")


def eat_apple():
    grab_screen_and_click("click_screen")
    time.sleep(1)
