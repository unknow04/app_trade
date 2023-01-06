import json

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

import menu
from settings_db import SettingData
from _client.client import SocketClient


class TitleScreen(MDScreen):
    """класс главного окна"""
    menu = menu.MENU_RUS
    connect_status = False
    db = SettingData()

    def show_password(self):
        pass

    def connect_icon(self):
        if self.connect_status:
            return "lan-connect"
        else:
            return "lan-disconnect"

    def form_user_login(self, *args):
        print(args)
        if "" not in args:
            data = self.db.get_data()
            message = json.dumps({"login": {"email": args[0], "password": args[1]}})
            print(type(message))
            print(message)
            client = SocketClient()
            connect = client.connect_server(data[1], int(data[2]))
            if connect[0]["message"] == 200:
                client.message(message)
                response = client.get_response()
                print(response, "<<<<<<<<<<<")
                TitleScreen.connect_status = True
                self.ids['icon1'].icon = 'lan-connect'
                self.ids['icon1'].color = 'green'
            else:
                self.ids['icon1'].icon = 'lan-disconnect'
                self.ids['icon1'].color = 'red'
        else:
            self.ids['text1'].hint_text = 'Вы ничего не ввели'
            self.ids['text2'].hint_text = 'Вы ничего не ввели'

class SettingScreen(MDScreen):
    """класс окна настроек"""
    db = SettingData()

    def save_settings(self, *args):
        if args[0] and args[1] != "":
            self.ids['text4'].hint_text = ""
            self.ids['text5'].hint_text = ""
            self.db.save_data(*args)

    def load_settings(self):
        data = self.db.get_data()
        if data:
            return data
        else:
            return (0, "None data", "None data")


class RegistrationScreen(MDScreen):
    """класс формы регистрации"""

    def read_setting(self):
        pass


class TradeApp(MDApp):
    """Главное приложение"""

    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    def callback(self):
        pass

    def build(self):
        sm = MDScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        sm.add_widget(TitleScreen(name='title'))
        sm.add_widget(SettingScreen(name='settings'))
        sm.add_widget(RegistrationScreen(name='registration_form'))
        return sm


if __name__ == '__main__':
    TradeApp().run()
