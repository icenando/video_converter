#! python3

# convert_video.py - converts videos to selected resolution,
# codec and format.


# from moviepy import *
from os import makedirs, path, listdir
from pprint import pformat
from config import *



def check_folder_exists(folders: list) -> None:
    for folder in folders:
        if path.exists(folder):
            pass
        else:
            makedirs(folder)
    pass


def crop_video(videos: list) -> None:
    #TODO: convert each video to selected resolution.
    # if selected resolution is larger than the 
    # original video, zoom in and crop.
    pass


def main() -> None:    
    logger.debug('Starting main()')

    check_folder_exists([input_folder, output_folder, log_folder])

    videos = [
        f for f in listdir(input_folder) 
            if path.isfile(path.join(input_folder, f)) 
            and not f.startswith('.')
    ]

    if videos:
        logger.debug('List of videos acquired: ' + pformat(videos))
        crop_video(videos)
    else:
        logger.debug('No videos in folder. Exiting programme')
        quit()

    logger.debug('Finished runnning main(). Exiting programme')
    pass



if __name__ == '__main__':
    main()
