from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
import os
import subprocess

from protonqt import run_proton_qt

class ExeBrowser(BoxLayout):
    def __init__(self, **kwargs):
        super(ExeBrowser, self).__init__(**kwargs)
        self.file_chooser = FileChooserListView(filters=["*.exe"])
        self.add_widget(self.file_chooser)
        self.open_button = Button(text="Open", size_hint=(1, 0.1), background_color=(0.5, 0.5, 0.5, 1), font_size=24)
        self.add_widget(self.open_button)
        self.open_button.bind(on_press=self.open_exe)
        self.status_label = Label(text="", size_hint=(1, 0.1), font_size=24)
        self.add_widget(self.status_label)

    def open_exe(self, instance):
        file_path = os.path.join(self.file_chooser.path, self.file_chooser.selection[0])
        if file_path.endswith('.exe'):
            # subprocess.Popen(file_path)
            run_proton_qt(file_path)
            self.status_label.text = "File opened successfully!"
        else:
            self.status_label.text = "Invalid file format. Please select a .exe file."

class ExeApp(App):
    def build(self):
        Builder.load_file('style.kv')
        self.title = "Exe File Browser"
        # self.icon = "path/to/icon.png"
        return ExeBrowser()

if __name__ == '__main__':
    ExeApp().run()
