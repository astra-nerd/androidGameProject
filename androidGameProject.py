import os
from kivy.utils import platform

# Force a 2400x1080 styled preview window ONLY when testing locally on your PC desktop
if platform not in ['android', 'ios']:
    from kivy.config import Config
    Config.set('graphics', 'width', '900')
    Config.set('graphics', 'height', '405')
    Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

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

        # 2. Interactive Button Menu Stack
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

<GameScreen>:
    canvas.before:
        Color:
            rgba: 0.15, 0.15, 0.18, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        
        Label:
            text: "Welcome to the 2D Game World!"
            font_size: '24sp'
            color: 1, 1, 1, 1
            size_hint_y: 0.8

        Button:
            text: "Back to Menu"
            size_hint: (None, None)
            size: (dp(150), dp(40))
            pos_hint: {'center_x': 0.5}
            on_release: root.back_to_menu()
''')

class MenuScreen(Screen):
    logo_src = StringProperty(os.path.join(BASE_DIR, 'gameTitleLogo.png').replace('\\', '/'))
    start_src = StringProperty(os.path.join(BASE_DIR, 'startBtn.png').replace('\\', '/'))
    options_src = StringProperty(os.path.join(BASE_DIR, 'optionsBtn.png').replace('\\', '/'))
    quit_src = StringProperty(os.path.join(BASE_DIR, 'quitBtn.png').replace('\\', '/'))

    def start_game(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game_play'

    def open_options(self):
        print("Options Button Tapped")

    def quit_game(self):
        import os as sys_os
        App.get_running_app().stop()
        sys_os._exit(0)

class GameScreen(Screen):
    def back_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game_play'))
        return sm

if __name__ == '__main__':
    GameApp().run()
