#! python3

# manager.py - exports PYTHONPATH environemnt variable and starts main app.

from UI.app import MainApp

from os import path, environ

PYTHONPATH = path.join('..', 'video_converter')
environ['PYTHONPATH'] = PYTHONPATH
environ['KIVY_NO_ARGS'] = '1'


MainApp().run()