from kivy.config import Config
# Force a 2400x1080 style wide landscape preview (scaled down to fit your desktop monitor)
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '405')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import os

# Automatically calculate the exact folder path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

Builder.load_string('''
<MenuScreen>:
    canvas.before:
        Color:
            rgba: 0.99, 0.69, 0.44, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: [0, dp(30), 0, dp(30)]
        spacing: dp(20)

        # 1. Game Title Header Area
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            size_hint_y: 0.5
            
            Image:
                source: root.logo_src
                size_hint: None, None
                size: dp(260), dp(70) 
                allow_stretch: True

        # 2. Interactive Button Menu Stack (Perfectly centered on the wide screen)
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(200), dp(160)
            pos_hint: {'center_x': 0.5}
            spacing: dp(10)

            # Start Button
            Button:
                background_normal: root.start_src
                background_down: root.start_src
                on_release: root.start_game()

            # Options Button
            Button:
                background_normal: root.options_src
                background_down: root.options_src
                on_release: root.open_options()

            # Quit Button
            Button:
                background_normal: root.quit_src
                background_down: root.quit_src
                on_release: root.quit_game()
''')

class MenuScreen(Screen):
    logo_src = StringProperty(os.path.join(BASE_DIR, 'gameTitleLogo.png').replace('\\', '/'))
    start_src = StringProperty(os.path.join(BASE_DIR, 'startBtn.png').replace('\\', '/'))
    options_src = StringProperty(os.path.join(BASE_DIR, 'optionsBtn.png').replace('\\', '/'))
    quit_src = StringProperty(os.path.join(BASE_DIR, 'quitBtn.png').replace('\\', '/'))

    def start_game(self):
        print("Start Game Button Tapped")

    def open_options(self):
        print("Options Button Tapped")

    def quit_game(self):
        """Forces an absolute immediate termination of the window, bypassing IDLE blocks."""
        import os
        print("Forcing immediate window destruction...")
        App.get_running_app().stop()
        os._exit(0) # Drops the window hook immediately



class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        return sm

if __name__ == '__main__':
    GameApp().run()
