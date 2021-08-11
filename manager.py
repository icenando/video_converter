#! python3

# manager.py - exports PYTHONPATH environemnt variable and starts main app.

from UI.app import MainApp

from os import path, environ

PYTHONPATH = path.join('..', 'video_converter')
environ['PYTHONPATH'] = PYTHONPATH


MainApp().run()