from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.button import Button

class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='2-ekranga o\'tish', on_press=self.almashtirish))
    def almashtirish(self, instance):
        self.manager.current = 'second'

class Second(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='1-ekranga o\'tish', on_press=self.almashtirish))
    def almashtirish(self, instance):
        self.manager.current = 'first'

class ScreenApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(First(name='first'))
        sm.add_widget(Second(name='second'))
        return sm

ScreenApp().run()
