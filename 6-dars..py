from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.app import App

class FileApp(App):
    def build(self):
        self.layout=BoxLayout(orientation='vertical')

        self.chooser=FileChooserIconView()
        self.layout.add_widget(self.chooser)

        self.load_button=Button(text='select')
        self.load_button.bind(on_press=self.load)

        self.result=Label(text='please select a file')

        self.layout.add_widget(self.result)
        self.layout.add_widget(self.load_button)
        return self.layout

    def load(self, instance):
        selected=self.chooser.selection
        try:
            self.result.text=f'selected file: {selected[0]}'
        except:
            self.result.text=f'please select a file'

FileApp().run()


