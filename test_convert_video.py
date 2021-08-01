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
    test_video = ['test_video', 'test_video.mov']
    check_folder_exists([test_video[0]])  # Creates "test_video" folder
    test_video_path = path.join(test_video[0], test_video[1])
    test_file = open(test_video_path, 'w')  # Creates "test_video/test_video.mov" file
    test_file.close()
    videos = list_videos(test_video[0])
    assert test_video[1] in videos
    remove(test_video_path)
    removedirs(test_video[0])


if __name__ == '__main__':
    test_folder_created()
    test_videos_listed()