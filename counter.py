import flet as ft

def counter(page: ft.Page):
    """
    Hello World
    """
    page.title = "Hello World"

    page.add(
        ft.Text("Hello World!")
    )

ft.app(target=counter, port=5000, view=ft.WEB_BROWSER)
