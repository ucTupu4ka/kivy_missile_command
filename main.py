from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config


# Устанавливаем размер окна:
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.write()


class Game(Widget):
    pass


class GameApp(App):
    def build(self):
        game = Game()
        return game


if __name__ == '__main__':
    GameApp().run()
