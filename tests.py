#! python3

# tests.py - tests for 'convert_video.py'


import unittest
from os import path, remove, removedirs
from config import input_folder

from convert_video import check_folder_exists, list_videos



class TestConvertVideoFunctions(unittest.TestCase):

    def test_folder_created(self):
        test_folder = 'unittest_folder'
        check_folder_exists([test_folder])
        new_folder = path.exists(test_folder)
        self.assertTrue(new_folder)
        if new_folder:
            removedirs(test_folder)        

    def test_videos_listed(self):
        test_video = 'unittest_video.mov'
        test_video_path = path.join(input_folder, test_video)
        with open(test_video_path, 'w') as video:
            pass
        videos = list_videos(input_folder)
        self.assertIn(test_video, videos)
        remove(test_video_path)



if __name__=='__main__':
    unittest.main()
