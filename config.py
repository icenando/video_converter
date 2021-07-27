#! python3

# config.py - configuration variables for 'convert_video.py'

from os import path

import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler(
            filename=path.join("logs","debug.log"),
            mode='a',
            maxBytes=1024*1024,
        )
    ]
)
logger = logging.getLogger('main')


input_folder = "input_videos"
output_folder = "output_videos"
log_folder = "logs"

resolutions = [
    "1920x1080",
    "1080x1920",
    "1080x1080",
    "1350x1080"
]

codecs = [
    "h264"
]

formats = [
    "mp4"
]