#! python3

# convert_video.py - converts videos to selected resolution,
# codec and format.


# from moviepy import *
from os import makedirs, path, listdir
from pprint import pformat
from config import *
import asyncio


def check_folder_exists(folders: list) -> None:
    for folder in folders:
        if path.exists(folder):
            pass
        else:
            makedirs(folder)
    pass


def list_videos(selected_folder: str) -> list:
    videos_list = []
    for f in listdir(selected_folder):
        if path.isfile(path.join(selected_folder, f)) and not f.startswith('.'):
            videos_list.append(f)
    return videos_list


async def crop_video(videos: str) -> None:
    # TODO: convert each video to selected resolution.
    # if selected resolution is larger than the
    # original video, zoom in and crop.
    pass


async def main() -> None:
    logger.debug('Starting main()')

    check_folder_exists([input_folder, output_folder, log_folder])

    videos = list_videos(input_folder)

    if videos:
        logger.debug('List of videos acquired: ' + pformat(videos))
        tasks = asyncio.gather(
            *[crop_video(video) for video in videos]
        )
        await tasks
    else:
        logger.debug('No videos in folder. Exiting programme')
        quit()

    logger.debug('Finished runnning main(). Exiting programme')
    pass


if __name__ == '__main__':
    asyncio.run(main())
