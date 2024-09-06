from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout()

        self.text=TextInput()
        layout.add_widget(self.text)

        self.result=Label()
        layout.add_widget(self.result)

        button = Button(text='hisoblash')
        button.bind(on_press=self.on_click)
        layout.add_widget(button)
        return layout
    def on_click(self, instance):
        try:
            a=str(eval(self.text.text))
            self.result.text=a
        except:
            self.result.text='xato amal'

if __name__ == '__main__':
    MyApp().run()
