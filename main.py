from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        label = Label(text='Hello from Python!', font_size='24sp', color=(0.2, 0.6, 1, 1))
        button = Button(text='Click me!', size_hint=(1, 0.3), on_press=self.on_button_press)
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        instance.text = 'Clicked!'

if __name__ == '__main__':
    MyApp().run()