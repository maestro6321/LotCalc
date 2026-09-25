import flet as ft

class MyApp:
    def __init__(self):
        # windows setting
        self.title = "LotCalc"
        self.window_width = 400
        self.window_height = 400
        self.resizable = False
        self.maximizable = False

        self.icon = "src/assets/icon.png"

        #layout settings
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.START

    def setup_page(self, page: ft.Page):
        page.title = self.title
        page.horizontal_alignment = self.horizontal_alignment
        page.vertical_alignment = self.vertical_alignment
        page.window.width = self.window_width
        page.window.height = self.window_height
        page.window.resizable = self.resizable
        page.window.maximizable = self.maximizable
        page.window.icon = self.icon

    def run(self, page: ft.Page):
        self.setup_page(page)