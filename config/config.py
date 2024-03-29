#! python3

# config.py - configuration variables for 'convert_video.py'

from os import path, makedirs

import logging
from logging.handlers import RotatingFileHandler
import json


### Needed for pyinstaller to locate vars.json ###
# pyinstaller --add-data './config/vars.json:./config/' manager.py
abs_path = path.split(path.dirname(__file__))[:-1]
abs_path = path.join(*abs_path)
###

def check_folder_exists(folders: list) -> None:
    assert(type(folders) == list)
    for folder in folders:
        if path.exists(folder):
            pass
        else:
            makedirs(path.join(abs_path, folder))
    pass


check_folder_exists(['logs'])


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler(
            filename=path.join(abs_path, "logs","debug.log"),
            mode='a',
            maxBytes=1024*1024,
            backupCount=3
        )
    ]
)
logger = logging.getLogger('main')


vars_file = path.join(abs_path, 'config','vars.json')
with open(vars_file, 'r') as f:
    vars = json.load(f)

input_file = vars["input_file"]
output_folder = vars["output_folder"]

resolutions = [tuple(vars['resolutions'][res]) for res in vars['resolutions']]

formats = [vars['formats'][i] for i in vars['formats']]

codecs = [vars['codecs'][i] for i in vars['codecs']]