from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
    title = 'Calculator'
    def build(self):
        self.layout=FloatLayout()
        self.text=Label(text='Hello World!', font_size=20, pos_hint={'x':0.5,'y':0.5})
        self.layout.add_widget(self.text)
        return self.layout

MyApp().run()
