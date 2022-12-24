from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen


class TitleScreen(MDScreen):
    """класс главного окна"""
    pass


class SettingScreen(MDScreen):
    """класс окна настроек"""
    pass


class RegistrationScreen(MDScreen):
    """класс формы регистрации"""
    pass


class TradeApp(MDApp):
    """Главное приложение"""

    def build(self):
        sm = MDScreenManager()
        sm.add_widget(TitleScreen(name='title'))
        sm.add_widget(SettingScreen(name='settings'))
        sm.add_widget(RegistrationScreen(name='registration_form'))
        return sm
