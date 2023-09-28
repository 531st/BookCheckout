import flet as ft
from modules.colors import color_mint3

def LoadingView(page):

    content = (
        ft.Container(
            content = ft.Column(
                [
                    ft.Text('Секунду, заводим камеру...', size=80, text_align=ft.TextAlign.CENTER),
                    ft.ProgressRing(width=305, height=305, stroke_width = 5, color=color_mint3)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),     
            alignment=ft.alignment.center
        )
    )

    page.update()
    return content