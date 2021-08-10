import time
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
        print("loop: "+str(i+1))
        first_enter = False
        if not grab_screen_and_click("select_episode1"):
            first_enter = True
            if not grab_screen_and_click("select_episode2"):
                print("opps! something went wrong, script stop!")
                return
        time.sleep(1)
        if not eat_apple(info_obj["apples"]):
            return
        first_refresh = True
        while not grab_screen_and_click(info_obj["server"]):
            if first_refresh:
                first_refresh = False
            else:
                time.sleep(10)
            grab_screen_and_click("refresh")
            time.sleep(1)
            grab_screen_and_click("yes")
            time.sleep(4)
        time.sleep(2)
        select_team(info_obj["team"])
        # 進關前倒數
        time.sleep(3)
        grab_screen_and_click("start_episode")
        for wave in info_obj["instructions"]:
            if not wait_until("wave"):
                return
            for step in wave:
                print("exe ins")
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
                    time.sleep(1)
                    # 指定技
                    if (len(step) == 3):
                        pos = config_data["select"+str(step[2])]
                        click(pos[0], pos[1])
                    time.sleep(4)
        if not wait_until("click_screen"):
            return
        ending_game()
        time.sleep(10)
        if first_enter:
            first_enter = False
            grab_screen_and_click("click_screen")
            time.sleep(4)
    print("finished")


def use_cloth(step):
    pos = config_data["cloth"]
    click(pos[0], pos[1])
    time.sleep(1)
    pos = config_data["master-skill"+str(step[0])]
    click(pos[0], pos[1])
    time.sleep(1)
    # 指定技能
    if len(step) == 2:
        pos = config_data["select"+str(step[1])]
        click(pos[0], pos[1])

    # 換人
    elif len(step) == 3:
        # switch_server(step[1], step[2])
        pos = config_data["switch_pick"+str(step[1])]
        click(pos[0], pos[1])
        time.sleep(1)
        pos = config_data["switch_pick"+str(step[2])]
        click(pos[0], pos[1])
        time.sleep(1)
        grab_screen_and_click("switch")
        time.sleep(2)
    time.sleep(4)


def use_ult(step):
    while not grab_screen_and_click("attack"):
        time.sleep(1)
    time.sleep(4)
    pos = config_data["ult"+str(step[0])]
    click(pos[0], pos[1])
    time.sleep(1)
    pos = config_data["card1"]
    click(pos[0], pos[1])
    time.sleep(1)
    pos = config_data["card2"]
    click(pos[0], pos[1])


def ending_game():
    grab_screen_and_click("click_screen")
    time.sleep(3)
    grab_screen_and_click("click_screen")
    time.sleep(3)
    grab_screen_and_click("next")
    time.sleep(3)
    if grab_screen_and_click("no_apply"):
        time.sleep(1)
    grab_screen_and_click("close")


def eat_apple(apples):
    if not grab_screen_and_click(apples):
        if not grab_screen_and_click("confirm"):
            print("already in episode")
            time.sleep(1)
            return True
        else:
            print("no apple left")
            return False
    time.sleep(1)
    grab_screen_and_click("confirm")
    time.sleep(4)
    return True
