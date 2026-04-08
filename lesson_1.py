import flet as ft

def main_page (page: ft.Page):
    page.title='Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text('Hello')
    
    text_input = ft.TextField(label='Введите имя')
    
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND,
                                        color=ft.Colors.GREEN, icon_color=ft.Colors.RED)
    text_button = ft.TextButton('send')
    icon_button = ft.IconButton(icon=ft.Icons.SEND)
    page.add(text_hello, text_input, elevated_button, text_button, icon_button, )
ft.app(main_page, view=ft.AppView.WEB_BROWSER)