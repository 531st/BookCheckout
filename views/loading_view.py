import flet as ft

def LoadingView(page):

    content = (
        ft.Container(
            content = ft.Column(
                [
                    ft.Text('Секунду, заводим камеру...', size=80, text_align=ft.TextAlign.CENTER),
                    ft.ProgressRing(width=305, height=305, stroke_width = 5)
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