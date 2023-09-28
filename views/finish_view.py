import flet as ft
from modules.colors import color_mint1, color_mint2, color_mint3



def FinishView(page):

    content = (
        ft.Container(
            content = ft.Column(
                [
                    ft.Text('Спасибо,', size=80, text_align=ft.TextAlign.CENTER),
                    ft.Text('Приходите еще!', size=80, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(
                    content=ft.Text('В меню', size=80, color='#DFE1E5'),
                    #expand=True,
                    width=600,
                    on_click=lambda _: page.go('/menu'),
                    style=ft.ButtonStyle(
                    color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLUE,
                    },
                    bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.with_opacity(50,color_mint2)},
                    padding={ft.MaterialState.HOVERED: 20},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0, "": 1},
                    animation_duration=500,
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(1, color_mint3),
                        ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                    },
                    shape={
                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                    },
                        ),
                )
                    
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