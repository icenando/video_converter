#! python3

# convert_video.py - converts videos to selected resolution,
# codec and format.


from moviepy import *
from os import makedirs, path



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



def check_folder_exists(folders: list) -> None:
    for folder in folders:
        if path.exists(folder):
            pass
        else:
            makedirs(folder)
    pass


def main() -> None:    
    check_folder_exists([input_folder, output_folder, log_folder])
    

    pass



if __name__ == '__main___':
    main()
