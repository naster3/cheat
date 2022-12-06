import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (320, 600)


class MusicScreen(Screen):
    pass


class SongCover(MDBoxLayout):
    angle = NumericProperty()

    def rotate(self):
        pass

    def play(self):
        pass


class MainApp(MDApp):
    def build(self):
        return MusicScreen()


MainApp().run()
