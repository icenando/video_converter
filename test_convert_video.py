#! python3

# test_convert_video.py - tests for 'convert_video.py'
# Requires pytest.


from os import path, remove, removedirs
from config import input_folder

from convert_video import check_folder_exists, list_videos



def test_folder_created():
    test_folder = 'test_folder'
    check_folder_exists([test_folder])
    new_folder = path.exists(test_folder)
    assert new_folder == True
    if new_folder:
        removedirs(test_folder)        

def test_videos_listed():
    test_video = 'test_video.mov'
    test_video_path = path.join(input_folder, test_video)
    with open(test_video_path, 'w') as video:
        pass
    videos = list_videos(input_folder)
    assert test_video in videos
    remove(test_video_path)

