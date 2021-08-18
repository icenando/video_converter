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
import json


Window.size = (900, 700)
Builder.load_file('UI/app.kv')


class MainWindow(Widget):

    selected_res = {}
    cwd = getcwd()
    
    input_file_chooser = ObjectProperty(None)
    output_folder_chooser = ObjectProperty(None)
    confirm_btn = ObjectProperty(None)


    def process_file(self):
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
        
        try:
            vars['input_file'] = (input_file := self.input_file_chooser.selection[0])
            logger.debug(f'input file set to: {input_file}')
            
            vars['output_folder'] = (output_folder := self.output_folder_chooser.selection[0])
            logger.debug(f'input file set to: {output_folder}')
            
        except IndexError:
            logger.critical(
                'process_file() was called without a valid input_file or output_folder.'
            )
            print('Critical error: view logs for details.')
            quit()

        self._update_vars_file(vars)
        resolutions_list = [self.selected_res[i] for i in self.selected_res]
        process_video(input_file, output_folder, resolutions_list)
        logger.debug("Returned to app.")
        
        # Deselecting input file
        self.update_labels('selected_file', '')
        self.input_file_chooser.selection = ''
        self.confirm_btn.disabled = True


    def update_labels(self, label_id, label_val):
        label_to_update = getattr(self.ids, label_id)
        if label_val:
            label_to_update.text = label_val[0]
        else:
            label_to_update.text = "No selection"
            
        self.check_valid_selections()
        pass


    def checkbox_click(self, value, res):
        if value == True:
            self.selected_res[res] = tuple(map(int, res.split('x')))

        else:
            self.selected_res.pop(res)

        resolutions = [None] * 1
        if self.selected_res:
            for res in self.selected_res:
                if resolutions[0] == None:
                    resolutions[0] = res
                else:
                    resolutions[0] += f', {res}'
        else:
            resolutions = []

        self.update_labels('resolutions_list', resolutions)


    def check_valid_selections(self):
        if self.input_file_chooser.selection \
                and self.output_folder_chooser.selection \
                and self.selected_res:
            self.confirm_btn.disabled = False
        else:
            self.confirm_btn.disabled = True
        
        pass


    def close_app(self):
        quit()
        

    def _update_vars_file(self, updated_values):
        logger.debug('Updating vars_file')
        with open(vars_file, 'w', encoding='utf-8') as f:
            json.dump(updated_values, f, ensure_ascii='False', indent=4)


class MainApp(App):
    def build(self):
        self.title = "Video Converter"
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
