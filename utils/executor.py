import time
from utils.monitor import *
from utils.mouse_clicker import *

config_data = {}


def start_playing(info_obj):
    grab_screen_and_click("select_episode")
    time.sleep(2)
    grab_screen_and_click(info_obj["server"])
    time.sleep(2)
    grab_screen_and_click("start_episode")
    time.sleep(10)


def set_config(config):
    global config_data
    config_data = config


def use_master_skill(instructs):
    return "use_master_skill"


def print_config():
    print(config_data)
