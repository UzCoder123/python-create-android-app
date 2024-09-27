from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class PopupApp(App):
    def build(self):
        self.layout=BoxLayout(orientation='vertical')
        self.button=Button(text='popupni ochish')
        self.button.bind(on_press=self.open)
        self.layout.add_widget(self.button)
        return self.layout

    def open(self, instance):
        self.content=BoxLayout(orientation='vertical')
        self.label=Label(text='bu popup')
        self.close=Button(text='popupni yopish')
        self.content.add_widget(self.label)
        self.content.add_widget(self.close)
        self.close.bind(on_press=self.close_popup)
        self.popup=Popup(title='popup misol', content=self.content, size_hint=(0.6,0.3), auto_dismiss=True)
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

if __name__ == '__main__':
    PopupApp().run()
