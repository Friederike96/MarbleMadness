import json
import os

from constants import game_constants


def load_json_data():
    if os.path.isfile(game_constants.level_data_path):
        with open(game_constants.level_data_path, 'r') as jfile:
            game_constants.level_data_dict = json.loads(jfile.read())
