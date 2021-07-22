import json
import os

def load_config():
    with open(os.path.dirname(__file__)+'\\..\\positions_config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
    return config_data
