from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        label = Label(text='Kivy + PyInstaller + Windows issue solution')
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()

