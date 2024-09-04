from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    title = 'Calculator'
    def build(self):
        self.layout=FloatLayout()
        self.input=TextInput(hint_text='salom', size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.5}, background_color=(0,255,0), foreground_color=(255,0,0))
        self.button=Button(text='click', size_hint=(0.2,0.1), pos_hint={'x': 0.6, 'y': 0.5}, background_color=(0,255,0))
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)
        return self.layout

MyApp().run()
