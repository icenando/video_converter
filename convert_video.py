#! python3

# convert_video.py - converts videos to selected resolution,
# codec and format.

from config.config import output_folder, logger, \
    formats, check_folder_exists

from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.video.fx.all as vfx
from pprint import pformat

from os import path


def crop_video(
            resolutions: list,
            in_file: str,
            filename: str,
            out_folder: str,
        ) -> None:

    out_file = path.join(out_folder, filename)

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


def process_video(file_to_process: str, resolutions: list) -> None:
    check_folder_exists([output_folder])

    logger.debug('Starting main()')

    logger.debug('Input videos acquired: ' + pformat(file_to_process))

    filename = path.split(file_to_process)[1]

    try:
        crop_video(
            resolutions,
            file_to_process,
            filename,
            output_folder,
        )
        logger.debug('Finished runnning process_file(). Returning to app.')

    except KeyboardInterrupt:
        logger.debug('KeyboardInterrupt - exiting.')

    pass


if __name__ == '__main__':
    from config.config import input_file, resolutions
    process_video(input_file, resolutions)
