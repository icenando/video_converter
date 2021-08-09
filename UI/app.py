#! python3

# app.py - main app window for ../convert_video.py

from config.config import logger, vars_file, vars
from convert_video import process_video

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

from os import getcwd
import json


Window.size = (900, 700)
Builder.load_file('app.kv')


class MainWindow(Widget):

    cwd = getcwd()

    def choose_file_folder(self, chooser: str, f_name: str):
        try:
            assert(chooser == 'folder' or chooser == 'file')
        except AssertionError:
            pass

        if chooser == "file":
            vars['input_file'] = f_name
            logger.debug(f'input file set to: {f_name}')
        else:
            vars['output_folder'] = f_name
            logger.debug(f'input file set to: {f_name}')

        self._update_vars_file(vars)

        process_video(f_name)

        logger.debug("Returned to app.")

    def close_app(self):
        quit()

    def _update_vars_file(self, updated_values):
        logger.debug('Updating vars_file')
        with open(vars_file, 'w', encoding='utf-8') as f:
            json.dump(updated_values, f, ensure_ascii='False', indent=4)


class MainApp(App):
    def build(self):
        self.title = "Choose an input file"
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
