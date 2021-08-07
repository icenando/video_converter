#! python3

# convert_video.py - converts videos to selected resolution,
# codec and format.

from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.video.fx.all as vfx
from os import path, listdir
from pprint import pformat
from config.config import *
import asyncio


def list_videos(selected_folder: str) -> list:
    videos_list = []
    for f in listdir(selected_folder):
        if path.isfile(path.join(selected_folder, f)) \
                        and not f.startswith('.'):
            videos_list.append(f)
    return videos_list


async def crop_video(
                    resolutions,
                    in_folder: str,
                    out_folder: str,
                    video_file: str
                ) -> None:

    in_file = path.join(in_folder, video_file)
    out_file = path.join(out_folder, video_file)

    for res in resolutions:
        with VideoFileClip(in_file, audio=True,) as f:
            if res[0]/res[1] == f.aspect_ratio:
                needs_cropping = False
                new_res = res
            else:
                needs_cropping = True
                new_res = (res[1] * f.aspect_ratio, res[1])

            logger.debug(
                'Resizing to ' + str(new_res[0]) + 'x' + str(new_res[1])
            )
            f = vfx.resize(f, new_res)

            if needs_cropping:
                logger.debug(
                    'Cropping to ' + str(res[0]) + 'x' + str(res[1])
                )
                f = vfx.crop(
                    f,
                    x_center=new_res[0]//2,
                    y_center=res[1]//2,
                    width=res[0],
                    height=res[1]
                    )

            for format in formats:
                logger.debug('Exporting...')
                f.write_videofile(out_file[:-4]+'_'+str(res)+format)
    pass


async def main() -> None:
    check_folder_exists([input_folder, output_folder])

    logger.debug('Starting main()')

    videos = list_videos(input_folder)

    if videos:
        logger.debug('List of videos acquired: ' + pformat(videos))
        tasks = asyncio.gather(
            *[crop_video(
                resolutions,
                input_folder,
                output_folder,
                video) for video in videos]
        )
        await tasks
    else:
        logger.debug('No videos in folder. Exiting programme')
        quit()

    logger.debug('Finished runnning main(). Exiting programme')
    pass


if __name__ == '__main__':
    asyncio.run(main())
