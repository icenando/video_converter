#! python3

# test_convert_video.py - tests for 'convert_video.py'
# Requires pytest.


from os import path, listdir
from convert_video import check_folder_exists, crop_video
import shutil


test_folder = 'test_folder'
test_video = 'test_video.mov'
test_video_path = path.join(test_folder, test_video)


def _teardown(folder_to_delete):
    shutil.rmtree(folder_to_delete)
    pass

def test_folder_created() -> None:
    check_folder_exists([test_folder])
    new_folder = path.exists(test_folder)
    assert new_folder is True
    _teardown(test_folder)


class TestCropVideo():
    
    test_input_video_folder = path.join('tests', 'test_videos', 'input')
    test_input_video = 'test_input_video.mp4'
    test_output_video_folder = path.join('tests', 'test_videos', 'output')
    check_folder_exists([test_output_video_folder])
    test_in_file_with_path = path.join(test_input_video_folder, test_input_video)
    
    test_resolutions = [  # (width, height)
        (200, 200),
        (100, 150),
    ]
    
    def test_crop_video(self) -> None:
        task = crop_video(
            self.test_resolutions,
            self.test_in_file_with_path,
            self.test_input_video,
            self.test_output_video_folder,
        )
        assert len(listdir(self.test_output_video_folder)) == len(self.test_resolutions)
        _teardown(self.test_output_video_folder)


if __name__ == '__main__':
    test_folder_created()
    TestCropVideo().test_crop_video()