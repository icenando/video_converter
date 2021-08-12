#! python3

# app.py - main app window for ../convert_video.py

from config.config import logger, vars_file, vars
from convert_video import process_video

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from os import getcwd
# import json


Window.size = (900, 700)
Builder.load_file('UI/app.kv')


class MainWindow(Widget):

    selected_res = {}
    cwd = getcwd()
    
    input_file_chooser = ObjectProperty(None)
    output_folder_chooser = ObjectProperty(None)
    confirm_btn = ObjectProperty(None)


    def choose_file_folder(self, chooser: str, f_name: str):
        try:
            assert(chooser == 'folder' or chooser == 'file')
        except AssertionError:
            logger.critical(
                '''
                choose_file_folder() was called 
                without a valid 'chooser' argument.
                '''
            )
            quit()
        try:
            assert(self.selected_res)
        except AssertionError:
            logger.critical(
                '''
                choose_file_folder() was called 
                without a valid resolution list.
                '''
            )
            quit()

        if chooser == "file":
            vars['input_file'] = f_name
            logger.debug(f'input file set to: {f_name}')
        else:
            vars['output_folder'] = f_name
            logger.debug(f'input file set to: {f_name}')

        # self._update_vars_file(vars)
        resolutions_list = [self.selected_res[i] for i in self.selected_res]
        process_video(f_name, resolutions_list)
        logger.debug("Returned to app.")


    def update_labels(self, label_id, label_val):
        label_to_update = getattr(self.ids, label_id)
        if label_val:
            label_to_update.text = label_val[0]
            self.check_valid_selections()
        else:
            label_to_update.text = "No selection"
            pass

    def checkbox_click(self, value, res):
        if value == True:
            self.selected_res[res] = tuple(map(int, res.split('x')))
        else:
            self.selected_res.pop(res)
    
        self.check_valid_selections()


    def check_valid_selections(self):
        if self.input_file_chooser.selection \
                and self.output_folder_chooser.selection \
                and self.selected_res:
            self.confirm_btn.disabled = False
        else:
            self.ids.confirm_btn.disabled = True
        
        pass


    def close_app(self):
        quit()
        

    # def _update_vars_file(self, updated_values):
    #     logger.debug('Updating vars_file')
    #     with open(vars_file, 'w', encoding='utf-8') as f:
    #         json.dump(updated_values, f, ensure_ascii='False', indent=4)


class MainApp(App):
    def build(self):
        self.title = "Video Converter"
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
