import flet as ft
from classes import *

async def main(page: ft.Page):
    app = MyApp()
    controls = ControlsPage()

    app.run(page)
    await controls.run(page)
    page.update()


if __name__ == "__main__":
    ft.run(main)